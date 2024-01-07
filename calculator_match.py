# Simple calculator using match operator 

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

operator = input("enter operator: ")

match operator:
    case "+":
        print  # addition 
    case "-":
        print(num1 -num2)  # substraction 
    case "*":
        print(num1*num2)   #multiplication 
    case "**":
        print(num1 **num2)  # exponentation
    case "/":
        print(num1/num2)   # division 
    case "//":
        print(num1//num2)   # floar division 
    case "%":
        print(num1%num2)  # remiander
