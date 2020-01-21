# 1. Tip Calculator

# bill_amount = float(input('The Total Bill Amount:$'))
# level_of_service = (input('Level Of Service : good, fair , bad'))
# tip_amount = float()

# if (level_of_service == 'good'):
#     tip_amount = bill_amount * .2
#     print('Tip Amount : $' ,"%.2f" %tip_amount)
# elif( level_of_service =='fair'):
#     tip_amount = bill_amount * .15
#     print('Tip Amount : $', "%.2f" %tip_amount)
# elif(level_of_service == 'bad'):
#     tip_amount = bill_amount *.10
#     print('Tip Amount : $' ,"%.2f" %tip_amount)
# else:
#     print('')
# total_amount = float(bill_amount + tip_amount)
# print('Total Amount: $' , "%.2f" %  total_amount)

# 2. Tip Calculator

# bill_amount = float(input('The Total Bill Amount:$'))
# level_of_service = input('Level Of Service : good, fair , bad')
# split = int(input('Split how many ways'))
# tip_amount = float()

# if (level_of_service == 'good'):
#     tip_amount = bill_amount * .2
#     print('Tip Amount : $' ,"%.2f" %tip_amount)
# elif( level_of_service =='fair'):
#     tip_amount = bill_amount * .15
#     print('Tip Amount : $', "%.2f" %tip_amount)
# elif(level_of_service == 'bad'):
#     tip_amount = bill_amount *.10
#     print('Tip Amount : $' ,"%.2f" %tip_amount)
# else:
#     print('')
# total_amount = float(bill_amount + tip_amount)
# per_person = float(total_amount/split)
# print('Total Amount: $' , "%.2f" %  total_amount)
# print('Amount per person: '"%.2f" % per_person)







# 3. How many coins?

# coins = 0
# question1 = "yes"
# while question1 == "yes":
#     first_total = (f'You have {coins} coins ')
#     print(first_total)
#     question1 = input('Do you want another?')
#     if (question1 == 'yes'):
#         coins +=1

# print("END")


#  4
# height = int(input("What is the height?"))
# width = int(input("What is the width?"))
# print("*" * width)
# for i in range(height - 2):
#     print("*" + " " * (width - 2) + "*")
# print("*" * width)   



# 5. Print a Triangle
# n = 1
# m = 10
# while m> 0:
#     print(''* m + '*' * n)
#     m -= 1
#     n +=2


# 6.Multiplication Table

# for num1 in range(1,11):
#     for num2 in range(1,11):
#         print(num1,"X",num2,"=",num1 * num2)



a = [2,4,5]
b = [2,3,4]
ab =[]

for i in range(len(a)):
    ab.append(a[i]*b[i])

print(ab)
