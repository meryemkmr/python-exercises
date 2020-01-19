# phonebook = {
#     'Meryem': '888-888-8888',
#     'Kazim': '111-111-1111',
#     'Foorkan': '222-222-2222',
#     'John': '999-999-9999'
# }
# my_value = 0
# while my_value != 5:
#     print()
#     print ( "Electronic Phone Book")
#     print ("=======================")
#     print ("1. Look up an entry ")
#     print ("2. Set an entry")
#     print ("3. Delete an entry")
#     print ("4. List all entries")
#     print("5. Quit")
#     print ()
#     my_val = int(input('What do you want to do? (1-5)? '))
#     print()
#     if my_value == 1:
#         name = input('Name :')
#         if name in phonebook:
#             print(f'Found entry for {name} :', phonebook[name])
#         else:
#             print('Sorry not found')
#     elif my_value == 2:

#         name = input ('Name: ')
#         phone = input ('Phone Number: ')
#         phonebook[name] = phone
#         print (f'Entry stored for {name}')
#     elif my_val == 3:
#         delete = input('Name: ')
#         phonebook.pop(delete)
#         print(f'Deleted entree for {delete}')
    
#     elif my_val == 4:
#         for x in phonebook.keys():
#             print("Found entree for ", x,": " , phonebook[x] )

#     elif my_val != 5:
#         print ( "Electronic Phone Book")
#         print ("=======================")
#         print ("1. Look up an entry ")
#         print ("2. Set an entry")
#         print ("3. Delete an entry")
#         print ("4. List all entries")
#         print("5. Quit")
# print('Bye.')


phoneBook = {"key" : "281-701-8297" }
def electric_PhoneBk (phone_Book):
    while True:
        print("Electronic phone book")
        print((input("1. Look up an entry" + "\n\n" + "2. Set an entry " + "\n\n" + "3. Delete an entry" + "\n\n" + "4. List all entries" + "\n\n" + "5. Quit")))
        ask = int(input("What do you want to do (1-5)? "))
        print(ask)
    # For loop requires the size of the dictionary. Hence you cant use it here since you are adding to the phonebook
        if (ask == 1):
            key_word = input("Enter the key ")
            look_up = phone_Book[key_word]
            print(look_up)
        elif (ask == 2):
            the_name = input("Enter a name ")
            the_number = input("Enter Phone Number ")
            phone_Book[the_name] = the_number
            print(phone_Book)
        elif (ask == 3):
            key_word = input("Enter the key ")
            del phone_Book[key_word]
            print(phone_Book)
        elif (ask == 4):
            contents = phone_Book.items()
            print(contents)
        elif (ask == 5):
            exit()
print(electric_PhoneBk(phoneBook))
