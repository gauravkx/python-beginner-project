
# making calcultor using match case


num1 = float(input("enter num1:"))
num2 = float(input("enter num2:"))

print("only these operator is avialable now, +,-,*,/,%,")

operator = input("enter operator:")

match operator:
    case "+":
        print("sum is ", num1+num2)
    case "-":
        if num1>=num2:
           print("diff is ", num1-num2)
        else:
            print("diff is ", num2-num1)
    case "*":
        print("product is ", num1*num2)
    case "/":
        print('division is ', num1/num2)
    case "%":
        print("reminder is ", num1%num2)
    case _:
        print("enter valid operator")