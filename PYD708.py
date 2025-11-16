#TODO
dict1 = {}
print("Create dict1:")
key = input("Key: ")
while key != 'end':
    value = input("Value: ")
    dict1[key]=value
    key = input("Key: ")

print("Create dict2:")
key = input("Key: ")
while key != 'end':
    value = input("Value: ")
    dict1[key]=value
    key = input("Key: ")

key = sorted(dict1)

for i in key:
    print(f"{i}: {dict1[i]}")