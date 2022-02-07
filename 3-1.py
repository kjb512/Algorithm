# 지불 금액
pay = 1250
# 거스름돈 큰 순서대로
exchange_type = [500, 100, 50]
# 동전 개수
count = 0 

for exchange in exchange_type:
  count += pay//exchange
  pay%=exchange

print(count)