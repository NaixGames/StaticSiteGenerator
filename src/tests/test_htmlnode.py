import unittest
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)


from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        html1 = HTMLNode("h1", "testing")
        html2 = HTMLNode("h2", "testing too", html1, {"href": "https://www.google.com"})

        self.assertEqual(html1.props_to_html(), "")
        self.assertEqual(html2.props_to_html(), " href=\"https://www.google.com\"")

if __name__ == "__main__":
    unittest.main()