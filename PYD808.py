# TODO
s = input()
print("Valid SSN" if s[:3].isnumeric() and s[4:6].isnumeric() and s[-4:].isnumeric() else "Invalid SSN")


