def prime(n):
    count=0
    for i in range (1,n):
        if (n % i==0):
            count+=1
    return count
n=int(input("Enter the number"))
res=prime(n)
if (res==2):
    print("The number is  a prime ")
else:
    print("the number is not a prime")
