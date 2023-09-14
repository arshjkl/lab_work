a = int(input("first side"))
b = int(input("second side"))
c = int( input("third side"))

s = (a+b+c/3)


area = (s*(s-a)*(s-b)*(s-c)**0.5)

print(area)