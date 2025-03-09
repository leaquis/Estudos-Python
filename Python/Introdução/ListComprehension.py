a = [1, 2, 3, 4, 5]
b = []

for i in a:
    b.append(i**2)

c = [i**3 for i in a]
d = [i for i in a if i%2==1]

print(a)
print(b)
print(c)
print(d)
