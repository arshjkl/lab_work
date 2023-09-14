sal = (int(input("enter salary")))

hra = 0.2*sal
ta = 0.05*sal
da = 0.1*sal

gs = sal+hra+ta+da

print ("gross salary:",gs)

if gs<300000:
    print("no IT")

if gs >=300000:
    IT = 0.1*gs
    print(IT)

if gs >=1000000:
    IT = 0.2*gs 
    print(IT)

if gs >=2500000:
    IT = 0.3*gs 
    print(IT)

    