print("\n-----------Calculator-----------")
first_no = float(input("\n1️⃣. Enter the first number: "))
second_no = float(input("2️⃣. Enter the first number: "))
user_sign = input("➡️. Enter the sign (+, -, *, /): ")

def calculate(first_no, second_no, user_sign):
    if user_sign == "+":
        return first_no + second_no
    elif user_sign == "-":
        return first_no - second_no
    elif user_sign == "*":
        return first_no * second_no
    elif user_sign == "/":
        if second_no == 0:
            return "Error: Division by zero"
        return first_no / second_no
    else:
        return "Error: Invalid operator"
    
results = calculate(first_no, second_no, user_sign)
print("\n🔢. The result is: \n\t", results,"\n")
