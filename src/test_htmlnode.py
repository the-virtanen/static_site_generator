import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_prop_html(self):
        node =  HTMLNode( props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href:"https://www.google.com" target:"_blank"')
    
#LeafNode    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello no tag")
        self.assertEqual(node.to_html(), "Hello no tag")
    """
    def test_leaf_to_html_children(self):
        node = LeafNode("p", "Hello no tag",["one","two"])
        self.assertRaises(node.to_html(), ValueError)
    """
if __name__ == "__main__":
    unittest.main()
