import math
def dist(x1,x2,y1,y2):
        a=(x2-x1)**2
        b=(y1-y2)**2
        c=math.sqrt(a+b)
        print(c)

x1=int(input("Enter  the number"))
x2=int(input("Enter  the number"))
y1=int(input("Enter  the number"))
y2=int(input("Enter  the number"))
dist(x1,x2,y1,y2)
