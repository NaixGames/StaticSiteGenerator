import unittest
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)

from block_type_utils import BlockType, block_to_block_type


class TestBlockTypeUtils(unittest.TestCase):
    def test_block_type_utils(self):
        text1 = "# This is a heading"
        text2 = "### This is also a heading"
        text3 = "#This is not a heading"

        #self.assertEqual(block_to_block_type(text1), BlockType.HEADING)
        #self.assertEqual(block_to_block_type(text2), BlockType.HEADING)
        #self.assertEqual(block_to_block_type(text3), BlockType.PARAGRAPH)

        text4 = "```\n This is valid code block text```"
        text5 = "```\n This is also valid code block text ```\n"
        text6 = "``` This is not valid code block text ```\n"
        
        self.assertEqual(block_to_block_type(text4), BlockType.CODE)
        self.assertEqual(block_to_block_type(text5), BlockType.CODE)
        self.assertEqual(block_to_block_type(text6), BlockType.PARAGRAPH)

        text7 = ">This is a quote text"
        text8 = "> This is also a quote text"
        text9 = " > Is not a quote text!"

        self.assertEqual(block_to_block_type(text7), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(text8), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(text9), BlockType.PARAGRAPH)

        text10 = "- This is\n- An unordered  list"
        text11 = "- This is not\n-an unordered list"
        self.assertEqual(block_to_block_type(text10), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(text11), BlockType.PARAGRAPH)

        text12 = "1. This is\n2. an ordered\n3. list"
        text13 = "0. This is\n1. not an ordered list"
        text14 = "0.This is not an ordered list"
        self.assertEqual(block_to_block_type(text12), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(text13), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(text14), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()