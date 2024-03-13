'''
4 # (N, 2N-1)
...D... 
..D.D..
.D...D.
D.D.D.D

8
.......D.......
......D.D......
.....D...D.....
....D.....D....
...D.......D...
..D.........D..
.D...........D.
D.D.D.D.D.D.D.D

'''

def insert_(size):
    table = [['.' for _ in range(2*size-1)] for _ in range(size)] # create 2n array

    for i in range(size):
        table[i][size-1-i] = 'D'
        table[i][size-1+i] = 'D'

    table[size-1] = ['D' if i % 2 == 0 else '.' for i in range(2*size-1)]
    return table


output = insert_(int(input()))
for row in output:
    print(''.join(row))