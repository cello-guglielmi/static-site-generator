from html_node import HTMLNode, LeafNode, ParentNode
from text_node import TextNode, TextType, textNode_to_htmlNode
from markdown_inline import text_to_textnode
from markdown_block import markdown_to_blocks, block_to_blocktype, extract_block_html_params

test = '''
# The Tale of Sir Boots

## Chapter 1: The Beginning

This is a *simple* paragraph with some **bold** text and some *italics*.

Here's a [link to my cave](https://boots-cave.com) and some `inline code`.

### Shopping List

* Honey
* Berries
* Fish
* Maple syrup

### Daily Tasks

1. Wake up
2. Catch fish
3. Practice magic
4. Take a nap

> Sometimes the best magic is a good nap
> - Sir Boots

Here's some code I wrote:

```python
def greet_wizard():
    print("Hello, magical friend!")
    return "sparkles"
```

#### Final *Thoughts*

This should test:

* Headers (multiple levels)
* Paragraph text
* **Bold** and *italic* text
* Links and inline code
* Unordered lists
* Ordered lists
* Block quotes
'''

test2 = '> Sometimes the **best** magic is a good nap'

test3 = '''#### Final Thoughts

This should test:

* Headers (multiple levels)
* Paragraph text
* **Bold** and *italic* text
* Links and inline code
* Unordered lists
* Ordered lists
* Block quotes'''

#test = '* Headers (multiple levels)\n* **Bold** and *italic* text'
#test = '> Sometimes the **best** magic is a good nap\n> - Sir Boots'
#test = '#### Final *Thoughts*'


testcb = ('ul', 'Paragraph text\n**Bold** and *italic* text\nLinks and inline code')

from html_node import HTMLNode, LeafNode, ParentNode
from text_node import TextNode, TextType, textNode_to_htmlNode
from markdown_inline import text_to_textnode
from markdown_block import markdown_to_blocks, block_to_blocktype, extract_block_html_params
from test_suite import test


def children_block_to_html(parent_tag, block_text):
    child_nodes = []
    if parent_tag == 'code':
        text_node = TextNode(block_text, TextType.TEXT)
        child_htmlnode = textNode_to_htmlNode(text_node)
        child_nodes.append(child_htmlnode)
    else:
        split = block_text.split('\n')
        for i in split:
            #print('i is:', i)
            subnodes = []
            child_textnodes = text_to_textnode(i)
            #print('a:', child_textnodes)
            for node in child_textnodes:
                child_htmlnode = textNode_to_htmlNode(node)
                subnodes.append(child_htmlnode)
                #print('b:', child_htmlnode)
            if parent_tag in ('ul', 'ol'):
                subparent = ParentNode('li', subnodes)
                print(subparent)
                #print(subparent.to_html())
                child_nodes.append(subparent)
            else:
                child_nodes.extend(subnodes)
        if parent_tag == 'blockquote':
            subparent = ParentNode('p', child_nodes)
            child_nodes = [subparent]
    return child_nodes


def markdown_to_htmlnode(markdown):
    html_node_list = []
    blocks = markdown_to_blocks(markdown)
    #print(blocks)
    for block in blocks:
        this_type = block_to_blocktype(block)
        #block_types.append(this_type)
        #print(f'BLOCK: {blocks.index(block)+1}, {this_type}')
        #print(block)
        html_tag, html_text = extract_block_html_params(block)
        #print(html_tag, html_text)
        parent_htmlnode = ParentNode(html_tag, children_block_to_html(html_tag, html_text))
        if html_tag == 'code':
            parent_htmlnode = ParentNode('pre', [parent_htmlnode])
        #print('parent:', parent_htmlnode)
        #to_html = parent_htmlnode.to_html()
        #print(to_html)
        html_node_list.append(parent_htmlnode)
    div_node = ParentNode('div', html_node_list)
    #print(div_node)
    #print(div_node.to_html())
    return div_node

if __name__ == '__main__':
    test_array = test.split('\n\n')
    '''
    for i in test_array:
        print(test_array.index(i))
        print(i)
        print('=====================')
    '''
    heading1, heading2, inline_text, link, heading3, ord_list, quote_block, code_block, heading4, simple_par, unord_list = test_array
    result = markdown_to_htmlnode(link)
    print(result.to_html())