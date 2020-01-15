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


for num1 in range(1,11):
    for num2 in range(1,11):
        print(num1,"X",num2,"=",num1 * num2)