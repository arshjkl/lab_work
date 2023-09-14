sec = int(input("enter time in seconds"))
sec = sec%(24*3600)

h = sec//3600
sec %= 3600
min = sec//60

sec%= 60

print(h,"hours",min,"minutes",sec,"seconds")
