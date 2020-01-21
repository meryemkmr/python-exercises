# Small
#1. Madlib function

# def madlib(name,subject):
#     return(f"{name}'s favorite subject is {subject}")
    

# madlib1 = madlib('Jenn','Science')  
# print(madlib1)  


# #2. Celsius to Fahrenheit conversion

# def convert(Celcius):
#     return (Celcius*9/5+32)
# temp = convert(0)
# print(temp)

#3. Fahrenheit to Celsius conversion
# def convert(Fahrenheit):
#     return (Fahrenheit-32*5/9)
# temp = convert(100)
# print(temp)

#4. is_even function

# def is_even(num):
#     if num  == 0:
#         print('even')
#         return True
#     elif num % 2 == 0:
#         print('even')
#         return True
#     else:
#         print('odd')
#         return False
    

# all_even = is_even(9)
# print(all_even)

# # 6. only_evens function
# only_evens = [11,20,42,97,23,10]
# def is_even(num):
#     e_num = []
#     for num1 in num:    
#         if num1 % 2 == 0:
#             e_num.append(num1)
#     return e_num


# print(is_even(only_evens))


# 7. only_odds function
# only_odd = [11,20,42,97,23,10]
# def is_odd(num):
#     o_num = []
    
#     for num1 in num:

        
            
#         if num1 % 2 != 0:
#             o_num.append(num1)
        
            
        
    
#     return o_num
# print(is_odd(only_odd))

#Medium
#1. Find the smallest number

# def smallest_num_in_list( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# print(smallest_num_in_list([1, 2, -8, 0]))

#2. Find the largest number


# def largest_num_in_list(list):
#     max = list[0]
#     for a in list:
#         if a > max :
#             max = a
#     return max
# print(largest_num_in_list([1,2,-8,0]))

#3. Find the shortest String


new_shortest = ['aydin','meryem','ali']

def shortest(myshort):
    short = myshort[0]
    for i in myshort:
        if (len(i) < len(short)):
            short = i
    
    return short
print(shortest(new_shortest))



#4. Find the longest String

new_longest = ['aydin','meryem','ali']

def longest(mylong):
    long = mylong[0]
    for i in mylong:
        if (len(i) > len(long)):
            long = i
    
    return long
print(longest(new_longest))