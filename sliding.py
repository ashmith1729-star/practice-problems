def sliding(list,m,n):
    l=len(list)-n
    i=0
    s=[]
    while i<=l:
        j=0
        sum=0
        f=[]
        k=i
        while j<=n-1:
            sum=sum+list[k]
            f.append(list[k])
            k+=1
            j+=1    
            
        if sum==m:
            s.append(f)
        i+=1
    return s
list=[2, 1, 5, 1, 3, 2, 4, 3]
n=3
m=9
print(sliding(list,m,n))