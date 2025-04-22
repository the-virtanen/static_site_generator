import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

#ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_tree(self):
        grandchild_node = LeafNode("b", "grandchild")
        gchild2 = LeafNode("j", "perjantai")
        gchild3 = LeafNode("i", "here we go!")
        child_node = ParentNode("span",[grandchild_node,gchild3])
        parent_node = ParentNode("div", [child_node, gchild2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><i>here we go!</i></span><j>perjantai</j></div>"
        )

if __name__ == "__main__":
    unittest.main()
