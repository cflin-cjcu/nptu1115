# TODO
n = int(input())
s = 0
for i in range(2,n+1):
    s += 1 / ((i-1) ** 0.5 + i ** 0.5 )
print(f"{s:.4f}")    
