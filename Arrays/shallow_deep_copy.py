'''
just for mutable objects. (set, dict, list)
'''


from copy import deepcopy, copy



a = [1, 4, 5]
b = a # shallow copy - point a and b to the same index in memory
print(id(a), id(b))
b.append(87)
print(a,b)


a = [1, 4, 5]
b = list(a) # Deep copy - list(), dict(), set() 
print(id(a), id(b))
b.append(87)
print(a,b)

# is not working for nested lists, so we use copy module
aa = [1, 4, 5, [3, 6]]
bb = list(aa) # Deep copy - list(), dict(), set() 
print(id(aa), id(bb))
bb[3][1] = 98
print(aa,bb)



aa = [1, 4, 5, [3, 6]]
bb = deepcopy(aa) # Deep copy - list(), dict(), set() 
print(id(aa), id(bb))
bb[3][1] = 98
print(aa,bb)


