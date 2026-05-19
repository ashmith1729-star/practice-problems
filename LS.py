n=int(input("Enter size of  List"))
list=[]
for i in  range (n):
    num=int(input(f"Enter the number {i+1} :"))
    list.append(num)
f=int(input("Enter the element "))
count=0
for i in range (n):
    if(list[i]==f):
        count=count+1
if(count>0):
    print("Element is found")
else:
    print("Element is not found")
