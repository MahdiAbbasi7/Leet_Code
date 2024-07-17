'''
000? -> 0000, 0001 -> 0, 1
00?0 -> 0000, 0010 -> 0, 4
0?11 -> 0011, 0111 -> 3, 7

'''
for_zero = []
for_one = []
change_to_decimal = []
def find(inputs:list[str]):
    for i, v in enumerate(inputs):
        if '?' in v:
            for_zero.append(v.replace('?', '0'))
        if '?' in v:
            for_one.append(v.replace('?', '1'))
    print(f'if ? equal to 0: {sorted(for_zero)} and if equal to 1: {sorted(for_one)}')
    final = sorted(for_zero + for_one)
        
    for value in final:
        change_to_decimal.append(int(value, 2))

    return change_to_decimal

print(find(['000?','00?0', '0?11']))
