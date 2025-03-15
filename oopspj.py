from abc import ABC,abstractmethod

class football(ABC):

    @abstractmethod
    def add_player():
         pass
    @abstractmethod
    def display_player():
         pass

player = []
class transfers(football):


    def add_player(self):
            count=int(input("howmanyplayer u want to add:"))
            if count==1:
                name=input("name:")
                age=int(input("age:"))
                team=input("tm:")

                player.append(f"name:{name},age:{age},team:{team}")
                print("player added succesfully")
                print("-"*25)
            
            elif count>1:
                 for i in range(count):
                      name=input("name:")
                      age=int(input("age:"))
                      team=input("tm:")
                      player.append(f"name:{name},age:{age},team:{team}")
                 print("players added succesfully")
                 print("-"*25)
            else:
                        print("invalid input")
                        print("-"*25)
        

         
    def display_player(self):
         if len(player) == 0:
              print("No players in the list")
         else:
              for i in player:
                   print(i)
                
    
    def remove_players(self):
        usr = input("Enter player name to remove: ")

        if usr in player:
             player.remove(usr)
            
            
obj=transfers()


while True:
        print("Football Transfers Market")

        print("What do you want to do? \n1.add teams \n2.display teams \n3.exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
             obj.add_club()
        elif choice ==2:
             obj.display_club()
        elif choice==3:
             obj.add_player()
        elif choice==4:
             obj.display_player()
        elif choice==5:
             obj.remove_players()


       