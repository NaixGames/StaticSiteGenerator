import os
from markdown_to_html import markdown_to_html_node

def get_title(md_title: str) -> str:
    return md_title[2:]

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")

    for line in lines:
        if len(line) == 0:
            continue
        if line[0] != "#":
            return "The Markdown for this page doesnt have title and hence it is invalid"
        if line[1] != " ":
            return "The Markdown for this page doesnt have title and hence it is invalid"
        return get_title(line)
    
    return "The Markdown for this page doesnt have title and hence it is invalid"

def generate_page(from_path: str, template_path: str, des_path: str) -> None:
    print(f"Generating page from {from_path} to {des_path} using {template_path}")

    #load md
    abs_from_path = os.path.abspath(from_path)
    if not os.path.isfile(abs_from_path):
        raise Exception("GIVEN PATH FOR SOURCE IS NOT A MD FILE")
    with open(abs_from_path, "r") as f:
        md_text = f.read()

    #load template
    abs_template_path = os.path.abspath(template_path)
    if not os.path.isfile(abs_template_path):
        raise Exception("GIVEN PATH FOR TEMPLATE IS NOT A MD FILE")
    with open(abs_template_path, "r") as f:
        template_text = f.read()

    html_node = markdown_to_html_node(md_text)
    html = html_node.to_html()
    title = extract_title(md_text)
    
    generated_html = template_text.replace("{{ Title  }}", title)
    generated_html = template_text.replace("{{ Content }}", html)

    abs_dst_path = os.path.abspath(des_path)
    
    with open(abs_dst_path, "w") as f:
        template_text = f.write(generated_html)