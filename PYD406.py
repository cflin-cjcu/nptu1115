# TODO
h = int(input())
while h != -9999:
    w = int(input())
    bmi = w / ((h/100)**2)
    if bmi < 18.5:
        s = "under weight"
    elif 18.5 <= bmi < 25:	
        s = "normal"
    elif 25.0 <= bmi < 30	:	
        s = "over weight"
    elif bmi >= 30:	
        s = "fat"
    print(f"BMI: {bmi:.2f}")
    print(f"State: {s}")
    h = int(input())



"""
fat
over weight
normal
under weight
BMI: _
State: _
"""