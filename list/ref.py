# n = 5

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


#     n = 5

# for i in range(1, n + 1):
    
#     spaces = " " * (n - i)
   
#     stars = "* " * n
    
#     print(spaces + stars)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# c = int(input("Enter your choice: "))

# if c == 1:
#     print("Result =", a + b)

# elif c == 2:
#     print("Result =", a - b)

# elif c == 3:
#     print("Result =", a * b)

# elif c == 4:
#     print("Result =", a / b)

# else:
#     print("Invalid choice")

#     # Predefined valid login credentials
# CORRECT_USERNAME = "admin"
# CORRECT_PASSWORD = "SecretPassword123"

# MAX_ATTEMPTS = 3

# print("--- Welcome to the Secure System ---")

# for attempt in range(1, MAX_ATTEMPTS + 1):
#     # Prompt the user for input
#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")
    
#     # Validate the credentials
#     if username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD:
#         print("\n✅ Access Granted! Welcome back.")
#         break  # Exit the loop entirely on successful login
#     else:
#         attempts_left = MAX_ATTEMPTS - attempt
#         print(f"❌ Incorrect credentials. Attempts remaining: {attempts_left}\n")
# else:
#     # This block executes ONLY if the loop finishes naturally without reaching the 'break'
#     print("⛔ Access Denied. You have been locked out due to too many failed attempts.")
# num = int(input("Enter a number: "))

# fact = 1

# while num > 0:
#     fact = fact * num
#     num = num - 1

# print("Factorial =", fact)

# num = int(input("Enter a number: "))

# temp = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if temp == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

def login(func):
    def check():
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "1234":
            func()
        else:
            print("Invalid credentials")

    return check


@login
def welcome():
    print("Login successful")


welcome()
