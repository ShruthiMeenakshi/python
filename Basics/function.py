def sum(a,b):
    z=a+b
    return z    #print(z) does not require for add=sum(10,20) instead sum(10.20) directly but can't call anywhere if we use without return

add = sum(10,20)
print(add)

#printing in main func
def mul(x,y):
    return x*y

num_mul=mul(10,20)
print(num_mul)

#bring 2 func together
def multi(p,q):
    return p*q

print(multi(sum(1,3), sum(5,6)))


#strings
def greetings(name):
    print("Hi " + name)

greetings("malli")