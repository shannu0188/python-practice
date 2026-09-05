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

# age = int(input("enter your age:  "))
# if age >= 18:
#    print("you are go to next cheking process")

#    has_id = input("do u have an id card (yes/no):  ")
#    if has_id == "yes":
#         print("you can go to office")
#    else:
#       print("you are not allowed")

# else:
#    print("you are under age")

# age = 18
# has_id = True
# if age >= 18 and has_id:
#     print("u can go")


#login
# username = input("Enter your username: ")

# if not username:
#     print("Username can't be empty")

# elif username == "admin":
#     print("Unknown user")

# else:
#     password = input("Enter your password: ")

#     if not password:
#         print("Password can't be empty")
#     else:
#         print("Login successful")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if not username:
#     print("Username can't be empty")
# elif not password:
#     print("Password can't be empty")
# elif username != "admin":
#     print("Unknown user")
# elif password != "password123":
#     print("Incorrect password")
# else:
#     print("Login successful")

# ATM withdrawal

# balance = 1000
# pin = input("Enter your PIN: ")
# if pin != "1234":
#     print("Incorrect PIN")
# else:
#     amount = float(input("Enter the amount to withdraw: "))
#     if amount <= 0:
#         print("Invalid amount")
#     elif amount > balance:
#         print("Insufficient funds")
#     else:
#         balance -= amount
#         print(f"Withdrawal successful. New balance: {balance:.2f}")




# age = 18
# if age >= 18:
#     pass
# else:
#     print("You are underage")


# name = input("Enter your name: ")
# name = "shannu"
# from os import name

# name = "shannu"
# if name:
#     print(f"Hello {name}")

# if name != "shannu":
#     print(f"Hello {name}")
# else:
#     print("sorry shannu")

# turnary operator
# age =25
# status = "adult" if age >=18 else "minor" 
# print(status)

# x = int(input("enter no:  "))
# result = "even" if x % 2 == 0 else "odd"
# print(result)


#while loop
# count = 0
# while count <5:
#     print(count)
#     count += 1

# match(switch case)
# command = input("enter the command:  ")

# match command:
#     case "start":
#         print("starting....")
#     case "stop":
#         print("stoping...")
#     case "restart":
#         print("restarting...")
#     case _:
#         print("unknown command")


# day = input("Enter day: ")

# match day:
#     case "sunday" | "saturday":
#         print("weekend")

#     case "monday" | "tuesday" | "thursday":
#         print("week days")

# age = int(input("enter your age:  "))
# match age:
#     case n if n < 18:
#         print("under age")
#     case n if n >= 18:
#         print("adult")


#while loop

# count = 0
# while count <=5:
#     print(count)
#     count += 1
# print("done")

# i = 0
# while i < 5:
#     print(i)
#     i +=1

# for i in range(5):
#     print(i)

# user_input = input("command:  ")

# while user_input != "quit":
#     print (f"processing: {user_input}")
#     user_input = input("command: ")

# while True:
#     command = input(" Enter the command (quit or exit): ").strip().lower()
#     if command =="quit":
#         print("Good bye!")
#         break
#     print(f"you are enterd: {command}")

count = 0
# while count < 100:
#     if count == 5:
#         print(" Reached 5 stopping erly")
#         break
#     print(count)
#     count +=1

# count = 0
# while count < 15:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count)

# count = 0
# while count <10:
#     count +=1
#     if count %2 == 0:
#         continue
#     print(count)

# while True:
#     user_input = input("enter a number:  (or 'done' to finish):  ").lower().strip()
#     if user_input.lower() == "done":
#         break
     
#     if not user_input.isdigit():
#         print("enter a vaild number")
#         continue


#     number = int(user_input)
#     print(number)
# print("png finsh")

# target = 120
# guess = 0
# while guess < 5:
#     attempt = int(input("gess the number:  "))
#     guess +=1
#     if attempt == target:
#         print("ur right")
#         break

# else:
#     print("ur out of attempt")

# using for loop
# for i in range(5):
#     print(i)

# for i in iter(int, 1):
#     line = (input("enter somthing (done or quit): "))
#     if line == "quit":
#         print(f"ur are entred:  {line}")
#         break

# for i in range(0, 15, 2):
#     print(i)

# for i in range(15, 0, -1):
#     print(i)

# for char in ("python"):
#     print(char)

# text = "python"
# for i in range(len(text)):
#     print(i, text[i])

# text = input("Enter a sentence: ")

# vowel_count = 0
# consonant_count = 0

# for char in text.lower():
#     if char in "aeiou":
#         vowel_count += 1
#     elif char.isalpha():
#         consonant_count += 1

# print(f"Vowels: {vowel_count}")
# print(f"Consonants: {consonant_count}")

# count = 0
# for i in range(10):
#     if i == 5:
#         print("found 5 ")
#         break
#     print(i)


# for i in range(10):
#     if i % 3 == 0:
#         continue
#     print(i)

# target ="p"
# text = "python"

# for char in text:
#     if char == target:
#         print(f"found {target} in {text}")
#         break

# else:
#     print(f" {target} not found {text}")

# for i in range(1, 4):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j} ")
#     print("="  * 10)


# for i in range(1, 10):
#     print("*" * i)

# today we can practice list data types(03/09/2026)

# name = ["shannu", "kaveri", "paapu"]
# vegitables = ["tomoto", "onion", "patato"]
# D_mart =["rice", "dal", "sugar"]
# mixed = [143, "muddumma", 143.2, True]
# print(name)
# print(vegitables)
# print(D_mart)
# print(mixed)


# D_mart =["rice", "dal", "sugar"]
# for item in D_mart:
#     print(item)
# print(len(D_mart))

# aisle_num = list(range(1, 6))
# print(aisle_num)
# empty = []
# print(empty)
# d_mart = list("DMART")
# print(d_mart)

# vegitables = ["tomoto", "onion", "patato", "carrot", "beens"]
# first = vegitables[0]
# second = vegitables[1]
# last = vegitables[-1]
# second_last = vegitables[-2]
# print(f"this is the indexing \n {first}\n {second}\n {last}\n {second_last}")


# price = [10, 20, 30, 70, 80, 50]
# first = price[0:3]
# mid_range = price[2:5]
# avg = price[:5]
# mid_avg = price[::-2]

# print(f"slicing \n {first} \n {mid_range} \n {avg} \n {mid_avg} \n")

# list is mutable how to see 
# veg = ["tomoto", "onion", "patato", "carrot", "beens"]
# first = veg[2]
# print(first)
# veg[2] = "cabbage"

# print (veg)

#  share cart 
# my_cart = ["rice", "dal", "sugar"]
# wife_cart = my_cart
# wife_cart.append("solt")
# my_cart.append("ghee")
# print(my_cart)
# print(wife_cart)

# me and my friend cart
# my_cart = ["rice", "dal", "sugar"]
# frd_cart = my_cart.copy()
# frd_cart.append("apple")
# print(f"this is my cart = {my_cart} ")
# print(f"My friend cart ={frd_cart}")


# cart = ["rice", "dal", "ghee", "apple"]
# print(cart)
# cart.insert(0, "sugar")
# print(cart)

# cart.pop()
# print(cart)

# cart.remove("rice")
# print(cart)

# my_cart = ["rice", "dal", "ghee", "apple"]
# for cart in my_cart:
#     print(cart)
# print(my_cart)

# my_cart = ["rice", "dal", "ghee", "apple"]

# has = "dal" in my_cart
# print(has)

# has2 = "solt" in my_cart
# print(has2)

# has3 = "solt" not in my_cart
# print(has3)

# prices =[]
# for i  in range(3):
#     p =int(input(f"price {i+1}:  ₹ "))
#     print(prices)
#     prices.append(p)
# total = sum(prices)
# avg = total / len(prices)

# print(f"total : {total}")
# print(f"avg : {avg}")
# print(f"in the price list {prices}")

# cart = [
#     ["dal", "rice", "bele"],
#     ["oil", "ghee", "butter"],
#     ["soap", "shampoo","diterjent"],
# ]
# print (cart[0][2])
# print (cart[1][1])
# print (cart[2][1])

my_cart = ["rice", "dal", "ghee", "apple"]    
letters = list("Dmart")
alise = list(range(1, 10))
print(letters)
print(alise)
