n = int(input())

for i in range(n):
    k = int(input())
    data = list(map(int, input().split()))
    print(min(data), max(data))
