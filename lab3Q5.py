n = int(input())

sum= 0 

while (n !=0):
    sum = sum + (n%10)
    n = n//10

print(sum)

if sum%3 ==0:
    print("yes it is divisible")

else :
    print ("it is not divisible")
    