# n, m = map(int, input().split())
# computers = "0" * n
# result = []

# for _ in range(m):
#     s, l = map(int, input().split())
#     slice_ = computers[s - 1 :]
#     requested_chairs = "0" * l
#     idx = slice_.find(requested_chairs)
#     if idx != -1:
#         computers = list(computers)
#         computers[s - 1 + idx : s - 1 + idx + l] = "1" * l
#         computers = "".join(computers)
#     result.append(computers)
        
# print('\n'.join(result))


n, m = map(int, input().split())
computers = "0" * n

for _ in range(m):
    s, l = map(int, input().split())
    slice_ = computers[s - 1 :]
    requested_chairs = "0" * l
    idx = slice_.find(requested_chairs)
    if idx != -1:
        computers = list(computers)
        computers[s - 1 + idx : s - 1 + idx + l] = "1" * l
        computers = "".join(computers)
        print(computers)