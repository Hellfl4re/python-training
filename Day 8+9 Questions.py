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
# n = range(int(inpint(input("Enter end of range: "))+1)
# name = ""
# for i in n:
#     i = str(i)
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

a = [1,2,3,4,5]
for i in a:
    print(i)
    for j in a:
        print(j)