from text_node import TextNode, TextType
import re

def split_nodes_delimeter(text_nodes, separator, type):
    new_nodes = []
    #print('all nodes: ', text_nodes)
    #print('node_list size: ', len(text_nodes))
    for node in text_nodes:
        #print('PARSING NODE: ', node)
        if node.text_type == TextType.TEXT and node.text.find(separator) != -1:
            split = node.text.split(separator)
            # print('SPLIT NODE: ', split)
            for i in range(len(split)):
                if split[i] == '':
                    continue
                if i % 2 == 1:
                    new_nodes.append(TextNode(split[i], type))
                else:
                    new_nodes.append(TextNode(split[i], TextType.TEXT))
        else:
            new_nodes.append(node)
    #print('final new nodes: ', new_nodes)
    return new_nodes

# newlist = [expression for item in iterable if condition == True]

def extract_markdown_image(text):
    # print(text)
    matches = re.findall(r'!\[(.*?)\]\((.*?)\)', text)
    # print(matches)
    if matches:
        valid_matches = re.findall(r'!\[([^\[\]\(\)]*)\]\(([^\[\]\(\)]*)\)', text)
        if not valid_matches:
            raise ValueError('Illegal markdown characters ([], ()) detected in image URL or alt text.')
        return valid_matches
    return []
    
def extract_markdown_link(text):
    ls = []
    matches = re.finditer(r'\[(.*?)\]\((.*?)\)', text)
    for match in matches:
        if match.start() != 0:
            if text[match.start() -1] == '!':
                continue
        ls.append((match.group(1), match.group(2)))
    return ls

def split_nodes_image(text_nodes):
    new_nodes = []
    #print('all nodes: ', text_nodes)
    #print('node_list size: ', len(text_nodes))
    for node in text_nodes:
        txt = node.text
        #print('PARSING NODE: ', node)
        images = extract_markdown_image(txt)
        if images == []:
            new_nodes.append(node)
            continue
        for alt_txt, url in images:
            substring = f'![{alt_txt}]({url})'
            split = txt.split(substring)
            if split[0] != '':
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_txt, TextType.IMAGE, url))
            pos = txt.index(substring) + len(substring)
            txt = txt[pos:]
        if txt != '':
            new_nodes.append(TextNode(txt, TextType.TEXT))
    return new_nodes

def split_nodes_link(text_nodes):
    new_nodes = []
    #print('all nodes: ', text_nodes)
    #print('node_list size: ', len(text_nodes))
    for node in text_nodes:
        txt = node.text
        #print('PARSING NODE: ', node)
        links = extract_markdown_link(txt)
        if links == [] and txt != '':
            new_nodes.append(node)
            continue
        for link_txt, url in links:
            substring = f'[{link_txt}]({url})'
            split = txt.split(substring)
            if split[0] != '':
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(link_txt, TextType.LINK, url))
            pos = txt.index(substring) + len(substring)
            txt = txt[pos:]
        if txt != '':
            new_nodes.append(TextNode(txt, TextType.TEXT))
    return new_nodes


def text_to_textnode(txt):
    nodes = [TextNode(txt, TextType.TEXT)]
    a = split_nodes_delimeter(nodes, '**', TextType.BOLD)
    b = split_nodes_delimeter(a, '*', TextType.ITALIC)
    c = split_nodes_delimeter(b, '`', TextType.CODE)
    d = split_nodes_image(c)
    e = split_nodes_link(d)
    return e