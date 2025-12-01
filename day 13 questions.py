"""28-11-2025"""
# # Q1
# some = 0
# mix_list = [10,-5,20,-10,30,-2]
# for i in mix_list:
#     if i > 0:
#         some += i
# print("Total =",some)

# # Q2
# sentence = str(input("Enter a sentence: \n"))
# vowelcount = 0
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# for i in sentence:
#     if i in vowels:
#         vowelcount +=1
# print("Total vowels =",vowelcount)

# # Q3
# items = ["Python","Java","C++","Go"]
# reversed_list = []
# for i in items:
#     while len(items) > 0:
#         reversed_list.append(items[-1])
#         items.pop(-1)
# print(reversed_list)

# # Q4
# star = '*'
# for i in range(2,6):
#     print(star*(i))

# # Q5
# raw_data = [1,2,2,3,4,4,4,5]
# raw_data = set(raw_data)
# raw_data = list(raw_data)
# raw_data.sort()
# print("Second largest number from the list: ", raw_data[-2])

# # Q6
# currency = {"USD": "Dollar", "EUR":"Euro", "INR": "Rupee"}
# currencykeys = []
# currencyvalues = []
# for i in currency.keys():
#     currencykeys.append(i)
# for i in currency.values():
#     currencyvalues.append(i)
# reverseddict = {}
# index = 0
# for index in range(len(currencykeys)):
#     reverseddict[currencyvalues[index]] = currencykeys[index]
#     index += 1
# print(reverseddict)

# # Q7
# teams = ["red","blue","green"]
# teamss = {}
# for i in teams:
#     teamss[i] = teams.index(i)+1
# print(teamss)

# # Q8
# words = ["apple", "banana", "apricot", "cherry", "blueberry"]
# alphas = "abcdefghijklmnopqrstuvwxyz"
# dictionary = {}
# for i in alphas:
#     lis = []
#     for j in words:
#         if j[0] == i:
#           lis.append(j)
#           dictionary[i] = lis
# print(dictionary)

# # Q9
# matrix = [[1,2],[3,4],[5,6]]
# transpose1 = []
# transpose2 = []
# index = 0
# for i in matrix:
#     i = list(i)
#     transpose1.append(i[index])
#     transpose2.append(i[index+1])
# transpose = [transpose1,transpose2]
# print(transpose)

# # Q10
# warehouse1 = {"apple": 10, "banana": 20}
# warehouse2 = {"banana": 30, "Orange": 5}
# for i in warehouse2.keys():
#     if i in warehouse1.keys():
#         warehouse1[i] = warehouse1[i] + warehouse2[i]
#     else:
#         warehouse1[i] = warehouse2[i]
# print(warehouse1)