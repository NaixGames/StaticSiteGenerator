import unittest
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)


from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf1 = LeafNode("h1", "testing")
        leaf2 = LeafNode("h2", "testing too", {"href": "https://www.google.com"})

        self.assertEqual(leaf1.props_to_html(), "")
        self.assertEqual(leaf2.props_to_html(), " href=\"https://www.google.com\"")

        leaf3 = LeafNode("p", "Hello, world!")
        self.assertEqual(leaf3.to_html(), "<p>Hello, world!</p>")

        leaf4 = LeafNode("p", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(leaf4.to_html(), "<p href=\"https://www.google.com\">Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()