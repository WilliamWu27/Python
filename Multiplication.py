x = input("What number would you like to multiply?")
xx = int(x)
y = input("Up to what number?")
yy = int(y)
yyy = yy + 1

for j in range(1, yyy):
    for i in range(1, j):
        gas = j * i
        gass = str(gas)
        ii = str(i)
        print(str(j) + " x " + ii + " = " + gass, end=" | ")
    print()
    