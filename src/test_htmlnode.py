import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        html1 = HTMLNode("h1", "testing")
        html2 = HTMLNode("h2", "testing too", html1, {"href": "https://www.google.com"})

        self.assertEqual(html1.props_to_html(), "")
        self.assertEqual(html2.props_to_html(), " href=\"https://www.google.com\"")

if __name__ == "__main__":
    unittest.main()