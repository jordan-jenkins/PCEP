year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year >= 1582:
    if year % 4 != 0:
        output = "Common year"
    elif year % 100 != 0:
        output = "Leap year"
    elif year % 400 !=0:
        output = "Common year"
    else:
        output = "Leap year"
else:
    output="Not within the Gregorian calendar period"
    
print(output)