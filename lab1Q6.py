a = int(input())
b = int(input())
c = int(input())

disc = ((b**2)-(4*a*c))

if disc < 0 :
    print("no real roots")
elif disc==0:
    print("roots are equal")
else :
    print("roots are real and distinct")
    root1 = (-b+disc/2*a)
    root2 = (-b-disc/2*a)

    print(root1,root2)
    