def sliding(arr, m, n):
    s=[]
    total=sum(arr[:n])
    if total == m:
        s.append(arr[:n])
    i=1
    for i in range(len(arr)-n):
        total=total-arr[i-1]+arr[i+n-1]
        if total==m:
            s.append(arr[i:i+n])
    return s
arr = [5,2,-1,0,3]
m=6
n=3
print(sliding(arr, m, n))
