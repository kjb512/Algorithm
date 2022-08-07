h, n = map(int, input().split())

data = list(map(int, input().split()))

plugs = []

count = 0
for i in range(n):
    new = data.pop(0)
    if new in plugs:
        continue

    if len(plugs) < h:
        plugs.append(new)
        continue

    index = []
    for j in range(h):
        if plugs[j] in data:
            index.append(data.index(plugs[j]))
        else:
            index.append(j+n)
            break
    mi = max(index)
    if mi >= n:
        mi -= n
        plugs[mi] = new
    else:
        plugs[plugs.index(data[mi])] = new
    count += 1

print(count)
