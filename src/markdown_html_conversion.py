from html_node import HTMLNode, LeafNode, ParentNode
from text_node import TextNode, TextType, textNode_to_htmlNode
from markdown_inline import text_to_textnode
from markdown_block import markdown_to_blocks, block_to_blocktype, extract_block_html_params
from test_suite import test



def children_block_to_html(parent_tag, block_text):
    # Helper function to convert text to HTML nodes
    def helper_text_to_html_node(text):
        html_nodes = []
        text_nodes = text_to_textnode(text)
        for node in text_nodes:
            html_node = textNode_to_htmlNode(node)
            html_nodes.append(html_node)
        return html_nodes
    
    child_nodes = []

    # For code block, handle text as a whole & preserve formatting
    if parent_tag == 'code':
        text_node = TextNode(block_text, TextType.TEXT)
        child_htmlnode = textNode_to_htmlNode(text_node)
        return [child_htmlnode]
    
    # For quote block, handle text as a whole & wrap content in <p> tags
    if parent_tag == 'blockquote':
        joined_text = block_text.replace('\n', ' ')
        subnodes = helper_text_to_html_node(joined_text)
        # subparent = ParentNode('p', subnodes)
        return subnodes
    
    # Split block text by newlines
    split_lines = block_text.split('\n')

    for line in split_lines:
        subnodes = helper_text_to_html_node(line)
        if parent_tag in ('ul', 'ol'):
            # For list items (ul/ol), wrap in <li> tags
            subparent = ParentNode('li', subnodes)
            child_nodes.append(subparent)
        else:
            # Add the subnodes directly if not a list
            child_nodes.extend(subnodes)

    return child_nodes


def markdown_to_htmlnode(markdown):
    html_node_list = []
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        # Extract HTML tag and text for the block
        html_tag, html_text = extract_block_html_params(block)

        # Create the parent HTML node with children
        parent_htmlnode = ParentNode(html_tag, children_block_to_html(html_tag, html_text))

        # Wrap 'code' blocks in <pre> tags
        if html_tag == 'code':
            parent_htmlnode = ParentNode('pre', [parent_htmlnode])
        
        # Append the parent HTML node to the list
        html_node_list.append(parent_htmlnode)

    # Wrap all nodes in a <div> tag
    return ParentNode('div', html_node_list)


if __name__ == '__main__':
    test_array = test.split('\n\n')
    '''
    for i in test_array:
        print(test_array.index(i))
        print(i)
        print('=====================')
    '''
    heading1, heading2, inline_text, link, heading3, ord_list, quote_block, code_block, heading4, simple_par, unord_list = test_array
    result = markdown_to_htmlnode(test)
    print(result.to_html())