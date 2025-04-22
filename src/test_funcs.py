import unittest
from text_function import text_node_to_html_node
from textnode import *

class TestFuncsNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_link(self):
        t1 = TextNode("hello", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(t1)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {'href': 'https://www.boot.dev'})


if __name__ == "__main__":
    unittest.main()