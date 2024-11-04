import unittest
from math_quiz import generate_random_int, operator_choice, solve_the_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_choice(self):
        # Check if the operator_choice function only returns '+', '-', or '*'
        allowed_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test multiple times to ensure randomness
            chosen_operator = operator_choice()
            self.assertIn(chosen_operator, allowed_operators)

    def test_solve_the_math_problem(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 5, '*', '4 * 5', 20),
            (8, 0, '+', '8 + 0', 8),  # Edge case with zero
            (0, 8, '*', '0 * 8', 0),  # Multiplying by zero
            (8, 8, '-', '8 - 8', 0),  # Result zero
            (8, 4, '*', '8 * 4', 32),  # Multiplication check
            (10, 1, '-', '10 - 1', 9),  # Subtraction check
            (1, 10, '-', '1 - 10', -9),  # Subtraction check negative result
            (-1, -10, '-', '-1 - -10', 9),  # Subtraction of negative numbers
            (-1, -10, '+', '-1 + -10', -11),  # Addition of negative numbers
            (-1, -10, '*', '-1 * -10', 10)  # multiplication of negative numbers
        ]

        for arg1, arg2, operator, expected_problem, expected_answer in test_cases:
            problem, solution = solve_the_math_problem(arg1, arg2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(solution, expected_answer)


if __name__ == "__main__":
    unittest.main()
