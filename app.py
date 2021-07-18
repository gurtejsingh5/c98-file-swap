f=open("test.txt")
fileLines=f.readlines()
for line in fileLines:
    print(line)

introstring="my name, is, gurtej. i am 15, years old"
words=introstring.split(",")
print(words)                 

def greet(name):
    print("hello,"+name+"how are u?")


greet("gurtej")    