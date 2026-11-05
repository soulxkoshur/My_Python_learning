x, y, z = input("Enter the expression with space: ").split(" ")

if y == "+":
    result = float(x) + float(z)
    print(round(result, 2))

elif y == "-":
    result = float(x) - float(z)
    print(round(result, 2))

elif y == "*":
    result = float(x) * float(z)
    print(round(result, 2))

elif y == "/" and z == 0:
    
    print("dividing by zero is not possible")
elif y == "/":
    result = float(x) / float(z)
    print(round(result, 2))

else: 
    print("please enter a valid expression")


