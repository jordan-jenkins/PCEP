c0 = int(input("Enter a number:"))

steps = 0
while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 /= 2
        print(int(c0))
    else:
        c0 = 3 * c0 + 1
        print(int(c0))

print("steps =",steps)
