

def markdown_to_blocks(markdown : str) -> list[str]:
    pre_result = markdown.split("\n\n")
    #clean each block so it makes sense
    result = []
    
    for element in pre_result:
        element = element.strip()
        if (element == "" or element == "\n"):
            continue

        result.append(element)

    return result
