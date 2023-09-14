p = int(input("amount"))
r = 7.1
t = int(input("time in year"))
n = int(input("no.of times interests compound in a year"))

if p<500 or t<6 :
    print("error")

else : 
    x = (p*(1+r/n)**(n*t))

    print(x)