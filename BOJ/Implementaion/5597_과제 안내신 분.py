data = list(map(int, range(1, 31)))

for i in range(28):
    n = int(input())
    data.remove(n)

print(min(data))
print(max(data))
