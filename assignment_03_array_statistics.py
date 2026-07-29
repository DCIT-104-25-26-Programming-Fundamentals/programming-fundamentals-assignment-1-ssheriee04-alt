# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)

def find_maximum(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

def main():
    try:
        count = int(input("How many numbers? "))
        
        # Validate that count is a positive integer
        if count <= 0:
            print("Error: Number of elements must be a positive integer.")
            return
        
        numbers = []
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            # Format as integer if it's a whole number for clean display
            if num.is_integer():
                num = int(num)
            numbers.append(num)
            
        print("\nResults:")
        print(f"Sum:      {calculate_sum(numbers)}")
        print(f"Average:  {calculate_average(numbers)}")
        print(f"Maximum:  {find_maximum(numbers)}")
        print(f"Minimum:  {find_minimum(numbers)}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()


