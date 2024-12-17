import unittest
from markdown_inline import split_nodes_delimeter, split_nodes_image, split_nodes_link, extract_markdown_image, extract_markdown_link, text_to_textnode
from markdown_block import markdown_to_blocks, block_to_blocktype
from text_node import TextNode, TextType

class TestMarkdownToBlocks(unittest.TestCase):
    # markdown_to_blocks() test cases
    def test_split_block_simple(self):
        # Case: Simple \n\n split
        print('test_split_block_simple')
        txt = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        result = markdown_to_blocks(txt)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        #print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_split_block_multiple_newlines(self):
        # Case: Excessive newlines
        print('test_split_block_multiple_newlines')
        txt = '# This is a heading\n\n\n\n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.'
        result = markdown_to_blocks(txt)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.']
        #print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_split_block_single(self):
        # Case: Only 1 block
        print('test_split_block_single')
        txt = '# This is a heading'
        result = markdown_to_blocks(txt)
        expected = ['# This is a heading']
        #print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_split_block_empty(self):
        # Case: Empty string
        print('test_split_block_empty')
        txt = ''
        result = markdown_to_blocks(txt)
        expected = []
        #print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')


class TestBlockToBlockType(unittest.TestCase):
    # block_to_blocktype() test cases

    def test_blocktype_suite(self):
        # Case: Excessive newlines
        print('test_blocktype_suite')
        test_cases = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "```\nThis is a code block\n```",
            "```python\n def hello():\n    return 'world'\n```",
            "> This is a blockquote.",
            "* Item 1\n* Item 2\n  * Sub-item 1\n  * Sub-item 2",
            "- Item 1\n- Item 2",
            "1. First item\n2. Second item\n3. Third item",
            "1. First item\n2. Second item\n    1. Sub-item 1\n    2. Sub-item 2",
            "This is just a regular text paragraph.",
            # "# Heading 1\nSome text here.\n\n> A quote block.\n\n1. First item\n2. Second item",
            # "Here is some text before the code block.\n\n```python\ndef add(a, b):\n    return a + b\n```\nAnd more text after the code block."
        ]
        result = []
        for case in test_cases:
            the_type = block_to_blocktype(case)
            #print(f'{case} = {the_type}')
            result.append(the_type)
        expected = [
            'heading',
            'heading',
            'heading',
            'code_block',
            'code_block',
            'quote_block',
            'unord_list',
            'unord_list',
            'ord_list',
            'ord_list',
            'paragraph',
        ]
        #print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

if __name__ == '__main__':
    unittest.main()