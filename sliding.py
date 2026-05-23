def sliding(arr, m, n):
    s = []
    sum = sum(arr[:n])
    if sum == m:
        s.append(arr[:n])
    i=1
    for i in range(len(arr)-n):
        sum=sum-arr[i-1]+arr[i+n-1]
        if sum==m:
            s.append(arr[i:i+n])
    return s
arr = [5,2,-1,0,3]
print(sliding(arr, 6, 3))
