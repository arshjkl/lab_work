n = int(input("enter a sentence"))

u = 0
l = 0
d= 0
s = 0
i = 0

while i < n  :
    c = n[i]

    if "A"<=c<="Z" :
        u+=1
    elif"a"<=c<="z" :
        l +=1
    elif "0"<=c<="9" :
        d += 1
    else:
        s+=1
    i+=1