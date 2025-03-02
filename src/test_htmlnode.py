import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a","This is a link", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(repr(node), "HTMLNode(a, This is a link, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_props_to_html(self):
        node = HTMLNode("a","This is a link", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_empty_tag(self):
        node = HTMLNode(None,"This is not a link", None, None)
        self.assertIsNone(node.tag)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">This is a link</a>")

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