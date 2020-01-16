# 1. Multiply Vectors



# a = [2,4,5]
# b = [2,3,4]
# ab =[]

# for i in range(len(a)):
#     ab.append(a[i]*b[i])

# print(ab)

# 2. Matrix Addition 
# 1.Way 
# a = [[2,4], [1,6]]
# b = [[4,7], [2,3]]
# new_big_list = []
# # outer
# for indexOne in range(len(a)):
#     # a[index] b[index]
#     # [2,4]       [4,7]
#     new_small_list = []
#     # inner
#     for indexTwo in range(len(a[indexOne])):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)

# 2.Way
# a = [[2,4], [1,6]]
# b = [[4,7], [2,3]]
# sum = [[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         sum[i][j] = a[i][j]+b[i][j]
# for s in sum:
#     print(s)
# 3.Way
# matrix1 = [[2,4], [1,6]]
# matrix2 = [[4,7], [2,3]]
# result = []
# for index1 in range(len(matrix1)):
#     for index2 in range(len(matrix2)):
#         if(index1==index2):
#             work_list = []
#             sum1 = matrix1[index1][0]+matrix2[index2][0]
#             sum2 = matrix1[index1][1]+matrix2[index2][1]
#             work_list.append(sum1)
#             work_list.append(sum2)
#             result.append(work_list)
# print(result)


# 3. Matrix Addition II

# a = [[2,3,4],[4,5,6],[6,7,8]]
# b =[[23,45,67],[89,77,67],[12,34,56]]

# sum = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         sum[i][j]= a[i][j]+b[i][j]
# for s in sum:
#     print(s)

# 4. De-dup

# 1. method
# Your list with duplicate values
# duplicates = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# Print the unique `duplicates` list
# print(list(set(duplicates)))


# 2. method
# duplicates = [1, 2, 3, 1, 2, 5, 6, 7, 8]
# unduplicated = []
# for i in duplicates:
#     if i  not in unduplicated:
#         unduplicated.append(i)
# print(unduplicated)

#5. Leetspeak
# my_string ='I am a leet programmer'.upper()
# leet_list =list(my_string)
# for i in range(len(leet_list)):
#     if leet_list[i]== 'A':

#         leet_list[i]= '4'
#     elif leet_list[i]=='E':
#         leet_list[i]= '3'
#     elif leet_list[i]=='G':
#         leet_list[i]= '6'
#     elif leet_list[i]=='I':
#         leet_list[i]= '1'
#     elif leet_list[i]=='O':
#         leet_list[i]= '0'
#     elif leet_list[i]=='S':
#         leet_list[i]= '5'
#     elif leet_list[i]=='T':
#         leet_list[i]= '7'


# leet_sentence = ''.join(leet_list)
# print(leet_sentence.lower())







#Small
#1. Sum the Numbers

# numbers = [1,2,3,4,5,6,7]

# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
