def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = data.split()
    list2 = []
    for i in list1:
        list2.append(len(i))
    return list2

# Read data from file
f = open("txt_file/data06.txt").read()
print(main(f))