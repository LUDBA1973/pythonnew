class Car:
    name = "bmw"  
    model = "x5"
    
    def drive(self):
        print(f"Car {self.name},{self.model} is driving in {self.year}") 

    def ferrari(self):
        self.drive()  
    def __init__(self, x):
        self.year = x  

obj = Car("2020")


obj.ferrari()
