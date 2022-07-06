def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list_max = data.split('\n')
    list_h = []
    i = 0
    while i < len(list_max):
        list_h.append(len(list_max[i]))
        i += 1

    return max(list_h)
    
# Read data from file
f = open("txt_file/data10.txt").read()
print(main(f))