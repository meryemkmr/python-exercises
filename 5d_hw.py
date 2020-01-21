# Small
#1. Phonebook dictionary

phonebook_dict = {
'Alice': '703-493-1834',
'Bob': '857-384-1234',
'Elizabeth': '484-584-2923'
}

# myphone = phonebook_dict.get("Elizabeth")
# print(myphone)

# phonebook_dict["Kareem"] = "938-489-1234"
# print(phonebook_dict)
# del phonebook_dict["Alice"]
# print(phonebook_dict)
# phonebook_dict["Bob"] = "968-345-2345"
# print(phonebook_dict)


# 2. Nested dictionaries

# ramit = {
# 'name': 'Ramit',
# 'email': 'ramit@gmail.com',
# 'interests': ['movies', 'tennis'],
# 'friends': [
#     {
#     'name': 'Jasmine',
#     'email': 'jasmine@yahoo.com',
#     'interests': ['photography', 'tennis']
#     },
#     {
#     'name': 'Jan',
#     'email': 'jan@hotmail.com',
#     'interests': ['movies', 'tv']
#     }
# ]
# }

# for key ,value in ramit.items():
#     print(key ,value)
# emailIs = ramit.get('email')
# print(emailIs)

# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'])


# 3. Friend counter


# {
# 'name': 'Ramit',
# 'email': 'ramit@gmail.com',
# 'interests': ['movies', 'tennis'],
# 'friends': [
#     {
#     'name': 'Jasmine',
#     'email': 'jasmine@yahoo.com',
#     'interests': ['photography', 'tennis']
#     },
#     {
#     'name': 'Jan',
#     'email': 'jan@hotmail.com',
#     'interests': ['movies', 'tv']
#     }
# ],
# 'friends_count': 2
# }


# Medium
#1. Letter Summary

# 1. Way

# letter_histogram = input('Please enter a word  :')
# counts = {}
# for word in letter_histogram:
#     if word not in counts:
#         counts[word]=1
#     else :
#         counts[word] +=1
# print(counts)

# 2. Way

# enter_word = input("Please enter a word: ")
# def word_freq(word):
#     my_dict = {}
#     for letter in word:
#         keys = my_dict.keys()
#         if letter in keys:
#             my_dict[letter] += 1
#         else:
#             my_dict[letter] = 1
#     return my_dict
# print(word_freq(enter_word))






# 2. Word Summary

# world_histogram = input('Please enter a sentence')
# world_his = world_histogram.split()
# counts= {}

# for word in world_his:
#     if word not in counts:
#         counts[word] = 1
#     else:
#         counts[word] +=1
# print(counts)





# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# helloIs = my_dictionary["hello"]
# print(helloIs)
# 
# watIs = my_dictionary.get("wat")
# print(watIs)
# isItThere = "wat" in my_dictionary
# print(isItThere)
# my_dictionary["theMeaningOfLife"] = "wat"
# wat = my_dictionary["theMeaningOfLife"]
# print(wat)
# my_dictionary["newKeyName"] = "hello world"
# print(my_dictionary)

name = input('Please enter your name?'.upper())
print(f'Hello , {name}'.upper())
print(f'Your Name Has {len(name)} letter in it! Awesome!')