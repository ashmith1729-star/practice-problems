def anagrams(s):
    list=[]
    for i in s:
        f=ord(i)
        list.append(f)
    list.sort()
    return list
str1="ASHMITH RAO"
str2="RAO ASHMITH"
if len(str1)!=len(str2):
    print("strings are not anagrams")
else:
    a=anagrams(str1)
    b=anagrams(str2)
    if a==b:
        print("strings are anagrams")
    else:
        print("strings are not anagrams")
 

