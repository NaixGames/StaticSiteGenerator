from textnode import TextType, TextNode
from static_to_public import static_to_public
from extract_markdown import generate_pages_recursively

def main() -> None:
    static_to_public()

if __name__ == "__main__":
    main()
    generate_pages_recursively("content", "template.html", "public")