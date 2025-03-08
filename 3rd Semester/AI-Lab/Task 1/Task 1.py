# task 1 mini project dynamic  calculater

import re

def evaluate_expression(expression):
    try:
        result=eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the Dynamic Calculator!")
    print("You can perform calculations using +, -, *, /, and parentheses.")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        user_input=input("Enter your expression: ")
        
        if user_input.lower()=='exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if not re.match(r'^[0-9+\-*/(). ]+$', user_input):
            print("Invalid input. Please use numbers and operators only.")
            continue
        
        result=evaluate_expression(user_input)
    
        print("Result:", result)


main()