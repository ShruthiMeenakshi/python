n=float(input("enter n"))
x=float(input("enter estimation"))
final=0.5*(x+(n/x))
print(final)
for i in range(0,10):
    final=0.5*(final+(n/final))
print(str(final))
