#while loop
n=0
while(n<10):
    n=n+1
    if n==6:
        break
    print(n)
print("next")
n=0
while(n<5):
    n=n+1
    if n==3:
        continue
    print(n)
print("next")
n=0
while(n<5):
    n=n+1
    if n==3:
        pass
    print(n)