# CALCULATOR

a = int(input("Enter the value of A \n"))
b = int(input("Enter the value of B \n"))
sign = input("Enter the operation +,-,/,% \n")
if (sign == "+"):
    print ("Answer is ", a + b)
elif(sign == "-"):
    print("Answer is ", a - b)
elif(sign == "/"):
    print("Answer is ", a / b)
elif(sign == "*"):
    print("Answer is ", a * b)
elif(sign == "%"):
    print("Answer is ", a % b)
else:
    print("Enter the correct operation")
