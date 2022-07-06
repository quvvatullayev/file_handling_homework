def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    i = 0
    while i < len(data):
        if data[i].isalpha():
            x.append(data[i])
        i += 1
    return x

# Read data from file
f = open("txt_file/data04.txt").read()
print(main(f))