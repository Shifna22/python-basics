try:
    f=open("filename.txt","r")
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("filenot found")
except PermissionError:
    print("permission error")
