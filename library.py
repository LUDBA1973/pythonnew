def categorize_input():
    int_list = []
    float_set = set()
    string_dict = {}
    
    while True:
        user_input = input("Enter a value (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            if '.' in user_input:
                value = float(user_input)
                float_set.add(value)
            else:
                value = int(user_input)
                int_list.append(value)
        except ValueError:
            string_dict[user_input] = None   
    if not int_list and not float_set and not string_dict:
        print("No valid data entered.")
    else:
        print("\nCategorized Data:")
        print(f"Integers: {int_list}")
        print(f"Floats: {float_set}")
        print(f"Strings: {string_dict}")
        

categorize_input()
