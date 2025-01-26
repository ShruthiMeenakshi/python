#strings
#inversion of string
s=input("enter sentence")
s1=''
for c in s:
    s1=c+s1
print(s1)

#palindrome
if(s==s1):
    print("palindrome")
else:
    print("not palindrome")
    
#count string
count=0
for i in range(0,len(s)):
    if(s[i]!=' '):
        count+=1
print(str(count))
