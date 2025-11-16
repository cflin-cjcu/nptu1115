# TODO
i = int(input())
a = set()
while i != -9999:
    a.add(i)
    i = int(input())

s=f"""Length: {len(a)}
Max: {max(a)}
Min: {min(a)}
Sum: {sum(a)}"""
print(s)
