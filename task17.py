class NoMultiplesFoundError(Exception):
    pass
def run():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))

        if numbers==[]:
            raise ValueError("List ios empty")
        else:
            multiples=[n for n in numbers if n % 3 ==0 and n % 5==0]

            if multiples==[]:
                raise NoMultiplesFoundError("No multiples of 3 and 5 found.")
            
            else:
                print(f"Multiples of 3 and 5:{multiples}")
                addlist=[numbers[i]+numbers[i+2] if i+2<len(numbers) else numbers[i] for i in range(len(numbers))]
                print(f"newlist:{addlist}")

    except ValueError as x:
        print(f"Error: Invalid input. {x}")

    except NoMultiplesFoundError as y:
        print(f"Error: {y}")

run()