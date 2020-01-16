# 1. Multiply Vectors



# a = [2,4,5]
# b = [2,3,4]
# ab =[]

# for i in range(len(a)):
#     ab.append(a[i]*b[i])

# print(ab)

# 2. Matrix Addition  ==> I couldn't got well
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


# a = [[2,4], [1,6]]
# b = [[4,7], [2,3]]
# sum = [[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         sum[i][j] = a[i][j]+b[i][j]
# for s in sum:
#     print(s)

# 3. Matrix Addition II

a = [[2,3,4],[4,5,6],[6,7,8]]
b =[[23,45,67],[89,77,67],[12,34,56]]

sum = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        sum[i][j]= a[i][j]+b[i][j]
for s in sum:
    print(s)

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





#Small
#1. Sum the Numbers

# numbers = [1,2,3,4,5,6,7]

# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
