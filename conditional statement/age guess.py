age = int(input("Please enter your age..."))

if age <100 :
    print("Your age between 0-100.")
    if age < 50 :
        print("Your age between 0-50.")
    elif age ==50:
        print("You are 50 years old")
    elif age >50 :
        print("Your age between 50-100.")
else :
    print("Please enter a value between 0-100.")

