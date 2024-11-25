numbers = list()

while True:
    number = int(input())
    if number == 0:
        break
    else:
        numbers.append(number)
for i in numbers[::-1]:
    print(i)
