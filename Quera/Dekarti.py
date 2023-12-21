'''
3 4
 _ _ _ _
| | | | |
 _ _ _ _
| | | | |
 _ _ _ _
| | | | |
 _ _ _ _

1 1 
 _
| |
 _

'''

a, b= input().split()

def print_pattern(n, m):
    for _ in range(n):
        print(' _' * m)
        print('| ' * (m + 1))
    print(' _' * m)

print_pattern(int(a), int(b))