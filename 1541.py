
a = input()
b = a.split("-")

c = []
for p in b:
    c.append(sum(list(map(int, p.split("+")))))

sum = c[0]
for i in range(1, len(c)):
    sum -= c[i]

print(sum)
