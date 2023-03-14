n = int(input())
data = []

for i in range(n):
    first, second = map(int, input().split())
    data.append([first, second])

data = sorted(data, key=lambda a:a[0])
data = sorted(data, key=lambda a:a[1])

## 2차원 요소를 기준으로 정렬할 때 sorted(list, key = lambda a:a[n]) 사용

last = 0
cnt = 0

for first, second in data:
    if first >= last:
        cnt += 1
        last = second

print(cnt)
