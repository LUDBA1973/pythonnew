total_tickets = 100 


while total_tickets > 0:
        
            requested_tickets = int(input("Enter the number of tickets you'd like to buy: "))

            if requested_tickets <= 0:
                print("Please enter a positive number.")

            elif requested_tickets > total_tickets:
                print(f"Sorry, only {total_tickets} tickets are available. Try again.")
                
            else:
                total_tickets -= requested_tickets
                print(f"Booking confirmed! You have purchased {requested_tickets} ticket(s).")
                print(f"{total_tickets} ticket(s) remaining.")

  
print("All tickets are sold out! Thank you for your interest.")

