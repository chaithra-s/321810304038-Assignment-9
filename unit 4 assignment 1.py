#to read entire text file
def read(a):
        txt = open(a)
        print(txt.read())
a=input("enter the file name:")
read(a)

#to read first n lines
def readfirst(a, n):
        from itertools import islice
        with open(a) as f:
                for l in islice(f,n):
                        print(l,end ='')
a=input("enter the file name:")
readfirst(a,2)

#to append text to file abd display the text
def read(a):
        from itertools import islice
        with open(a,"w") as file:
                file.write("Python Exercises\n")
                file.write("Java Exercises")
        txt = open(a)
        print(txt.read())
read('anu.txt')

#to read last n lines of the file
def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,"lines from file:",f)
        for line in (file.readlines() [-n:]):
            print(line, end='')
name=input("enter the file name:" )
n= int(input("no of last lines to read:"))
try:
    LastNLines(name,n)
except:
    print("file error....")
    
#  to read file line by line and store it in variable
def read(a): 
    with open (a) as file:
         cse=file.readlines()
          print(cse)
a=input("enter the file name:")
read(a)


#to read file line by line and store it in list
def read(a):
        with open(a) as file:     
                list = file.readlines()
                print(list)
a=input("enter the file name:")
read(a)
