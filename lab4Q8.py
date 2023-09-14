n = int(input("enter number"))

i = 2 
f = 0

if n==1 :
    print("1 is either prime or composite")


while i <= n :
    if n %i == 0 :
        f =1
    break

if f ==1:

    print("the entered no is not a prime no")

else :
    print("the entered no is a prime no.")