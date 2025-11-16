# TODO

print("Create tuple1:")
# TODO
a = []
i = int(input())
while i != -9999:
    a.append(i)
    i = int(input())

print("Create tuple2:")
# TODO
b = []
i = int(input())
while i != -9999:
    b.append(i)
    i = int(input())

c = (*a,*b)
list(c).s

d = sorted(list(c))


print(f"Combined tuple before sorting: {c}")
print(f"Combined list after sorting: {d}")
