
# while True:
#     try:
#         x= int(input("enter no:"))

#     except ValueError as v:
#         print(f"Error:{v}")

#     else:
#         if x>0:
#             print("positive")
#         elif x<0:
#             print("negative")

#     finally:
#         print("starting new session...")

   
import random

num = random.randint(1, 100)  # Random number between 1 and 100
print(num)

num = random.uniform(1.5, 10.5)  # Random float between 1.5 and 10.5
print(num)

num = random.random()  # Random float between 0 and 1
print(num)


num = random.randrange(0, 100, 5)  # Random number from 0 to 100 in steps of 5
print(num)

items = ['apple', 'banana', 'cherry']
choices = random.choices(items, k=2)
print(choices)

nums = random.sample(range(1, 100), 5)  # Get 5 unique random numbers from 1 to 100
print(nums)

nums = random.choices(range(1, 100), k=5)  # Get 5 random numbers with possible duplicates
print(nums)



items = ['apple', 'banana', 'cherry']
choices = random.sample(items, 2)  # Pick 2 unique items
print(choices)

choices = random.choices(items, k=2)  # Pick 2 items, duplicates possible
print(choices)

