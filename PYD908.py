f_name = input()
n = int(input())
a = []
# TODO
with open(f_name) as f:
    d = f.read()
    s = d.split()
    ss = set(s) ## ss 表示不重複的字
for i in ss:
    if s.count(i) == n:
        a.append(i)
b = sorted(a)
for i in b:
    print(i)
