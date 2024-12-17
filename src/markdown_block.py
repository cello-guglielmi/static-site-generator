#from node_text import
import re



def markdown_to_blocks(markdown):
    markdown = markdown.split('\n\n')
    split = []
    for i in markdown:
        if i == '':
            continue
        split.append(i.strip())
    return split


def block_to_blocktype(block):
    block_types = {
        'heading': re.search(r'^(#{1,6}\s)', block),
        'code_block': re.search(r'^```.*?```$', block, re.DOTALL),
        'quote_block': re.search(r'^>\s', block, re.MULTILINE),
        'unord_list': re.search(r'^\*|-\s', block, re.MULTILINE),
        'ord_list': re.match(r'^1\.\s', block),
        }
    if block_types['ord_list']:
        list = block.split('\n')
        for index, line in enumerate(list):
            pattern = f'^{index+ 1}\.\s'
            match = re.match(pattern, line)
            if not match:
                block_types['ord_list'] = False
        block_types['ord_list'] = True

    for block_type in block_types:
        if block_types[block_type]:
            return block_type
    return 'paragraph'

def extract_block_html_params(block):
    tag = 'p'
    text = block
    types = {
        'h': re.search(r'^#{1,6}\s(.*)', block, re.DOTALL),
        'code': re.search(r'^```\w*\s(.*)\s```$', block, re.DOTALL),
        'blockquote': re.search(r'^>\s(.*)', block, re.MULTILINE),
        'ul': re.search(r'^\*\s|^-\s', block, re.MULTILINE),
        'ol': re.match(r'^1\.\s(.*)', block),
        }

    if types['ol']:
        txt = []
        list = block.split('\n')
        for index, line in enumerate(list):
            pattern = f'^{index+ 1}\.\s(.*)'
            match = re.search(pattern, line)
            if not match:
                types['ol'] = False
                break
            txt.append(match.group(1))
        text = '\n'.join(txt)

    if types['ul']:
        txt = []
        list = block.split('\n')
        for line in list:
            item = re.search(r'^\*\s(.*)|^-\s(.*)', line)
            if item.group(1):
                txt.append(item.group(1))
            elif item.group(2):
                txt.append(item.group(2))
        text = '\n'.join(txt)

    if types['blockquote']:
        txt = []
        list = block.split('\n')
        for index in range(len(list)):
            line = re.search(r'^>\s(.*)', list[index])
            if line:
                txt.append(line.group(1))
        text = '\n'.join(txt)

    for block_type in types:
        if types[block_type]:
            tag = block_type
            break
    
    if tag == 'code' or tag == 'h':
        text = types[tag].group(1)

    if tag == 'h':
        num = block[0:5].count('#')
        tag = f'h{num}'

    return (tag, text)