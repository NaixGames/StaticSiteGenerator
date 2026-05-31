from htmlnode import HTMLNode
from leafnode import LeafNode
from block_type_utils import BlockType, block_to_block_type
from conversion_utils import markdown_to_blocks
from split_utils import text_to_nodes

def child_text_to_html(text: str) -> list[HTMLNode]:
    textnodes = text_to_nodes(text)
    answer = []

    for tnode in textnodes:
        answer.append(tnode.text_node_to_html_node())

    return answer

def get_heading_amount(heading_text: str) -> int:
    for i in range(1,7):
        if heading_text[i] == " ":
            return i
        
    raise Exception("Not heading text passed to get_heading_amount function")

def get_coded_text(code_text: str) -> str:
    text = code_text[4:] #remove the ```\n"

    if text[-1] == "\n":
        return text[:-4]
    return text[:-3]

def get_quote_tex(quote_text: str) -> str:
    split_lines = quote_text.split("\n")
    ans = ""

    for line in split_lines:
        if (len(line) < 2):
            continue
        if line[1] == " ":
            ans += line[2:] + "\n"
            continue
        ans += line[1:]+"\n"
    return ans

def get_ordered_list_lines(text: str) -> list[str]:
    lines = text.split("\n")

    answer = []

    for line in lines:
        start_ind = line.find(". ")

        answer.append(line[start_ind+2:])

    return answer

def get_unordered_list_lines(text: str) -> list[str]:
    lines = text.split("\n")

    answer = []

    for line in lines:
        answer.append(line[2:])

    return answer



def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)


    base_node = HTMLNode("div")
    base_node.children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if (block_type == BlockType.HEADING):
            heading_amount = get_heading_amount(block)
            parent_node = HTMLNode(f"h{heading_amount}")
            parent_node.children = child_text_to_html(block[heading_amount+1:])
            base_node.children.append(parent_node)
            continue

        if (block_type == BlockType.CODE):
            pre_parent_node = HTMLNode("pre")
            parent_node = LeafNode("code") #Text in code block are not parsed! reason we use a leafblock
            pre_parent_node.children = [parent_node]
            parent_node.value = get_coded_text(block)
            base_node.children.append(pre_parent_node)
            continue

        if (block_type == BlockType.QUOTE):
            parent_node = HTMLNode("blockquote")
            qt = get_quote_tex(block)
            parent_node.children = child_text_to_html(qt)
            base_node.children.append(parent_node)
            continue

        if (block_type == BlockType.UNORDERED_LIST):
            unordered_elements = get_unordered_list_lines(block)

            parent_node = HTMLNode("ul")
            parent_node.children = []

            for line in unordered_elements:
                new_node = HTMLNode("li")
                new_node.children = child_text_to_html(line)
                parent_node.children.append(new_node)

            base_node.children.append(parent_node)
            continue

        if (block_type == BlockType.ORDERED_LIST):
            ordered_elements = get_ordered_list_lines(block)

            parent_node = HTMLNode("ol")
            parent_node.children = []

            for line in ordered_elements:
                new_node = HTMLNode("li")
                new_node.children = child_text_to_html(line)
                parent_node.children.append(new_node)

            base_node.children.append(parent_node)
            continue

        if block_type == BlockType.PARAGRAPH:
            parent_node = HTMLNode("p")
            block = block.replace("\n", " ")
            parent_node.children = child_text_to_html(block) #Maybe I should replace new line with spaces?
            base_node.children.append(parent_node)
            continue


        raise Exception("Request with block type that is not implemented")

    return base_node


