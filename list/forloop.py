# for i in range(30):
#     print(i)

# for i in range(10,30):
#     print(i)

# for i in range(0,20,5):
#     print(i)

# for i in range(20):
#     print(i,i+5)

# for i in range(5):
#     print("*", end = " ")

#for i in range(8):
    #for j in range(5):
        #print(j, end = " ")
    #print()


#for i in range(1,5):
    #for j in range(1,i+1):# pattern printing (h)(print(j/i))
        #print(j,end=" ")
    #print()


#for i in range(1,5):
    #for j in range(1,i+1):# pattern printing (h)(print(j/i))
        #print(i,end=" ")
    #print()


#for i in range(5,0,-1):
    #for j in range(5,i-1,-1): #pattern printing 
        #print(j,end=" ")
    #print()
  


#* 
#* * 
#* * * 
#* * * * 
#* * * * * 



#n=0
#for i in range(0,5):
     #for j in range(1,i+2): 
         #print(n, end=" ") 
         #n=n+1 #number pattern (half pyramid)       
     #print()
#0 
#1 2 
#3 4 5 
#6 7 8 9 
#10 11 12 13 14


#for i in range(0,6):
    #for j in range(5):#pattern printing 
        #print("*",end=" ")
    #print()
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 

#n=5
#for i in range(n,0,-1):
     #for j in range(i):  
         #print("*", end=" ") #number pattern inverse (half pyramid)
         #n=n+1
     #print()
#* * * * * 
#* * * * 
#* * * 
#* * 
#*
# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)


#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 


# n = 5
# for i in range(n, 0, -1):
#     print("* " * i)

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 



# n = 5

# for i in range(5):
#     print(" " * i + "*" * (9 - 2 * i))

# *********
#  *******
#   *****
#    ***
#     *

# n=5

# for i in range(1,n,+ 1):
#    print(" " * (n - i) + "*" * i)
#  for i in range(5):
#       print(" " * i + "*" * (9 - 2 * i))

# n=5
# for i in range(1,n,1):
#   print(" " * (n -i) + "*" * i)

# n=5
# for i in range(1, n + 1):
#    print(" " * (n - i) + "* " * i)

# for i in range( n,0,-1):
#     print(" " * (n - i) + "* " * i)
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# 
# for i in range(5, 0, -1):
#  print("* " * i)
 
# for i in range(1,5+1):
#  print("* " * i)

# * * * * 
# * * * 
# * * 
# * 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 




# for i in range(1, 5 + 1):
#     print("*" * i + " " * (2 * (5 - i) + 1) + "*" * i)

# for i in range(5- 1, 0, -1):
#     print("*" * i + " " * (2 * (5- i) + 1) + "*" * i)

# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *



# for i in range(1, 4 + 1):
#     print("* " * i)           

# for i in range(4- 1, 0, -1):
#     print("* " * i)

# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# *

# for i in range(1, 8):
#     s1 = " " * (8- i)
#     s2= "* " * 8
#     print(s1+ s2)
#        * * * * * * * * 
#       * * * * * * * * 
#      * * * * * * * * 
#     * * * * * * * * 
#    * * * * * * * * 
#   * * * * * * * * 
#  * * * * * * * *

# for i in range(10,0,-1):
#    if(i==10):
#     print("*" * i)
#    elif(i==1):
#     print("*" * i)
#    else:
#      print("*"+" "*(i-2)+"*")
# n=5
# for i in range(n):
#     for j in range(n):
#       if i==0 or i==n-1 or j==0 or j==n-1 :
#          print("*",end=" ")

#       else:
#          print(" ",end=" ")

#     print()
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * *
# n=int(input())
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     if i==j:#1001001001
#       print("1",end="")
#     else:
#       print("0",end="")
# print()
n=6
for i in range(n,0,-1):
    if(i==n):
     print("*" * i)
    elif(i==1):      #hollow taingle
     print("*" * i)
    else:
       print("*"+" "*(i-2)+"*")
for i in range(1,n+1):
    if(i==n):
     print("*" * i)
    elif(i==1):      #hollow taingle
     print("*" * i)
    else:
       print("*"+" "*(i-2)+"*")
