
# count = 5

# while count < 0:
#     print(count)
#     count = count+1  

# print("Blast off!")

# num = int(input("Enter a num: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#      num = num // 10
# print("Reverse num:", reverse)



# m=int(input("enter the num:"))
# sum=0
# while m>0:
#     digit=m%10
#     sum=sum+digit  # sum of digits
#     m=m//10
# print(sum)
#  
# balance = 10000

# while True:
#     print("\n1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     c = int(input("Enter your choice: "))

#     if c == 1:
#         amount = int(input("Enter deposit amount: "))
#         balance = balance + amount
#         print("Amount deposited successfully.")

#     elif c== 2:
#         amount = int(input("Enter withdrawal amount: "))

#         if amount <= balance:
#             balance = balance - amount
#             print("Please collect your cash.")
#         else:
#             print("Insufficient balance.")

#     elif choice == 3:
#         print("Current Balance:", balance)

#     elif choice == 4:
#         print("Thank you for using the ATM.")
#         break

#     else:
#         print("Invalid choice.")


# n=int(input("enter the num"))
# m=int(input("enter the num"))
# print("1.mul")
# print("2.add")
# print("3.sub")
# print("4.div")

# c=int(input("enter the choice:"))   #calculaator
# if(c==1):
#     print("res=",n*m)
# elif(c==2):
#     print("res=",n+m)
# elif(c==3):
#     print("res=",m-n)
# elif(c==4):
#     print("res=",n/m)
# else:
#     print("invalid choice")


correctpass="shifna12"
name="shifna"
maxattempt=3
inputname=(input("enter the name"))
inputpass=(input("enter the pass"))
for attempt in range(1,maxattempt-1):
    if(correctpass==inputpass and inputname==name):
        print("correct password u are welcome")
        break
    elif(inputpass!=correctpass and inputpass!=name):
        left=maxattempt-attempt
        print("invalid and",left)
    else:
        print("invalid and out attempt")

