
import time


# def fun(x,y):
#     for i in range(x):
#         time.sleep(y)
#         print(i)

# z=threading.Thread(target=fun,args=(4,2,"threading"))
# z.start()

# class cls(Thread):

#     def run(self):
#         lst=[]

#         for i in range(1,10):
#             if i%2==0:
#                 lst.append(i)
#                 print(i)
#                 time.sleep(2)
#                 print(lst)
                

# thread1=cls()
# thread1.start()


from threading  import *
class cls(Thread):
    def __init__(self, name):  
        self.__name = name  

    def run(self):  
        print(f"{self.__name} is running.")


t1 = cls("Thread-1")
t1.start()




