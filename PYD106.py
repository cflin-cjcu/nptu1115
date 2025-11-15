x = eval(input())
y = eval(input())
z = eval(input())

# TODO
a = (  z / 1.6)  /  ((x*60+y)/(60*60))

s = f"""
Speed = {a:.1f}
"""
print(s)