
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]) - int(ord('a'))) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]

count = 0
for step in steps:
  nrow = row + step[0]
  ncol = col + step[1]
  if(nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8):
    continue
  count += 1

print(count)