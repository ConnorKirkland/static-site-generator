from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, TextNode2):
        return self.text == TextNode2.text and self.text_type == TextNode2.text_type and self.url == TextNode2.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {(self.text_type.value)}, {self.url})"

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError("invalid TextType")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href":{text_node.url}})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})