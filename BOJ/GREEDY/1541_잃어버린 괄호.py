a, b = map(int, input().split())
cnt = 0

while True:
    if a == b:
        break
    elif b == 0:
        print('-1')
        exit()

    if b%2 == 1:
        b -= 1
        b = b/10
    else:
        b //= 2
    cnt += 1

print(cnt+1)
