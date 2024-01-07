# largest among the three numbers 

# taking 3 numbers as input from user
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))

# checking which number is greatest 
if a>b:
    if a>c:
        print("a is largest with it's value",a)
    else:
        print("c is largest with it's value",c)
elif b>c:
     print("b is largest with it's value",b)
else:
    print("c is largest with it's value",c)