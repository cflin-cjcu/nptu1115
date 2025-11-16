# TODO

def compute(x:int, y:int):
    for i in range(min(x,y),0,-1):
        if x%i==0 and y%i==0:
            return i

a, b = eval(input())
print(compute(a,b))