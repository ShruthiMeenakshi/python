#to check the given no. is armstrong or not
#the no. of digits are raised to their power of each digit and their power of sum of the digits=the given no.
for i in range(0,5):
    n=int(input("Enter n"))
    a=0
    c=0
    E=n
    d=n
    while(n>0):
        n=int(n/10)
        a=a+1
    print(a)
    while(d>0):
        r=d%10
        c+=pow(r,a)
        d=int(d/10)
    if(c==E):
        print("it is armstrong")
    else:
        print("not an armstrong")

