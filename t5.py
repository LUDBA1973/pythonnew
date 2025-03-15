
# task05
a= int(input("enter num 1: "))
b= int(input("enter num 2: "))

if a>b:
    if a>200:
        print(a,"is greater than",b)
        print(a,"is greater than 200")
    else:
        print(a,"is greater than",b)
elif a == b:
    if a>200:
        print(a,"is equal to",b)
        print(a,"is greater than 200")
    else:
        print(a,"is equal to",b)
else:
    if a>200:
     print(b,"is greater than",a)
     print("But",a,"is greater than 200")
    else:
        print(b,"is greater than",a)

        