from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Cant render parent node without a tag")
    
        if self.children == None or len(self.children)==0:
            raise ValueError("Cant render Parent Node without childrens")
        
        result = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result