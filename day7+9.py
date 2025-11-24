"""Operators"""
#assignment operators
# = += -= *= /= %= //= **=
# assign add and assign subtract and assign multiply and assign divide and assign modulus and assign floor divide

#arithmetic operators
# + - * / % // **
# add subtract multiply divide modulus floor division exponentiation

#membership operators
# 'in' & 'not in'           returns True or False

#idnetity operators
# 'is' & 'is not'           returns True or False

#comparison operators
# == != > < >= <=
# equal not equal greater than less than greater than or equal to less than or equal to

#logical operators
# and or not
# logical AND logical OR logical NOT

# a = 10
# b = 10
# c = 10

# print(id(a), id(b), id(c))
# if a is b and b is c: then they point to same memory location

"""input and output statements"""
# input() : by default takes string values 
#           the values entered by user can be typecasted to required data type
# print() : used to display output on console
#           by default adds a new line after every print statement
# eval()   : used to evaluate a string as a python expression
#            can be used to take multiple inputs from user in a single line

"""flow control statements:   it is a statement that determines the order in which other statements are executed in a program
                           they allow us to make decisions and repeat certain blocks of code based on conditions"""
# if elif else
# for while
# break continue pass
# try except finally
# def return yield

"""conditional statements: used for decision making"""
# if        checks the condition true or not
#           only runs if the result is true
#           if condition is false the next code is skipped
# elif      elif checks another condition if the previous if condition is false
#           used when there are multiple conditions to check
# else      when the condition in if is false then else block is executed
#           else does not have any condition

# o = int(input("Enter a number: "))
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
# if o in list1:
#     print("the number is present in list")
# elif o % 10 == 0:
#     print("the number is a multiple of 10")
# else:
#     print("the number is absent from list and it is odd")

"""looping statements: used to execute a block of code repeatedly until a certain condition is met"""
#While loop: runs the loop until the condition provided is true
#For loop: used to iterate over a sequence

# set1 = {10, 20, 30, 40, 50}
# # for i in set1:
# #     print(i)

# while True:
#     print(set1)
