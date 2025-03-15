# oops
#OOPS CONCEPT: data,object,inheritence,encapsulation,abstraction,polymorphism

# Class
# blueprint for creating a object
# class car:
#     name="bmw"
#     model="x5"


#     def __init__(self,x):
#         self.year=x
#         self.age=44

#     def drive(self):
#         print(f"car is driving in{self.year},{obj.name}{self.age}")
     
#     def ferrari(self):
#         self.drive()

    

# obj=car("2020")
# obj.ferrari()

# object
# instance of a class
# runtime entity it creates when u run it
# created using class as a template and has unique data

# inheritence
# parent class
# child class
# parent class is called super class
# child class is called subclass
# child class inherits all the properties of parent class
# child class can also add new properties or override the properties of parent class
# Inheritance is a mechanism in object-oriented programming (OOP) where one class can inherit the properties and methods of another class.
# The child class inherits all the attributes and methods of the parent class and can also add new attributes
# and methods or override the ones inherited from the parent class.
# Inheritance is used to create a new class that is a modified version of an existing class.

# single inheritence
'''
class x:
    def y(self):
        print("hello world")

class z(x):
    def k(self):
        print("gggg")

abdul = z()   

abdul.y()
abdul.k()
'''
'''
class a:
     
     def z(self):
        print("hello",d().name)

class b(a):
     def y(self):
        print("world")

class c(a):
    def k(self):
        print("gg")

class d(b,c):
    name="abdul"
    def m(self):
        print("wp")

user = d()
print(user.name)
user.z()
user.y()
user.k()
user.m()
'''


# polymorphism
# polymorphism is the ability of an object to take on multiple forms
# it can be achieved through method overloading or method overriding

# class mycls:
#   method overloading    
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
    
# cls=mycls()

# print(cls.add(2))


# encapsulation
# encapsulation is the concept of bundling data and methods that operate on that data within a singl
# class or object
# public,private(__),protected(_)

# class employee:
#     def __init__(self):
#         self.__name="abdul"
#         self.age=20      
#     def gg(self):
#         print(f"hello i am {self.name} and i am {self.age} years old")


     

# emp=employee()
# emp.gg()

        

# Abstraction
# abstraction is the concept of showing only necessary information to the outside world while hiding the internal details
# it is a concept of exposing only necessary information to the outside world while hiding the internal details

from abc import ABC,abstractmethod

class lib(ABC):
  

        @abstractmethod
        def add(self):
            pass

        @abstractmethod
        def sub(self):
            pass


class cly(lib):

        def __init__(self,x):
            #  super().__init__()
            self.total=x
     
        def add(self):
            user = int(input("enter number"))
            a=user+10
            self.total.append(a)
            print(self.total)

        def sub(self):
            user = int(input("enter number"))
            print(user-10)


total =[]
obj=cly(total) 

user1 = input("enter choice 1/2:")
while True:
    if user1 == "1":
            obj.add()
    elif user1 == "2":
        obj.sub()