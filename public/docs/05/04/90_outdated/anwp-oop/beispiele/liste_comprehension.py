x = [3, -6, -8, 9, 15]
print(x)
y = [2, 13, 4, -8, 4]
print(y)
print()

a = [z+1 for z in x]
print(a)

b = [z+1 for z in x if z>0]
print(b)

c = [x[i]+y[i] for i in range(len(x))]
print(c)

d = [x[i]+y[i] for i in range(len(x)) if x[i]>0 and y[i]>0]
print(d)
