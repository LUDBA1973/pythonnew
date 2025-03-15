books=[]
def library():
     print("\nOptions: \n1. Add Books \n2. Display Book \n3. borrow Book \n4. Return book ")
     choice = input("Enter your choice (1-4): ")

     if choice =="1":
          if books==[]:
               user=int(input("how many books you want to add:"))
               for i in range(user):
                    bk_name=input("enter book name :")
                    books.append(bk_name)
                    print(f"book {bk_name} added to the library")
                    
          else:
                bk_name=input("enter book name :")
                books.append(bk_name)
                print("book added successfully")


     elif choice=="2":
          if books==[]:
               print("No books in the library")
          else:
               for i,book in enumerate(books,1):
                    print(f"{i}:{book}")

     elif choice == "3":
          borrow_book=input("Enter the book name you want to take :")
          if borrow_book in books:
               books.remove(borrow_book)
               print(f"{borrow_book} is borrowed successfully..")
          else:
               print(f"{borrow_book} is not available in library")

     elif choice =="4":
          return_book=input("Enter the book name you want to return :")
          books.append(return_book)
          print(f"{return_book} is returned successfully..")
     else:
          print("Invalid choice .Please enter a valid option.")        
          

while True:
        print("\nOptions: \n1. Access Library \n2 Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            library()
        elif choice == "2":
            print("\nThank you for using the Library System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")