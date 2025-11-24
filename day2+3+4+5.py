# # type = 10
# # print(type)
# # Every variable in python is an identifier but not every identifier is a variable.
# # An identifier is a name used to identify a variable, function, class, module or other object

# # a,b,c,d,e = 5,10.5,"Hello",True,3+4j
# # print(c+"#$b+#$c+#$d+#$e",a,b,d,e)

# # for = 10
# # print(for)

# # _ = 10
# # print(type(_))

# booool = True
# print(type(booool))
# # integer = 10
# # print(type(integer))
# # floating = 10.5
# # print(type(floating))
# # complexnum = 3 + 4j
# # print(type(complexnum))

# # list1 = [1, 2, 3, 4, 5]
# # print(list1.index(2))
# # print(len(list1))
# # print(type(list1))
# # tuple1 = (1,)
# # print(type(tuple1)) 
# # print(len(tuple1))
# # print(tuple1)
# # dict1 = {"name": "John", "age": 30}
# # print(len(dict1))
# # print(type(dict1))
# # set1 = {1, 2, 3, 4, 5}
# # print(len(set1))
# # print(type(set1))
# # string = "Hello"
# # print(len(string))
# # print(type(string))

# # a = list1.index(1)
# # print(a)


# # list works as a dynamic array in python
# # there is no indexing in a set
# # tuple is immutable
# # dict is a key value 


# # print(list1[0::2])  #slicing

# # print(list1[::-1])  #reversing a list
# # add operation works on in place insertion
# # append concatenation extend and insert are used at inplace insertion
# # extend operation returns NONE

# # list1.append(6)
# # print(list1)
# # list1.remove(3)
# # print(list1)
# # list1.pop()
# # print(list1)
# # list1.insert(2, 10)
# # print(list1)
# # list1[0] = 100
# # print(list1)
# # list1.sort()
# # print(list1)
# # list1.reverse()
# # print(list1)
# # list1.extend([7, 8, 9])
# # print(list1)
# # list1.clear()
# # print(list1)
# # del list1

# # list1 = [1, 2, 3, 4, 5, 2]
# # print(list1)
# # print(min(list1))
# # print(max(list1))
# # print(sum(list1))
# # print(list1.count(2))
# # print(list1.index(4))
# # list1.extend([7,8,9])
# # print(list1)
# # copylist = list1.copy()
# # print(copylist)
# # print(type(copylist))
# # print(len(copylist))
# # list1.sort(reverse=True)
# # print(list1)
# # list1.sort()
# # print(list1)
# # list1 *= 2
# # print(list1)
# # list1 += [7,8,9]
# # print(list1)
# # list1 *= 3
# # print(list1)


# # #delete functions 
# # list1.pop()         #last value in a list
# # print(list1)
# # list1.remove(2)     #specified value in a list
# # print(list1)
# # list1.pop(0)        #remove element at index 0
# # print(list1)
# # # del list[list1.index(4)]   #remove element with value 4
# # list1.clear()
# # print(list1)


# #utility functions
# # list1 = [5,3,8,6,2,7,4,1]
# # print(list1.sort(reverse=True))      #returns None
# # print(list1)
# # print(list1.reverse())   #returns None
# # print(list1)

# # del list1[0]
# # print(list1)
# # del list1[2:5]
# # print(list1)
# # del list1
# # print(list1)

# #operation on a dictionary
# dict1 = {"name": "John", "age": 30, "city": "New York"}
# # print(dict1)
# # #add operation
# # dict1["country"] = "USA"
# # print(dict1)
# # #update operation
# # dict1["age"] = 31
# # print(dict1)
# # dict1.update({"city": "Los Angeles"})
# # print(dict1)
# # #delete operation
# # del dict1["country"]
# # print(dict1)
# # print(dict1.pop("age"))        #returns the value of the key being removed
# # print(dict1)
# # dict1.popitem()        #removes and returns the last inserted key-value pair
# # print(dict1)

# #view operation
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())