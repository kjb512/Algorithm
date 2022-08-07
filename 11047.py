n, pay = map(int, input().split())

exchange_type = []
for i in range(n):
    exchange_type.append(int(input()))
exchange_type.reverse()

count = 0
for exchange in exchange_type:
    count += pay // exchange
    pay %= exchange
print(count)
