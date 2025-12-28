k = input("Enter your name ---> ")
print("===================================\nODD NUMBER SUMMATION, press 0 to stop\n===================================")
sum = 0
odd = ''
while True:
    den = eval(input("Input a random number ---> "))
    if den == 0:
        print("Program stops .!!!")
        break
    elif den % 2 == 1:
        print("ODD NUMBER DETECTED, code continues")
        sum += den
        odd = str(den) + " "
        continue
    elif den % 2 == 0:
        print("EVEN NUMBER DETECTED, continue")
        continue
print(f"Hi {k}, the sum of all ODD number is {sum}")
print(f"ODD numbers detected included the ff {odd}")