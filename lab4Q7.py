n = int (input("enter value"))

a = 1 
b = 1 

sum = a + b 

count=1

print("fibonacci series is")

while(count<=n):
    count +=1
    print(a)

    a= b
    
    b = sum

    sum = a +b