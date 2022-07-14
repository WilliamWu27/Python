x = input("What number would you like to multiply?")
xx = int(x)
y = input("Up to what number?")
yy = int(y)
yyy = yy + 1

for i in range(1, yyy):
    gas = xx * i
    gass = str(gas)
    ii = str(i)
    print(x + " x " + ii + " = " + gass)
    print()