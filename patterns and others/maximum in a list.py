n=int(input("enter n"))
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
print(l)
m=l[0]
for i in range(1,n):
    if(m<l[i]):
        m=l[i]
print(m)
