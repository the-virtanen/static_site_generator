import unittest
from blocktype import *
from textnode import TextType

class TestBlockType(unittest.TestCase):
    def test_ordered_list(self):
        block = """1. sdf
2. 21345
3. ölkjasdf
4. alöksj"""
        expected_result = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(block), expected_result)

    def test_ordered_list_fail(self):
        block = """1. sdf
3. ölkjasdf
4. alöksj"""
        expected_result = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_result)

    def test_unordered_list(self):
        block =  "- what \n- is this\n- stuff"
        expected_result = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(block), expected_result)

    def test_unordered_list_fail(self):
        block =  "- what \n-is this\n- stuff" #missing space after dash
        expected_result = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_result)
    
    def test_quote(self):
        block =  ">what \n>is this\n>stuff"
        expected_result = BlockType.QUOTE
        self.assertEqual(block_to_block_type(block), expected_result)
    
    def test_quote_fail(self):
        block =  ">what \nis this\n>stuff" #missing >
        expected_result = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_result)

if __name__ == "__main__":
    unittest.main()


