# Get input
expresion = input("expresion: ")

# convert this into variables

x, y, z =  expresion.split(" ")

#change type of variables x and z to floats 

type_x = float(x)
type_z = float(z)

# calculate the result

if y == "+":
    result  = type_x + type_z
if y == "-":
     result = type_x - type_z
if y == "*":
     result =  type_x * type_z
if y == "/":
     result =  type_x / type_z

print(round(result))