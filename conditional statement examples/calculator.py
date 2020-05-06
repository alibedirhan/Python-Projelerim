entry = """
(1) addition
(2) subtraction
(3) multiplication
(4) division
(5) square
(6) square root
"""
print(entry)

process = input("Enter the number of the process you want to: ")

if process == "1":
    num1 = int(input("Enter the first number for addition: "))
    num2 = int(input("Enter the second number for addition: "))
    
    print(num1, "+", num2, "=", num1 + num2)

elif process == "2":
    num3 = int(input("Enter the first number for substraction: "))
    num4 = int(input("Enter the second number for substraction: "))

    print(num3, "-", num4, "=", num3 - num4)

elif process == "3":
    num5 = int(input("Enter the first number for multiplication : "))
    num6 = int(input("Enter the second number for multiplication: "))

    print(num5, "x", num6, "=", num5 * num6)

elif process == "4":
    num7 = int(input("Enter the first number for division: "))
    num8 = int(input("Enter the second number for division: "))

    print(num7, "/", num8, "=", num7 / num8)

elif process == "5":
    num9 = int(input("Enter the number for square: "))

    print(num9, "square of number =", num9 ** 2)

elif process == "6":
    num10 = int(input("Enter the number square root : "))

    print(num10, "square root of number = ", num10 ** 0.5)
else:

    print("Wrong process.")

    print("Enter one of the options below:", entry)

