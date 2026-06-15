#Program to see the difference bet var

"""
Difference  is that for var a & b values are same but 
depends on syntax it treated as variable and list which uses 
different memory address 
""" 

a = 10
b = 10

print("Memory Address of a is: ", id(a))
print("Memory Address of b is: ", id(b))

a = [10]
b = [10]

print("Memory Address of a is: ", id([a]))
print("Memory Address of b is: ", id([b]))