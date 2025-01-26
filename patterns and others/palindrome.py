n=int(input("enter n "))
s=0
a=n
while(n>0):
    r=n%10
    s=(s*10)+r
    n=int(n/10)
if(a==s):
    print("palindrome")
else:
    print("not palindrome")
