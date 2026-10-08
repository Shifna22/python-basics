f=open("compain.txt","r")
word=input("enter the word:")

data=f.read()

count=data.count(word)
print("word occus",count,"times")
f.close()

