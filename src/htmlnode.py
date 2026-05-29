from __future__ import annotations

class HTMLNode:
    def __init__(self, tag : str = None, value : str = None, children : list[HTMLNode] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):        
        answer = f"<{self.tag}{self.props_to_html()}>"

        for node in self.children:
            answer += node.to_html()

        answer += f"</{self.tag}>"
        
        return answer
    
    def props_to_html(self):
        if (self.props == None or len(self.props) == 0):
            return ""
        
        answer = ""

        for key in self.props:
            answer += f" {key}=\"{self.props[key]}\""
        
        return answer

    def __repr__(self):
        answer = f"Tag: {self.tag} \n"
        answer += f"Value: {self.value} \n"
        answer += "Children: "
        for child in self.children:
            answer += str(child) + "\n"
        answer += f"Props: {self.props_to_html()}"
        return answer