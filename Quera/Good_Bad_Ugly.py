# Inputs
N = int(input())
grave_names = []
for _ in range(N):
    grave_names.append(input())

people_names = []
for _ in range(N-1):
    people_names.append(input())

# Create a dictionary to count the occurrence of each grave name
grave_count = {}
for grave_name in grave_names:
    if grave_name in grave_count:
        grave_count[grave_name] += 1
    else:
        grave_count[grave_name] = 1

# Count the occurrences of each person's name in the list of grave names
person_count = {}
for person_name in people_names:
    if person_name in person_count:
        person_count[person_name] += 1
    else:
        person_count[person_name] = 1

# Search for the fake grave
for person_name, count in person_count.items():
    if person_name in grave_count:
        grave_count[person_name] -= count

# Check which grave has a non-zero count
for grave_name, count in grave_count.items():
    if count != 0:
        print(grave_name)
        break