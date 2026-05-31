from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(text: str) -> bool:
    if (text[0] != "#"):
        return False
    
    for i in range(1, 7):
        if i >= len(text):
            return False
        
        if text[i] == " ":
            return i < len(text) - 1
        
        if text[i] != "#":
            return False

        
def is_code_block(text: str) -> bool:
    if (text[0:4] != "```\n"):
        return False
    
    if (text[-3:] != "```" and text[-4:] != "```\n"):
        return False
    
    return True

def is_quote_block(text: str) -> bool:
    return text[0] == ">"

def is_unordered_list(text: str) -> bool:
    splited_lines = text.split("\n")

    for line in splited_lines:
        if line[0: 2] != "- ":
            return False
        
    return True

def is_ordered_list(text: str) -> bool:
    splited_lines = text.split("\n")

    for i in range(0, len(splited_lines)):
        line = splited_lines[i]

        start_ind = line.find(". ")
        if (start_ind == -1):
            return False
        
        if line[0:start_ind + 2] != f"{i+1}. ":
            return False
        
    return True

def block_to_block_type(text : str) -> BlockType:
    if (is_heading(text)):
        return BlockType.HEADING
    if (is_code_block(text)):
        return BlockType.CODE
    if (is_quote_block(text)):
        return BlockType.QUOTE
    if (is_unordered_list(text)):
        return BlockType.UNORDERED_LIST
    if (is_ordered_list(text)):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH