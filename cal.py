def cal(a,b,n):
    if n==1:
        print("Result:",a+b)
    elif n==2:
        print("Result:",a-b)
    elif n==3:
        print("Result:",a*b)
    elif n==4:
        print("Result:",a/b)
    else:
        print("Invalid choice")
while True:
    print("Choose operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    n = int(input("Enter your choice: "))
    if n==5:
        print("Exit")
        break
    a = int(input("Enter the number a: "))
    b = int(input("Enter the number b: "))
    cal(a,b,n)
