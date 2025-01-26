n=int(input("Enter how many numbers"))
for i in range(n,0,-1):
    for j in range(0,i+1,):
        print("*",end=" ")
    print()
