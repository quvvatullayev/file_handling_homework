def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sum = 0
    for i in data:
        sum += 1
    return sum

# Read data from file
f = open("txt_file/data02.txt").read()
print(main(f))