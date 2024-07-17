# from pprint import pprint

# another_list = []
# def strings(Strings:list[str]):
#     list_of_strings = list(Strings)
#     for i in range(len(list_of_strings)):
#         for j in range(len(list_of_strings)):
#             another_list.append(list_of_strings[i] + list_of_strings[j])
#     return another_list

# another_list1 = []
# def strings1(list_strings:list[str]):
#     for _ in range(len(list_strings)):
#         for _ ,k in enumerate(list_strings):
#           another_list1.append(k + 'a')
#           another_list1.append(k + 'b')
#         final = sorted(set(another_list1))
#     return final


# another_list2 = []
# def strings2(list_strings:list[str]):
#     for _ in range(len(list_strings)):
#         for _ ,k in enumerate(list_strings):
#           another_list2.append(k + 'a')
#           another_list2.append(k + 'b')
#         final = sorted(set(another_list2))
#     return final



# another_list3 = []
# def strings3(list_strings:list[str]):
#     for _ in range(len(list_strings)):
#         for _ ,k in enumerate(list_strings):
#           another_list3.append(k + 'a')
#           another_list3.append(k + 'b')
#         final = sorted(set(another_list3))
#     return final


# another_list4 = []
# def strings4(list_strings:list[str]):
#     for _ in range(len(list_strings)):
#         for _ ,k in enumerate(list_strings):
#           another_list4.append(k + 'a')
#           another_list4.append(k + 'b')
#         final = sorted(set(another_list4))
#     return final

# string1 = strings(['a', 'b'])

# string11 = strings1(['aa', 'ab', 'ba', 'bb'])

# string21 = strings2(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'])

# string31 = strings3(['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 
#                 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb'])

# string41 = strings4(['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 
#                 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 
#                 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 
#                 'bbaaa', 'bbaab', 'bbaba', 'bbabb', 'bbbaa', 'bbbab', 'bbbba', 'bbbbb'])

# first_list = ['a', 'b']
# finallist = first_list + string1 + string11 + string21 +  string31 + string41

# for i ,k in enumerate(finallist):

#   if number == i +1:
#     print(k[-1])

number = int(input(''))

if number % 2 == 0:
    print('b')
else:
    print('a')


