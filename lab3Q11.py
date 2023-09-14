n = int(input("enter a no"))

sum = 0

temp = n

while temp > 0 :
    digit = temp % 10
    sum += digit**3
    temp//=10

if n == sum :
    print ("it is a armstrong no")

else :
    print ("n is not a armstrong no")