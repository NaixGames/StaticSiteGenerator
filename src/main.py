from textnode import TextType, TextNode
from static_to_public import static_to_public
from extract_markdown import generate_pages_recursively
import sys

def main() -> None:
    static_to_public()

if __name__ == "__main__":
    if (len(sys.argv)<2):
        basepath ="/"
    else:
        basepath = sys.argv[1]

    main()
    generate_pages_recursively("content", "template.html", "docs", basepath)