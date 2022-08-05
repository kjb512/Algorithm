money = 1000 - int(input())

exchange_type = [500, 100, 50, 10, 5, 1]

count = 0
for exchange in exchange_type:
    count += money // exchange
    money %= exchange

print(count)
