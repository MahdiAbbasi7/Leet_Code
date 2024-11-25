keyvoon = (3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2) * 6
nezam = (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3) * 3
shir_farhad = (2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3) * 4

num_of_tests = int(input())
answer_of_tests = input().strip()
tuple_of_str_of_answers = tuple(str(answer_of_tests))

correct_answers_key = 0
correct_answers_nez = 0
correct_answers_shir = 0

for i in range(len(tuple_of_str_of_answers)):
    if keyvoon[i] == int(tuple_of_str_of_answers[i]):
        correct_answers_key += 1

for i in range(len(tuple_of_str_of_answers)):
    if nezam[i] == int(tuple_of_str_of_answers[i]):
        correct_answers_nez += 1


for i in range(len(tuple_of_str_of_answers)):
    if shir_farhad[i] == int(tuple_of_str_of_answers[i]):
        correct_answers_shir += 1

result = {
    "keyvoon": correct_answers_key,
    "shir farhad": correct_answers_shir,
    "nezam": correct_answers_nez,
}

temp = max(result.values())
print(temp)
res = [key for key in result if result[key] == temp]
for names in res:
    print(names)
