n = int(input())
coins = [500,100,50,10,5,1]
cnt = 0
coin = 1000 - n

for i in coins:
    cnt += coin // i
    coin = coin % i

print(cnt)
