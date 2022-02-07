pay = 1250
exchange_type = [500, 100, 50]

count = 0 

for exchange in exchange_type:
  count += pay//exchange
  pay%=exchange

print(count)