 #Q1
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# print(a, "First Number")
# print(b, "Second Number")
# a,b = b,a
# print(a, "First Number after")
# print(b, "Second Number after")



# #Q2
# inp = int(input("Input total Seconds "))
# if inp<60:
#     print("Minutes = 0")
# else:
#     minutes = inp // 60
#     seconds = inp % 60
#     print(minutes, "min", seconds, "sec")
# if minutes>=60:
#     hours = minutes // 60
#     minutes = minutes % 60
#     print(hours, "hrs", minutes, "min", seconds, "sec") 
# else:
#     print("hrs = 0")

#Q3
# num = int(input("Enter a number "))
# num = str(num)
# lastdigit = num[-1]
# if int(lastdigit) % 3 == 0:
#     print("Last digit is divisible by 3")
# else:
#     print("Last digit is not divisible by 3")

#Q4
# char = str(input("Enter a character "))
# if len(char) != 1:
#     print("Invalid Input")
# elif char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#     print("Vowel")
# else:
#     print("Consonant")

# #Q5
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# op = int(input("""Select a value for required operator:
#                1: +
#                2: -
#                3: *
#                4:/
#                """))
# if op == 1:
#     print("Sum = ", a+b)
# elif op ==2:
#     print("Difference = ", a-b)
# elif op ==3:
#     print("Product = ", a*b)
# elif op ==4:
#     if b == 0:
#         print("Undefined")
#     else:
#         print("Quotient = ", a/b)
# else:
#     print("Invalid Operation")


#Q6
# units = int(input("Units of electricity consumed: "))
# cost = 0
# if units<=100:
#     print("The Electricity bill is $0")
# elif units<=200:
#     units-=100
#     print("Electricity bill is $", units*5)
# elif units>200:
#     cost = 500 + (units - 200)*10
#     print("Electricity bill is $", cost)
# else:
#     print("Invalid amount of units entered")


# #Q7
# salary = int(input("Employee's salary "))
# years = int(input("Years of service "))
# if years > 10:
#     salary = salary+salary*0.1
# if years > 5 and years< 10:
#     salary = salary+salary*0.05
# if salary > 50000:
#     salary = salary - salary*0.1
#     print("In hand salary =", salary)
# else:
#     print("In hand salary =", salary)

"""Date 24-11-2025"""
#Q1
# name = str(input("Enter Your Name: "))
# age = int(input("Enter Your Age: "))
# print("Name: ", name)
# print("Age: ", age)

# #Q2
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# print("Sum: ", a+b, "\n" "Difference: ", a-b, "\n" "Product: ", a*b, "\n" "Quotient: ", a/b)

#Q3
# a = int(input("Enter a number "))
# if a % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

#Q4
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# c = int(input("Enter third number "))
# if a >= b and a >= c:
#     print(a, "is the largest number")
# elif b >= a and b >= c:
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")

#Q5
# maths = int(input("Enter marks in Mathematics "))
# science = int(input("Enter marks in Science "))
# english = int(input("Enter marks in English "))
# sst = int(input("Enter marks in Social Studies "))
# hindi = int(input("Enter marks in Hindi "))
# total = maths + science + english + sst + hindi
# average = total / 5
# print("Total Marks: ", total)
# print("Average Marks: ", average)

# if average >= 90:
#     print("Grade: A")
# elif average >= 80:
#     print("Grade: B")
# elif average >= 70:
#     print("Grade: C")
# else:
#     print("Grade: Fail")

#Q6
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# op = int(input("""Select a value for required operator:
#                1: +
#                2: -
#                3: *
#                4:/
#                """))
# if op == 1:
#     print("Sum = ", a+b)
# elif op ==2:
#     print("Difference = ", a-b)
# elif op ==3:
#     print("Product = ", a*b)
# elif op ==4:
#     if b == 0:
#         print("Undefined")
#     else:
#         print("Quotient = ", a/b)
# else:
#     print("Invalid Operation")

#Q7
# n = int(input("Enter the range to be summed up to: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum of numbers from 1 to", n, "is:", sum)

#Q8
# n = int(input("Enter a number to print its multiplication table: "))
# print("Multiplication table for", n)
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

#Q9
# ranged = range(int(input("Enter start of range: ")), int(input("Enter end of range: "))+1)
# even = 0
# odd = 0
# for i in ranged:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Number of even numbers:", even)
# print("Number of odd numbers:", odd)

#Q10
# n = range(1, int(input("Enter end of range: "))+1)
# name = ""
# for i in n:
#     i = str(i)+" "
#     name += i
#     i = int(i)
#     i += 1
#     print(name)

# #Special question
# a = int(input("Enter start of range: "))
# b = int(input("Enter end of range: "))
# list1 = []
# listeven = []
# listodd = []
# while a <= b:
#     list1.append(a)
#     a = a + 1
# for a in list1:
#     while a % 2 == 0:
#         listeven.append(a)
#         break
#     while a % 2 != 0:
#         listodd.append(a)
#         break
# print("Even numbers in the range are:", listeven, "Length =", len(listeven))
# print("Odd numbers in the range are:", listodd, "Length =", len(listodd))

# a = [1,2,3,4,5]
# for i in a:
#     print(i)
#     for j in a:
#         print(j)

"""Date 25-11-2025"""

# #Q1
# a = str(input("Enter a number "))
# for i in a:
#     b = i
#     for j in reversed(a):
#         c = j
# if b == c:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#Q2
# a = input()
# i = 0
# list1 = []
# while i in range(101):
#     list1.append(i)
#     i += 1
#     list1 = sorted(list1, reverse=True)
# print(list1)

#Q3
# x = {'a': 34, 'b': 32, 'c': 39}
# listkeys = []
# listvalues = []
# for i in x:
#     listkeys.append(i)
#     listvalues.append(x[i])

# print("Keys:", listkeys)
# print("Values:", listvalues)

#Q4
# list1 = [1, 2, 3 ,4, 3,3 ,4, 5]
# for i in list1:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     print(i, "appears", count, "times")

#Q5
# name = "*"
# space = " "
# repeat = 3
# for i in range(1, 5):
#     print(space*repeat+name+space*repeat)
#     name += "**"
#     repeat -= 1

#Q6
# a = "taramasalata"
# b = 0
# c = "a"
# for i in a:
#     if i == 'a':
#         b += 1
# print("count of a =", b)    

#Q7
# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0:
#         return False
#     limit = int(n**0.5) + 1
#     for i in range(3, limit, 2):
#         if n % i == 0:
#             return False
#     return True

# primes = [n for n in range(1, 51) if is_prime(n)]
# print("Prime numbers between 1 and 50:", primes)

"""26-11-2025"""
#Q1
# ranged = range(1, 101)
# for i in ranged:
#     if i%3==0 and i%5!=0:
#         print("Fizz")
#     elif i%3!=0 and i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     else:
#         print(i)

#Q2
# numbers = [1,5,22,9,14,3,4,88,7]
# evens = []
# odds = []
# for i in numbers:
#     if i%2==0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print("Evens:", evens, "\nOdds:", odds)

# #Q3
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# punctuation = ['.',',']
# user = str(input("Enter the Phrase/Sentence: "))
# vowel_count = 0
# consonant_count = 0
# for i in user:
#     if i in vowels:
#         vowel_count += 1
#     elif i not in vowels and i!=" " and i not in punctuation:
#         consonant_count += 1
#     else:
#         continue
# print("Total Vowels =", vowel_count)
# print("Total Consonants =", consonant_count)

#Q4
# secret_number = 67
# a = 0
# while a!=secret_number:
#     a = int(input("Enter your guess: "))
#     if a>secret_number:
#         print("Too High! Try Again")
#     elif a<secret_number:
#         print("Too Low! Try Again")
#     else:
#         print("")
# print("Correct!")


# #Q5
# prime=[]
# for num in range(2,51):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         prime.append(num)
# print("Prime numbers between 1 and 50 are:", prime)

#misc
# num = int(input("Enter number of rows: "))
# i = 0
# while i < num:
#     i += 1
#     print(" "* (num-i) + "*" * (2*i-1))

"""27-11-2025"""

#Q1
# length = int(input("Enter length of the rectangle: "))
# breadth = int(input("Enter breadth of the rectangle: "))
# perimeter = 2*(length + breadth)
# area = length * breadth
# print("Perimeter of the rectangle is:", perimeter)
# print("Area of the rectangle is:", area)

#Q2
# num = int(input("Enter a number: "))
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd number")

#Q3
# list1 = [12, 45, 23, 67, 34, 89, 90]
# some = 0
# for i in list1:
#     some += i
# print("Sum of all numbers in the list is:", some)

#Q4
# list1 = [34, 67, 23, 89, 2, 45, 90]
# tumble = []
# list1 = sorted(list1)
# tumble.append(list1[0])
# tumble.append(list1[-1])
# print(tuple(tumble))

#Q5
# name = str(input("Tell me your name user: "))
# if name == "":
#     name = "Guest"
# print("Greetings,", name+"!")