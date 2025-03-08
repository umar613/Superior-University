# task 2 mini project 1 fizz buzz game
# import random

# def fizz_buzz_game():
#     print("Welcome to the Fizz Buzz Game!")
#     print("The computer will generate a random number between 1 and 100.")
#     print("You need to respond with 'Fizz', 'Buzz', 'Fizz Buzz', or the number itself.")
#     print("Type 'exit' to quit the game.")
    
#     while True:
#         number=random.randint(1, 100)
#         print(f"\nComputer's number: {number}")
        
#         user_input=input("Your answer: ").strip()
        
#         if user_input.lower()=='exit':
#             print("Thanks for playing! Goodbye!")
#             break
        
#         if number % 3==0 and number % 5==0:
#             correct_answer = "Fizz Buzz"
#         elif number % 3==0:
#             correct_answer="Fizz"
#         elif number % 5==0:
#             correct_answer="Buzz"
#         else:
#             correct_answer=str(number)

#         if user_input==correct_answer:
#             print("Correct!")
#         else:
#             print(f"Wrong! The correct answer was: {correct_answer}")

# fizz_buzz_game()

# mini project 2 movie budget
movies=[
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def calculate_average_budget(movies):
    total_budget=sum(budget for _, budget in movies)
    average_budget=total_budget / len(movies)
    return average_budget

def find_high_budget_movies(movies, average_budget):
    high_budget_movies=[]
    for movie, budget in movies:
        if budget > average_budget:
            high_budget_movies.append((movie, budget, budget - average_budget))
    return high_budget_movies

def main():

    average_budget=calculate_average_budget(movies)
    print(f"The average budget of the movies is: ${average_budget:,.2f}")

    high_budget_movies=find_high_budget_movies(movies, average_budget)
    
    if high_budget_movies:
        print("\nMovies with budgets higher than the average:")
        for movie, budget, difference in high_budget_movies:
            print(f"{movie}: ${budget:,.2f} (Higher than average by: ${difference:,.2f})")
    else:
        print("No movies have a budget higher than the average.")

    count_high_budget_movies=len(high_budget_movies)
    print(f"\nNumber of movies that spent more than the average: {count_high_budget_movies}")

    num_movies_to_add=int(input("\nHow many movies would you like to add? "))
    
    for _ in range(num_movies_to_add):
        movie_name=input("Enter the movie name: ")
        movie_budget=int(input("Enter the movie budget: "))
        movies.append((movie_name, movie_budget))

    average_budget=calculate_average_budget(movies)
    print(f"\nThe new average budget of the movies is: ${average_budget:,.2f}")

    high_budget_movies=find_high_budget_movies(movies, average_budget)
    
    if high_budget_movies:
        print("\nMovies with budgets higher than the new average:")
        for movie, budget, difference in high_budget_movies:
            print(f"{movie}: ${budget:,.2f} (Higher than average by: ${difference:,.2f})")
    else:
        print("No movies have a budget higher than the new average.")

    count_high_budget_movies=len(high_budget_movies)
    print(f"\nNumber of movies that spent more than the new average: {count_high_budget_movies}")

main()