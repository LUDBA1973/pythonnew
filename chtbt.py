def chatbot():
    print("Welcome to the chatbot!")
    name = input("What is your name? ")
    print(f"Hello {name}, I'm happy to chat with you!")

    while True:
        user_input=input("user:")
        if user_input.lower() == "exit" or user_input.lower()=="goodbye" or user_input.lower()=="bye":
            print("Goodbye, it was nice chatting with you Have a great day!")
            break
        elif user_input.lower() == "hello" or user_input.lower() == "hi":
            print("Hi there! How can i assist you?")
        elif user_input.lower()== "how are you?":
            print("I'm just a program, but I'm here to help")
        elif  user_input.lower()=="what is your name" or "name" in user_input or user_input.lower()=="who are you":
            print("I'm a chatbot, your virtual assistant")
        else:
            print("Sorry , I didn't understand that.")


chatbot()               
