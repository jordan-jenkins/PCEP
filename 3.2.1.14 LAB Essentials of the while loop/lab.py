blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

# height = 0
# previous_layer = 0

# while blocks > previous_layer:
#     previous_layer += 1
#     blocks -= previous_layer
#     print(previous_layer)
#     height += 1

height = 0

while blocks > height:
    height += 1
    blocks -= height
    
    
print("The height of the pyramid:", height)