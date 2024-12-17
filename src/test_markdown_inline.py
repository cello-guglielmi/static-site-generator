import unittest
from markdown_inline import split_nodes_delimeter, split_nodes_image, split_nodes_link, extract_markdown_image, extract_markdown_link, text_to_textnode
from text_node import TextNode, TextType

class TestNodeSplitDelimiter(unittest.TestCase):
    '''
    def test_split_markdown_code(self):
        # Test case for split_markdown() with a code marked text
        print('test_split_markdown_bold')
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        expected = [TextNode('This is text with a ', TextType.TEXT, None), TextNode('code block', TextType.CODE, None), TextNode(' word', TextType.TEXT, None)]
        print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_markdown_multiword(self):
        # Test case for split_markdown() with multiple words within the delimiter
        print('test_split_markdown_multiword')
        node = TextNode("These two words **ARE BOLD**", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        expected = [TextNode('These two words ', TextType.TEXT, None), TextNode('ARE BOLD', TextType.BOLD, None)]
        print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_markdown_double(self):
        # Test case for split_markdown() with multiple occurances of the same type
        print('test_split_markdown_double')
        node = TextNode("These **TWO** words are **BOLD**", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        expected = [TextNode('These ', TextType.TEXT, None), TextNode('TWO', TextType.BOLD, None), TextNode(' words are ', TextType.TEXT, None), TextNode('BOLD', TextType.BOLD, None)]
        print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_markdown_double_diff(self):
        # Test case for split_markdown() with multiple occurances of different types
        print('test_split_markdown_double_diff')
        node = TextNode("This is *ITALIC* and this is **BOLD**", TextType.TEXT)
        new_nodes = split_nodes_delimeter(split_nodes_delimeter([node], "**", TextType.BOLD), "*", TextType.ITALIC)
        expected = [TextNode('This is ', TextType.TEXT, None), TextNode('ITALIC', TextType.ITALIC, None), TextNode(' and this is ', TextType.TEXT, None), TextNode('BOLD', TextType.BOLD, None)]
        print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_markdown_multinode(self):
        # Test case for split_markdown() function with multiple nodes
        print('test_split_markdown_multinode')
        node1 = TextNode("This one word is **BOLD**", TextType.TEXT)
        node2 = TextNode("WHOLE SENTENCE IS BOLD", TextType.BOLD)
        node3 = TextNode("This is just text", TextType.TEXT)
        node_list = [node1, node2, node3]
        new_nodes = split_nodes_delimeter(node_list, "**", TextType.BOLD)
        expected = [TextNode('This one word is ', TextType.TEXT, None), TextNode('BOLD', TextType.BOLD, None), TextNode('WHOLE SENTENCE IS BOLD', TextType.BOLD, None), TextNode('This is just text', TextType.TEXT, None)]
        print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')
    '''

class TestExtractImageLink(unittest.TestCase):
    '''
    def test_extract_image(self):
        print('test_extract_image')
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_image(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_extract_link(self):
        print('test_extract_link')
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_extract_special_char(self):
        print('test_extract_special_char')
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_extract_nested(self):
        print('test_extract_nested')
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_extract_empty(self):
        print('test_extract_empty')
        text = "This is text with a link [](https://www.boot.dev) and [](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        expected = [("", "https://www.boot.dev"), ("", "https://www.youtube.com/@bootdotdev")]
        print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')
    '''
    # Errors
    '''
    def test_extract_empty(self):
        print('test_extract_empty')
        text = "This is text with a link [(INVALID PAR)](https://www.boot.dev) and [(empty)](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        print(result)
        expected = [("", "https://www.boot.dev"), ("(empty)", "https://www.youtube.com/@bootdotdev")]

        print('====================')

    def test_extract_closing_missing(self):
        print('test_extract_closing_missing')
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_link(text)
        #print(result)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)
        print('====================')
    '''

class TestNodeSplitMarkdown(unittest.TestCase):
    '''
    # split_nodes_image() test cases
    def test_split_image(self):
        # Case: An image
        # Case: Multiple images
        # Case: Text at the end
        print('test_split_image')
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), ![google](https://google.png) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) okay?", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [TextNode('This is text with a ', TextType.TEXT, None), 
                    TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'), 
                    TextNode(', ', TextType.TEXT, None), 
                    TextNode('google', TextType.IMAGE, 'https://google.png'), 
                    TextNode(' and ', TextType.TEXT, None), 
                    TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'), 
                    TextNode(' okay?', TextType.TEXT, None),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    # split_nodes_link() test cases
    def test_split_link(self):
        # Case: A link
        # Case: 2 links
        # Case: Link at the end
        print('test_split_link')
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_link_only_text(self):
        # Case: No markdown formatted links
        print('test_split_link_only_text')
        node = TextNode("This is text without properly formatted link (https://www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node,])
        expected = [TextNode("This is text without properly formatted link (https://www.boot.dev)", TextType.TEXT)]
        # print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_link_beginning(self):
        # Case: Link at beginning
        print('test_split_link_beginning')
        node = TextNode("[reddit r/all](https://www.reddit.com/r/all) is a cool website!", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [TextNode("reddit r/all", TextType.LINK, 'https://www.reddit.com/r/all'),
                    TextNode(" is a cool website!", TextType.TEXT),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')

    def test_split_link_empty(self):
        # Case: Empty string
        print('test_split_link_empty')
        node = TextNode('', TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = []
        # print('EXPECT: ', expected)
        print('RESULT: ', new_nodes)
        self.assertEqual(new_nodes, expected)
        print('====================')
    '''

class TestTextToTextNode(unittest.TestCase):
    # text_to_textnode() test cases
    def test_text_to_textnode_all(self):
        # Case: Multiple markdown elements - all
        # Case: Element at the end
        print('test_text_to_textnode_all')
        txt = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = text_to_textnode(txt)
        expected = [TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_text_to_textnode_empty(self):
        # Case: Empty elements
        print('test_text_to_textnode_empty')
        txt = 'This is (empty bold text) ** ** with an (empty code block) ` ` and an (empty link) [ ]( )'
        result = text_to_textnode(txt)
        expected = [TextNode("This is (empty bold text) ", TextType.TEXT),
                    TextNode(" ", TextType.BOLD),
                    TextNode(" with an (empty code block) ", TextType.TEXT),
                    TextNode(" ", TextType.CODE),
                    TextNode(" and an (empty link) ", TextType.TEXT),
                    TextNode(" ", TextType.LINK, " "),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')

    def test_text_to_textnode_consecutive(self):
        # Case: Consecutive elements
        # Case: Element at beginning
        print('test_text_to_textnode_consecutive')
        txt = '**This**`code block`*is nice*.'
        result = text_to_textnode(txt)
        expected = [TextNode("This", TextType.BOLD),
                    TextNode("code block", TextType.CODE),
                    TextNode("is nice", TextType.ITALIC),
                    TextNode(".", TextType.TEXT),
                    ]
        # print('EXPECT: ', expected)
        print('RESULT: ', result)
        self.assertEqual(result, expected)
        print('====================')


if __name__ == '__main__':
    unittest.main()