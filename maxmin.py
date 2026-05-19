def fmax(list):
    fmax=list[0]
    for i in list:
        if (i>fmax):
            fmax=i
    return fmax
def fmin(list):
    fmin=list[0]
    for  i in list:
        if(i<fmin):
            fmin=i
    return fmin
n=int(input("Enter the size of list"))
list=[]
for i in range (n):
    num=int(input("Enter the number "))
    list.append(num)
a=fmax(list)
b=fmin(list)
print(a,b)
