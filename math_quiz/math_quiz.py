import random


def generate_random_int(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    @param min_value: The minimum integer value.
    @param max_value:  The maximum integer value.
    @return: A randomly generated integer within the given range.
    """
    return random.randint(min_value, max_value)


def operator_choice():
    """
    Randomly select a mathematical operator from +,-,*.
    @return: A randomly chosen operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def solve_the_math_problem(arg1, agr2, operator):
    """
    Create a math problem as a string and compute the correct answer based on the given operator.
    @param arg1: The first argument in the math problem.
    @param agr2: The second argument in the math problem.
    @param operator: The chosen operator for the math problem ('+', '-', '*').
    @return: A tuple containing the math problem as a string and the correct answer as an integer.
    """
    problem = f"{arg1} {operator} {agr2}"
    if operator == '+':
        solution = arg1 + agr2
    elif operator == '-':
        solution = arg1 - agr2
    else:
        solution = arg1 * agr2
    return problem, solution


def math_quiz():
    """
        This is the main function to run the math quiz game.

        The game will ask the user to solve generated math problems. For each correct answer,
        the user earns a point. The total score is displayed at the end of the game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        arg1 = generate_random_int(1, 10)  # generate arg1
        arg2 = generate_random_int(1, 5.5)  # generate arg2
        operator = operator_choice()  # randomly choose the operator

        # generate the math problem and get the correct answer
        problem, correct_ans = solve_the_math_problem(arg1, arg2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            # verify if the ans provided by the user is correct
            if user_answer == correct_ans:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_ans}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle non-integer input
    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
