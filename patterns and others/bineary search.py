#bineary search
n=int(input("enter n"))
f=0
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
l.sort()
print(l)
k=int(input("Enter the key to find"))
mid=len(l)//2
high=len(l)
low=0
if (k>=l[mid]):
    high=mid
else:
    low=mid
for i in range(low,high):
    if(k==l[i]):
        f=f+1
if(f==0):
    print("element found")
else:
    print("element not found")
