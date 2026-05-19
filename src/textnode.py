from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text :str, text_type : TextType, url : str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_eq = self.text == other.text
        type_eq = self.text_type == other.text_type
        url_eq = self.url == other.url

        return text_eq and type_eq and url_eq
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self) -> LeafNode:
        if (self.text_type == TextType["TEXT"]):
            return LeafNode(None, self.text)
        if (self.text_type == TextType["BOLD"]):
            return LeafNode("b", self.text)
        if (self.text_type == TextType["ITALIC"]):
            return LeafNode("i", self.text)
        if (self.text_type == TextType["CODE"]):
            return LeafNode("code", self.text)
        if (self.text_type == TextType["LINK"]):
            return LeafNode("a", self.text, {"href":self.url})
        if (self.text_type == TextType["IMAGE"]):
            return LeafNode("img", "", {"src":self.url, "alt":self.text})
        
        raise Exception("TextNode type convertion to html not supported")
        
        