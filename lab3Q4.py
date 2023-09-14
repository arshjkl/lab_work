n = (input("enter the no"))

sum= 0

while (n!=0) :
    sum = sum + (n%10)
    n= n//10

print(sum)
if sum % 3 == 0:
    print("divisible")

else:
    print("not divisible")
