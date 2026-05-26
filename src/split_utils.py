import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type : TextType) -> list[TextNode]:
    new_output = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_output.append(node)
            continue

        node_text = node.text
        split_text = node_text.split(delimiter)
    

        if (len(split_text) % 2 == 0):
            raise Exception("Invalid Markdown syntax detected")


        delimiter_mode = 1
        for element in split_text:
            if (delimiter_mode == 1):
                created_node = TextNode(element, TextType.TEXT)
            else:
                created_node = TextNode(element, text_type)
            
            new_output.append(created_node)
            delimiter_mode *= -1

    
    return new_output

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    image_matches = matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    result = []

    for img in image_matches:
        result.append(img)

    return result

def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    links_matches = matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    result = []

    for img in links_matches:
        result.append(img)

    return result