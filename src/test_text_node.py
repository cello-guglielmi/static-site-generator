import unittest
from text_node import TextType, TextNode, textNode_to_htmlNode

class TestTextNode(unittest.TestCase):
    def test_eq_type(self):
        print('test_eq_type')
        print('EQUAL')
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        print(node)
        print(node2)
        self.assertEqual(node, node2)
        print('====================')

    def test_eq_link(self):
        print('test_eq_link')
        print('EQUAL')
        node = TextNode('This is a link (none) text node', TextType.LINK)
        node2 = TextNode('This is a link (none) text node', TextType.LINK)
        print(node)
        print(node2)
        self.assertEqual(node, node2)
        print('====================')

    def test_eq_link_false(self):
        print('test_eq_link_false')
        print('NOT EQUAL')
        node = TextNode('This is a link url text node', TextType.LINK, 'https://www.google.com')
        node2 = TextNode('This is a link url text node', TextType.LINK, 'https://www.reddit.com')
        print(node)
        print(node2)
        self.assertNotEqual(node, node2)
        print('====================')

    def test_eq_type_false(self):
        print('test_eq_type_false')
        print('NOT EQUAL')
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.ITALIC)
        print(node)
        print(node2)
        self.assertNotEqual(node, node2)
        print('====================')

    def test_eq_url(self):
        print('test_eq_url')
        print('EQUAL')
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        print(node)
        print(node2)
        self.assertEqual(node, node2)
        print('====================')

    def test_repr(self):
        print('test_repr')
        print('EQUAL')
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node_repr = "TextNode(This is a text node, TextType.TEXT, https://www.boot.dev)"
        print(node)
        print(node_repr)
        self.assertEqual(repr(node), node_repr)
        print('====================')

class TestTextNodeToHTMLNodeConversion(unittest.TestCase):
    def test_textNode_to_htmlNode_bold(self):
        # Test case for textNode_to_htmlNode() conversion with bold text
        print('test_textNode_to_htmlNode_bold')
        text_node = TextNode('This is bold text', TextType.BOLD)
        html_node = textNode_to_htmlNode(text_node)
        print(html_node)
        self.assertEqual(str(html_node), 'LeafNode(b, This is bold text, None)')
        print('====================')

    def test_textNode_to_htmlNode_text(self):
        # Test case for textNode_to_htmlNode() conversion with simple text
        print('test_textNode_to_htmlNode_text')
        text_node = TextNode('This is just simple text', TextType.TEXT)
        html_node = textNode_to_htmlNode(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value,'This is just simple text')
        print('====================')

    def test_textNode_to_htmlNode_image(self):
        # Test case for textNode_to_htmlNode() conversion with simple text
        print('test_textNode_to_htmlNode_text')
        text_node = TextNode('This is an image', TextType.IMAGE, 'https://www.google.com')
        html_node = textNode_to_htmlNode(text_node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value,'')
        self.assertEqual(
            html_node.props,
            {'src': 'https://www.google.com', 'alt': 'This is an image'}
        )
        print('====================')

    def test_textNode_to_htmlNode_type_error(self):
        # Test case for textNode_to_htmlNode() invalid type error
        print('test_textNode_to_htmlNode_type_error')
        with self.assertRaises(Exception):
            text_node = TextNode(text='This is just simple text', text_type='')
            html_node = textNode_to_htmlNode(text_node)
        print('Exception raised, invalid or missing type')
        print('====================')


if __name__ == '__main__':
    unittest.main()