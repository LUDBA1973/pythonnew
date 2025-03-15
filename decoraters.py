# decoraters 
'''
def upper(x):

    def pr():
        data=x()
        return data.upper()
    
    return pr

def split(y):

    def gg():
        data= y()
        return data.split()
    
    return gg



@split
@upper #this fun will execute first
def myfun():
    return"jogo bonito"


print(myfun())
'''
# def fun(*gg):
#     return "helllo " + str(gg)


# rang=int(input("enter no :"))

# names=[]
# for i in range(rang):
#     name=input("enter name:")
#     names.append(name)

# print(fun(names))

# without usung self
class b:
    @staticmethod
    def add():
        return 5+5
    
obj=b()
print(obj.add())