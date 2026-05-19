def BS(list,f):
    list.sort()
    low=0
    high=n-1
    mid=(high-low)//2
    while low<=high:
        if(f==list[mid]):
            return mid
        elif(list[mid]<f):
            low=mid+1
        else:
            high=mid-1
    return -1                          
    
n=int(input("Enter size of  List"))
list=[]
for i in  range (n):
    num=int(input(f"Enter the number {i+1} :"))
    list.append(num)
f=int(input("Enter the element"))
res=BS(list,f)
if res!=-1:
    print("Element is found") 
else:
    print("element is not found")
