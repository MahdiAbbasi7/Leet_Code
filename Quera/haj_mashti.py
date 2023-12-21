'''
YNY -> Haji
NNN -> Agha
NNY -> Mashti
NYY -> Karbalaee
'''

vorodi = input()

list(vorodi)

for i in range(len(vorodi)) : 
    if vorodi[i] == 'Y':
        print('Haji')
        break
    elif vorodi[i + 1] == 'Y' : 
        print('Karbalaee')
        break
    elif vorodi[i + 2] == 'Y' : 
        print('Mashti')
        break
    else : 
        print('Agha')
        break