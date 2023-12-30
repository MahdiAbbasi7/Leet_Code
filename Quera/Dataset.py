a, b, c = input().split()

Dataset = []
test = []

for i in range(int(a)):
    Dataset += input().split()

for j in range(int(b)):
    test += input().split()

dict_dataset = {Dataset[i]: Dataset[i + 1] for i in range(0, len(Dataset), 2)}

result = []
for i in test : 
    value = dict_dataset.get(i)
    if value is None:
        result.append('Unknown')
        # print(result)
    else :
        result.append(value)

print(*result, sep='\n')