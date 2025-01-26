n=float(input("enter your salary"))
g=input("male(m) or female(F)").upper()
if g=="m":
    total=n+n*0.10
else:
    total=n+n*0.12
print("total amount",total)
