def reverse(list):
    i=0
    j=len(list)-1
    while i<j:
        list[i],list[j]=list[j],list[i]
        i+=1
        j-=1
    return list

list = [234,456,345453,34534542342424244,454423]
print(reverse(list))
