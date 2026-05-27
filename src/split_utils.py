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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    answer = []
    for node in old_nodes:
        processed_text = node.text
        extracted_images = extract_markdown_images(processed_text)

        if len(extracted_images) == 0:
            answer.append(node)
            continue
        
        for image_ext in extracted_images:
            splited_text = processed_text.split(f"![{image_ext[0]}]({image_ext[1]})", 1)

            first_half = splited_text[0]
            if (first_half != ""):
                created_node = TextNode(first_half, TextType.TEXT)
                answer.append(created_node)

            created_node = TextNode(image_ext[0], TextType.IMAGE,  image_ext[1])
            answer.append(created_node)

            processed_text = splited_text[1]
                
                
        if (processed_text != ""):
            created_node = TextNode(processed_text, TextType.TEXT)
            answer.append(created_node)

    return answer
    

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    answer = []
    for node in old_nodes:
        processed_text = node.text
        extracted_links = extract_markdown_links(processed_text)

        if len(extracted_links) == 0:
            answer.append(node)
            continue
        
        for url_ext in extracted_links:
            splited_text = processed_text.split(f"[{url_ext[0]}]({url_ext[1]})", 1)

            first_half = splited_text[0]
            if (first_half != ""):
                created_node = TextNode(first_half, TextType.TEXT)
                answer.append(created_node)

            created_node = TextNode(url_ext[0], TextType.LINK,  url_ext[1])
            answer.append(created_node)

            processed_text = splited_text[1]
                
                
        if (processed_text != ""):
            created_node = TextNode(processed_text, TextType.TEXT)
            answer.append(created_node)

    return answer