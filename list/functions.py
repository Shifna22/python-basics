

#factorail
num =int(input("Enter a num: "))
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1
print("Factorial =", fact)
#palindrome 
num = int(input("Enter a number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if temp == reverse:      # palinfdrome + functions

    print("Palindrome")
else:
    print("Not Palindrome")
#welcome deco
def welcome(func):
    def display():
       print("Welcome to Python")
    func()
    return display# wecome decorator

#executional dec
def execution(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@execution
def message():
    print("Hello Python")
message()
def message():
    print("Have a nice day!")
message()




#even genratoe
def even_generator(n):
    for i in range(0, n+ 1, 2):
        yield i
n= 10
print("Even numbers up to {n}:")
for number in even_generator(n):
    print(number, end=" ")

#fibb generator
def fibonacci(n):
  a = 0
  b = 1
  for i in range(n):
    yield a
    a, b = b, a + b
n = int(input("enter the no:"))
for num in fibonacci(n):
  print(num)

#login

def login(func):
    def check():
      name=(input("enter the name:"))
      password=int(input("enter the password:"))
      if name=="shifna" and password==1234:
        func()
      else:
        print("invalid credencials")
    return check
@login
def welcome():
   print("login success")

welcome()

#exextion

def execution(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function is completed")
    return wrapper
@execution
def hello():
    print("Hello World")
hello()



  





