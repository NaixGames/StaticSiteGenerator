from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag : str = None, value : str = None, props: dict[str, str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if (self.value == None or self.value == ""):
            raise ValueError("LeafNode needs to have a value to be rendered!")
        
        if (self.tag == None or self.tag == ""):
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        answer = f"Tag: {self.tag} \n"
        answer += f"Value: {self.value} \n"
        answer += f"Props: {self.props_to_html()}"
        return answer