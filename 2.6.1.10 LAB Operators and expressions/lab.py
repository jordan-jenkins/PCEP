x = float(input("Enter value for x: "))

# Write your code here.
# y1 = x + (1/x) 
# y2 = x + (1/y1)
# y3 = x + (1/y2)
# y = 1/y3

y = 1/(x+(1/(x+(1/(x+(1/x))))))

print("y =", y)