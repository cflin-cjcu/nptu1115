# TODO

def compute(r: int, c:int):
    a = [ [f"{j-i:4d}" for j in range(c)] for i in range(r)]

    for i in a:
        print(*i)


r = int(input())
c = int(input())
compute(r,c)