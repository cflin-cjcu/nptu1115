# TODO
n = int(input())
for i in range(n):
    s = input()
    print(len(set(s.lower())-{' '})==26)