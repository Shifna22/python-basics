file=open("attendance.txt","r")
longest=""
for line in file:
    if len(line)>len(longest):
        longest=line
file.close()

print("longest line:",longest)

