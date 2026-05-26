import unittest
from textnode import TextNode, TextType
from split_utils import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestTSplitUtils(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(len(new_nodes), len(expected_result))

        for i in range(0, len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_result[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_result[i].text_type)

    def test_bf_split(self):
        node = TextNode("This is text with a **bf block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bf block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(len(new_nodes), len(expected_result))

        for i in range(0, len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_result[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_result[i].text_type)

    def test_bf_and_code_split(self):
        node = TextNode("This is text with a `code block` word and a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(len(new_nodes), len(expected_result))

        for i in range(0, len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_result[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_result[i].text_type)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
, matches)


if __name__ == "__main__":
    unittest.main()