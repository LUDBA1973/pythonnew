# for loop

# iterate list and print each elements

numbers=[1,2,5,6,3,8]




# break and continue
# break and continue are used to control the flow of for loop
# break is used to exit the loop
# continue ski[s the current iteration and move to next one

# for i in numbers:

#     if i==5:
#         break
#         # continue
#     print(i)

# range
# range is a function that returns a sequence of numbers

# it is used to generate a sequence of numbers

for i in range(1,10):
    # if i==5:
    #     continue
    # if i==9:
    #     break
    print(f"5*{i}=",i*5)
    

# nested loop

# loop inside loop
# inner loop will run first
# then outer loop will run


# b = '*'
# for i in range(6):
#     # for j in b:
#         print(i*b)
'''
rows =int(input("enter no of rows:"))

for i in range(rows):
         print("* "*(i+1))

for i in range(rows,0,-1):
    print("* "*i)


# for i in range(rows):
#     print("*"*(rows-i))
      
# hill
for i in range(rows):
    print(" "*(rows-i-1)+"* "*(i+1)) 
  
#   reverse hill
for i in range(rows):  
     print(" "*i+"* "*(rows-i))

# right triangle
for i in range(rows+1):
    print(" " * (rows - i) * 2+"* " * i)
   
# reverse
for i in range(rows):
     print(" "*i*2+"* "*(rows-i))

'''

# while loop

# num = 5

# while num >0:
#      print(num)

#      num -=1

# num = 0
# while num < 5:
#      print(num)
#      num +=1

# num =0
# while num<101:
#      num += 1

#      if num%2 != 0:
#           continue
     
#      print(num)

# function
# def greet(name):
#      print("Hello, " + name + "!")


# greet("abdul")  




# name, age = input("Enter your name and age: ").split()
# # print(f"Name: {name}")
# # print(f"Age: {age}")
# n1 =(f"Name: {name}")
# a1=(f"Age: {age}")
# print(n1)
# print(a1)

# inputs = input("Enter multiple values separated by space: ").split()
# print("You entered:", inputs)

