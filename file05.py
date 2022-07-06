def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = []
    son = 0
    harf = 0
    i = 0
    while i < len(data):
        if data[i].isalpha():
            harf += 1
        elif data[i].isdigit():
            son += 1

        i += 1
    list1.append(son)
    list1.append(harf)


    return list1
    
# Read data from file
f = open("txt_file/data05.txt").read()
print(main(f))