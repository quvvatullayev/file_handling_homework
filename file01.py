def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    return list(data)


# Read data from file
f = open("data01.txt").read()
print(main(f))