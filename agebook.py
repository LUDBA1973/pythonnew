def travel_book():
        age=int(input("enter your age:"))
        ticket_price= 50

        if age < 0:
                print("invalid age")
        elif age < 18:
                ticket_price = ticket_price - ticket_price*(30/100)
        elif age > 60:
                ticket_price = ticket_price - ticket_price*(20/100)
        else:
                ticket_price = ticket_price
        

        print("Age:",age)
        print("Ticket Price:$",ticket_price)


travel_book()
