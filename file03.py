def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            x.append(data[i])
        i += 1
    return x
    
# Read data from file
f = open("txt_file/data03.txt").read()
print(main(f))