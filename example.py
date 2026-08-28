# a = 20
# b = 3

# print(f"{a} dividedd by {b} is {a / b}")

# print("Welcome to the tax calculator")
# price = float(input("Enter the price: "))
# tax = float(input("enter the tax:  "))
# total = price * tax

# print(f"price: {price:.2f}")
# print(f"tax: {tax:.2f}")
# print(f"total: {total:.2f}")    


# name = "shanmukha"
# score = 100

# print(f"{'name':<15}: {name:>15}")
# print(f"{'score':<15}: {score:>15}")
# print(f"{'Status':<15}: {'Active':>15}")

# first = "one\t"
# last = "two\t"

# full = first + last
# print(full *10)


# import string

# print("enter your age")
# age =string(input("your age : "))

# print(age)

# age = 25
# print("age: " + str(25))

# print("ha" *50)

# case converssion method

#text = "shanmukha is belive our ownself"
# print(text)
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

#taken username from the user, upper case or lower case can we convert in the backend
# username = input("Enter your name:  ")
# username = username.strip()
# username = username.lower()
# print(username)
# username = username.upper()
# username = username.strip()
# print(username)
# print(len(username))

# if else how its work 

# if "Hello":
#     print("good")
# if None:
#    print("never")
# if [1, 2, 3]:
#      print("has items")

#simple example for voting method    
# text = str(input("hii what is your name:   "))

# age = int(input("Enter your age: "))

# if age >= 18:
#     print(text, "u can vote")
# else:
#     print(text, "sorry u r under age")

#binary to decimal conversion
# print(bin(-1))

# print(ord("A"))
# print(bin((ord("A"))))
# print(round(0.1 + 0.2, 10))

# a = 10
# b = "shanmukha"
# c = 0.1

# print(type(a))
# print(type(b))
# print(type(c))

# big = 10 * 100
# print(big)
# print(type(big))
# population = 80_000_000_0
# print(population)

# price =99.99
# temp = -3.5
# print(type(price))

# p = 0.1 + 0.2 

# print(round(p, 16))

# print(10 / 3)
# print(10 // 3)
# print(10 % 8)

# print(-7 / 2)

#logical operators(using and, or, not)

# age = 25
# has_id = False

# print(age >=18 and has_id)
# print(age >=18 )
# print(age >=26 or age >=26 and has_id)
# print(age >=18 and not has_id)

# print(bool(input("Enter your name:   ") or input("Enter your name:   ")))

# print(bool({}))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool(None))
# print(bool(""))
# print(bool(0)) 
# print(bool(0.0))    
# print(bool(0j)) 
# print(bool(False))
# print(bool(range(0)))

# name = input("Enter your name:  ")
# getting = name or "anonymous"
# print(f"Hello {getting}")

# name = input("Enter your name:  ")
# age = int(input("Enter your age:  "))
# name1 = input("Enter your name:  ")

# print(f"i am {name} and i love you soo {name1} and my age is {age}")

# result = "yes"
# yes = "NO"
# print(type(result))
# print(bool(result))
# print(result is yes)

# print("p" in "python")
# print("java" in "python")
# print("p" not in "python")
# print("java" not in "python")

# print( (3 + 5) * 3)
# print( 10 == 10)
# print( 5 != 10)
# print( 10 > 10)
# print( 10 < 10) 
# print( 10 >= 10)
# print( 10 <= 10)

# print(10 == 10)
# print("shannu" is "alita")

# if False:
#     print("i am good")
#     print("i am fine")
# print("i am not good")

# result calculator
# score = int(input("Enter your score:  "))

# if score >= 90:
#     print(f"your score is {score} and your grade is A")
# elif score >= 80:
#     print(f"your score is {score} and your grade is B")
# elif score >= 70:
#     print(f"your score is {score} and your grade is C")
# elif score >= 60:
#     print(f"your score is {score} and your grade is D") 
# else:
#     print(f"your score is : {score} , you are fail")

#nested if condition

age = int(input("enter your age:  "))
if age >= 18:
    print("you are go to next cheking process")

    has_id = input("do u have an id card (yes/no):  ")
    if has_id == "yes":
        print("you can go to office")
    else:
        print("you are not allowed")
else:
    print("you are under age")



        
