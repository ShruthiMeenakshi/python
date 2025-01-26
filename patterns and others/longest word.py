a=input("enter a sentence")
b=a.split()
b=max(b,key=len)
print("the longest word is ",b)
