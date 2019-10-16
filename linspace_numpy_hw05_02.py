start = float(input())
end = float(input())

count = int(input())
L = []
L.append(start)
while count > 1:
    d = (end - start) / (count - 1)
    start += d
    L.append(start)
    count -= 1

print(L)