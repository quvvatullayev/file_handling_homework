def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    for i in data.split(','):
        x.append(int(i))

    return x


# Read data from file
f = open("txt_file/data01.txt").read()
print(main(f))