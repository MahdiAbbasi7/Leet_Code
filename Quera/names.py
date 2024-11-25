n = int(input())
list_of_names = []
counter, max_of_counters = 0, 0
var = ""

for i in range(n):
    list_of_names.append(input())


for n1p in range(len(list_of_names)):
    for n2p in list_of_names[n1p]:
        if n2p in var:
            counter -= 1
        else:
            var += n2p
            counter += 1
    var = ""
    if max_of_counters < counter:
        max_of_counters = counter
    counter = 0

print(max_of_counters)
