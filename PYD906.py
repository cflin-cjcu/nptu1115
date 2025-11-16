f_name = input()
str_old = input()
str_new = input()
#TODO
print("=== Before the replacement")
with open(f_name) as f:
    s = f.read()
    print(s)
    print("=== After the replacement")
    s_new = s.replace(str_old,str_new)
    print(s_new)
