def create_notes_in_file():

    """
    pobiera zapisy z input
    tworzy plik
    kopiuje zapisy
    """
    import os
    webaddres = []
    line = input("Adress www: ")

    while line !='':
        webaddres.append(line)
        line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
    else:
        print("END")

    print(webaddres)

    dirname = os.getcwd()
    filename = input("Podaj nazwę pliku: ")
    filepath = os.path.join(dirname,filename)
    print(filepath)
    file = open (filepath, "w+")
    for x in webaddres:
        file.write(x+"\n")
    file.close()

def line_from_file_to_list():
    """
    pobiera nazwę pliku
    zapisuje je w liscie
    """
    import os
    filename =input('Enter filename with web addresses to read: ')
    while not os.path.isfile(filename):
        print("File does not exist. Try again: ")
        filename =input('Enter filename to read: ')
    webaddresses=[]
    with open(filename,'r') as file:
        for line in file:
            webaddresses.append(line.replace("\n",''))
            print(line)
    return(webaddresses)
