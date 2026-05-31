from textnode import TextType, TextNode
from static_to_public import static_to_public
from extract_markdown import generate_page

def main() -> None:
    static_to_public()

if __name__ == "__main__":
    main()
    generate_page("content/index.md", "template.html", "public/index.html")