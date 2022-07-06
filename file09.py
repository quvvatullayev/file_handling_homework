def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    min_list = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            min_list.append(int(data[i]))
        i += 1
    return min(min_list)

# Read data from file
f = open("txt_file/data09.txt").read()
print(main(f))