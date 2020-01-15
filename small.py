# name = input('What is your name?')  # small number 1

# output = f'hello , {name} '
# print(output)

# name = input ('what is your name?')
# message = f' Hello {name}! \n Your Name Has 6 Letter In It! Awesome!'
# print(message.upper()) # hello you!

# name =input("What is your name?")
# subject = input("What is subject")
# msg = f"{name}'s favorite subject in scholl is {subject}."
# print(msg)  # Madlib


# day = int(input('Day (0-6)?'))
# print(day)

# day_of_week = int(input('Day (0-6)?'))
# if (day_of_week == 0):
#     print('sunday')
# elif(day_of_week == 1 ):
#     print('monday') 
# elif(day_of_week == 2 ):
#     print('thuesday')  
# elif(day_of_week == 3 ):
#     print('wednesday') 
# elif(day_of_week == 4 ):
#     print('thursday') 
# elif(day_of_week == 5 ):
#     print('friday')  
# elif(day_of_week == 6 ):
#     print('saturday') 
# else :
#     print('return to  home page')        

# work_or_sleep_in = int(input('Day(0-6)?'))
# if (work_or_sleep_in < 5):
#     print('Go to work')
# else :
#     print('Sleep In')

# degree_conversion = int(input('Temperature in C?'))
# print(str(degree_conversion*9/5+32 ) + ''+'F')

# count = 1
# while (count < 11):
#     print(count)
#     count += 1


# n = input('Start from :')
# m = input ('End on :')
# count = 2
# while (count < 9):
#     print(count)
#     count += 1

square = int (input('How big is the square?'))
i = 0
while (i < square):
    j = 0
    while(j< square):
        j += 1
        print('*' , end = '')
    i +=1
    print('')
    
    