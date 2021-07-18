def countWordsFromFile():
    fileName=input("enter the file name ")

    NumberOfWords=0

    file=open(fileName,'r')
    for Line in file :
        words=Line.split()
        NumberOfWords=NumberOfWords+len(words)

    print("number of words")
    print(NumberOfWords)


countWordsFromFile()

