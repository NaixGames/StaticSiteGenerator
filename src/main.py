from textnode import TextType, TextNode

def main() -> None:
    dummy_text_node = TextNode("This is some anchor text", TextType["LINK"], "https;//potito.com")
    print(dummy_text_node)

if __name__ == "__main__":
    main()