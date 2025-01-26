#linear search
n=int(input("enter n "))
l=[]
f=0
for i in range(0,n):
    a=int(input("enter value "))
    l.append(a)
print(l)
k=int(input("enter key "))
for i in range(0,n):
    if(k==l[i]):
        f=f+1
        m=i
if(f==0):
    print("element not found")
else:
    print("element found at",m, "index")
