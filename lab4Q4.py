n = int(input("enter no."))

DC = 0
IC = 0

num = int(input("enter no."))

while n!=-999 :
    if num%n==0:
        DC = DC+1
        print("divisible count is",DC)
    else:
        IC=IC+1
        print("indivisible count is",IC)


