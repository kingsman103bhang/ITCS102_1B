#FACTORIAL PROGRAM

print("THE FACTORIAL PROGRAM")
number = eval(input("Enter any number --> "))
factorial = 1
for f in range(number,0,-1):
        factorial *= f
print("The factorial of",number,"is",factorial)


