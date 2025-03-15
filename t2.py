# task002
marks = int(input("enter your marks:"))

if  90 <= marks <= 100:
    print("You have secured Grade A")
elif marks >= 80 and marks < 90:
    print("You have secured Grade B")

elif marks>=70 and marks<80:
    print("You have secured Grade C")

elif marks>=60 and marks<70:
    print("You have secured Grade D")

elif marks<60 and marks >0:
    print("You have secured Grade F")

else:
    print("Invalid marks")
 