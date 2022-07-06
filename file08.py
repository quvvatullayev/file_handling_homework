def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    max_list = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            max_list.append(int(data[i]))
        i += 1
    return max(max_list)

# Read data from file
f = open("txt_file/data08.txt").read()
print(main(f))