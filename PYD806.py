# TODO

def compute(s: str,c: str):
    return s.count(c)

s = input()
c = input()
a=f"{c} occurs {compute(s,c)} time(s)"
print(a)
