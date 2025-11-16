# TODO

a = [int(input()) for i in range(10)]
b = [a.count(a[i]) for i in range(10)]

print(a[b.index(max(b))])
print(max(b))
