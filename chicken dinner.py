x=input().split(',')
y=sorted(list(set(x)))
z=[]
for i in range(0,len(y)):
    z.append(x.count(y[i]))
t=z.index(max(z))
print(y[t])
