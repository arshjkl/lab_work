a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))

d =(b**2)-(4*a*c)

if a==0 :
    print("eqn is valid")

if d<0 :
    print("imaginary roots")

elif d==0 :
    print("real and equal roots")
    y = -b/2*a

    print(y)

elif d>0 :
    print("real and distinct roots")

    x1 = -b + (d**0.5)/2*a
    x2 = -b - (d**0.5)/2*a
    