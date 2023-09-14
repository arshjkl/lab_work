n = int(input("enter the no."))

temp = n

r = 0

while n >0:
    d = n%10
    r = (r*10)+d
    n = n//10

if(temp==r):

    print("the no.is a palindrome")


else:
    print("the is not a palindrome")
    