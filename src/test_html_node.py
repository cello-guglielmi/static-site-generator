import unittest
from html_node import HTMLNode, LeafNode, ParentNode

# Testing values
    # self.assertEqual(node.to_html(), "<p>expected html</p>")
    # self.assertNotEqual(node.to_html(), "wrong html")

# Testing exceptions
    # with self.assertRaises(ValueError):
    #     bad_node = ParentNode(None, [])
    #     bad_node.to_html()

class TestHTMLNode(unittest.TestCase):
    '''
    def test_eq_type(self):
        print('test_eq_type')
        print('EQUAL')
        node1 = HTMLNode('p', 'this is text', None, None)
        node2 = HTMLNode('p', 'this is text', None, None)
        print(node1)
        print(node2)
        self.assertEqual(node1, node2)
        print('====================')

    def test_repr(self):
        print('test_repr')
        print('EQUAL')
        node = HTMLNode('p', 'this is text', None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        node_repr = "HTMLNode(p, this is text, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        node_propstohtml = ' href=\"https://www.google.com\" target=\"_blank\"'
        print(node)
        print(node_repr)
        print(node.props_to_html())
        print(node_propstohtml)
        self.assertEqual(repr(node), node_repr)
        print('====================')

    def testleaf_eq_type(self):
        print('testleaf_eq_type')
        print('EQUAL')
        node1 = LeafNode('a', 'this is text')
        node2 = LeafNode('a', 'this is text')
        print(node1)
        print(node2)
        self.assertEqual(node1, node2)
        print('====================')

    def testleaf_tohtml(self):
        print('testleaf_tohtml')
        print('EQUAL')
        node1 = LeafNode('a', 'this is text')
        node1tohtml = '<a>this is text</a>'
        print(node1.to_html())
        print(node1tohtml)
        self.assertEqual(node1.to_html(), node1tohtml)
        print('====================')
        '''
    
    def testparent_tohtml(self):
        # Setting node variables
        props1 = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        props2 = {
            "href": "https://www.reddit.com", 
            "target": "_molasses",
        }
        leaf1 = LeafNode('i', '!this is leaf node 1 text!')
        leaf2 = LeafNode('b', '!this is leaf node 2 text!')
        leaf3 = LeafNode('p', '!this is leaf node 3 text!', props1)
        pnode1 = ParentNode('p', [leaf1, leaf2])
        pnode2 = ParentNode('a', [pnode1, leaf3], props2)

        # Test case for to_html() method
        method_result = pnode2.to_html()
        expected = '<a href="https://www.reddit.com" target="_molasses"><p><i>!this is leaf node 1 text!</i><b>!this is leaf node 2 text!</b></p><p href="https://www.google.com" target="_blank">!this is leaf node 3 text!</p></a>'
        self.assertEqual(method_result, expected)

    def testparent_errors(self):
        # Test case for no tag
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode('b', 'some text')])
            node.to_html()
        
        # Test case for empty children
        with self.assertRaises(ValueError):
            node = ParentNode('div', [])
            node.to_html()


if __name__ == '__main__':
    unittest.main()