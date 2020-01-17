# 3. day =>> 01/15/2020
# number = [1,2,3,4,5]
# print(number[1])

# num1 = [1,2]
# number = [num1,2,3,4,5]
# print(number[0])


# a = [1,4,7,9,10]
# b = [4,6,8,9]
# print( a+b) 



# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.extend(["binge watch a show", "go to sleep"])


# print(todos)
# menu = [ 'biryani' ,'kabab', 'naan' , 'chicken',]
# choose_menu = input("What would like to eat? ")
# menu.extend(['icecream'])
# print (menu)
# count = 0
# while count < len(menu):
#     print(count)
#     count += 1
#     print (menu)

# menu = [ ]
# choose_menu = input("What would like to eat? ")
# while len(choose_menu) >0:
#     menu.append([choose_menu])
#     print(menu)
#     choose_menu = input("What would like to eat? ")
# print(menu)

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(3, 6)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]

# while (len(numbers)>0):
#     print(numbers.pop())
#     print(numbers)
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# alp2 = list(alphabet)

# print(type(alp2))


# for index in range(1,1001,2):
#     print(index)


# for num1 in range(1,11):
#     for num2 in range(1,11):
#         print(num1,"X",num2,"=",num1 * num2)

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.append("binge watch a show")
# todos.append("go to sleep")
# count = 0
# while count < len(todos):
#     print(f"{count}: {todos[count]}")
#     count += 1

# x = [[2,6],[6,2],[8,2],[5,12]]
# print(x[2])
# print(x[2][1])

# a = [ [2, 4, 6, 8 ],  
#     [ 1, 3, 5, 7 ],  
#     [ 8, 6, 4, 2 ],  
#     [ 7, 5, 3, 1 ] ]  
# i = 0
# j = 0
# while i < len(a) :  
#     while j < len(a[i]) :  
#         print(f"{a[i][j]}", end=" ")
#         j += 1 
#     print()
#     j = 0
#     i+= 1


# for i in range(len(a)):
#     for j in range(len(a[i])):
        
#         print(f'{a[i][j]}', end= '')
#         j +=1

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# # index = 0
# # while index < len(alphabet):
# #     print(alphabet[index])
# #     index += 1

# for index in range(len(alphabet)):
#     print(alphabet[index])

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphalist = list(alphabet)

# print(type(alphalist))

# alphabet = ".".join(alphalist)

# print(type(alphabet))
# print(alphabet)


# for outter_variable in range(3):
#     for innner_variable in range(3):
#         print(outter_variable)
#         print(outter_variable , innner_variable)


# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i}*{j}')



# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# subj = ['Object','HW','Training']
# for w in range(1,17):
    
#     print (f'Week : {w}')
    
#     for d in days:
#         print(f'\t{d}')
#         for lesson in subj:
#             print(f'\t\t-{lesson}')


# mount = ['jan','feb','march','april','may','jun']
# days = ['mon','tue','wed','thu','fri','satur','sun']
# for year in range(1,11):
#     print(f'Year : {year}')
#     for moun in mount:
#         print(f'\t. {moun}')
#         for week in range(1,5):
#             print(f'Week : {week}')
#             for day in days:
#                 print(f'\t\t*{day}')

# def print_student():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")




# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_student()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_student()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_student()


# def greeting(person):
#     print(f'Welcome {person}')
# greeting('Meryem')


# my_numbers = [7, 9, 90]
# my_numbers_2 = [75, 33, 6, 9]

# def avg_my_list(my_list):
#     avg = sum(my_list)/len(my_list)
#     return avg

# print(avg_my_list(my_numbers))
# print(avg_my_list(my_numbers_2))

# my_tuple = (3,4,5,6)
# v1 ,v2, v3, v4 = my_tuple
# print(v1)

# contact = [{
#     'first_name': 'Meryem',
#     'last_name': 'Komur',
#     'phone':{
#         'cell':'333-333-3333',
#         'home':'444-444-4444',
#     }
# },
# {
#     'first_name': 'John',
#     'last_name': 'Kearney'
# },
# {   'first_name': 'Sean',
#     'last_name': 'Page'

# }]

# print(contact[0])
# print(contact[1])
# print(contact[1]['last_name'],contact[2]['first_name'])
# print(contact[0]['phone']['cell'])
contact = [
    {
        'first_name': 'Phillip',
        'last_name': 'Guo',
        'email': 'phillip.guo@gmail.com',
        'phone':{
            'work':'837-494-3948',
            'cell': '234-897-4933'
        }
    },
    {
        'first_name': 'Mark',
        'last_name': 'Guzdial',
        'email': 'mark.guzdial@gatech.edu',
        'phone':{
            'work':'484-569-3466',
            'cell': '493-485-9845'
        }
    }
]

print(contact[1]['phone']['work'])