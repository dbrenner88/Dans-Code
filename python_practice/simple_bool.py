class BooleanProcessor:
    def __init__(self):
        self.number = None
        self.operation = None

    def ask_for_number(self):
        for i in range(10):
            try: 
                self.number = int(input("Enter a number: "))
                break
            except ValueError:
                print(f"Not a number. Please enter a valid number. After 10 tries the program will exit. It is currently the {i+1} try.")
        else:
            print("Exceeded the number of tries. Exiting.")
            exit(1)

    def get_operation(self):
        valid_inputs = ["yes", "no"]
        for i in range(10):
            try:
                self.operation = input("Do you want to add 10 to the number? (yes/no): ").lower()
                if self.operation in valid_inputs:
                    break
                else: raise ValueError
            except ValueError:
                print(f"Not a valid entry, after 10 tries the program will exit. It is currently the {i+1} try.")    
        else:
            print("Invalid operation. Exiting the program.")
            exit(1)
            
    def execute_add_10(self):
        if self.operation == "yes":
            result = self.number + 10
            print("Number after adding 10:", result)
        elif self.operation == "no":
            print("All good, goodbye!")
        else:
            print("Invalid operation. Exiting the program.")

# Example usage
boolean_processor = BooleanProcessor()
boolean_processor.ask_for_number()
boolean_processor.get_operation()
boolean_processor.execute_add_10()
