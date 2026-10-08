try:
    filename=input("enter a filename:")
    f=open(filename,"r")
    print("filefounded sucessfully")
    f.close()
except FileNotFoundError:
    print("filenotfound")

