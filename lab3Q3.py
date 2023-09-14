S1 = int(input("side1"))
S2 = int(input("side2"))
S3 = int(input("side3"))

if (S1 < 0 or S2 < 0 or S3 < 0) :
    print ("invalid sides")

elif (S1 + S2 > S3 or S2 + S3 > S1 or S3 + S1 > S2) and (S1 >0 and S2 >0 and S3 >0):
    print(S1 ,S2 ,S3)

else :
    print("error")