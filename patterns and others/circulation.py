m=int(input("enter number of elements"))
l=[]
for i in range(1,m+1):
    a=int(input("enter no. to be appended"))
    l.append(a)
print(l)
n=int(input("enter number of times to be circulated"))
for i in range(0,n):
    for j in range(0,len(l)-1):
        t=l[j]
        l[j]=l[j+1]
        l[j+1]=t
print(l)

