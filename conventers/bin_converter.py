def binary_to_int():
    """
    convert bin text to int from .txt file
    """
    with open('binary.txt', 'r') as file:
      content = file.read()
    content = content.splitlines()
    l = []
    for con in content:
      l.append(int(con,2))
    return l
