"""
Demonstrates control flow in Python.
Covers: if/elif/else, ternary expression, match-case (Python 3.10)
"""

def fizz_buzz(n):
    # Ternary expression
    # result = "Fizz" if n % 3 == 0 else ""
    
    # Match-case (Python 3.10)
    match (n % 3 == 0, n % 5 == 0):
        case (True, True):
            return "FizzBuzz"
        case (True, False):
            return "Fizz"
        case (False, True):
            return "Buzz"
        case _:
            return str(n)

def main():
    print("FizzBuzz for 1-100:")
    for i in range(1, 101):
        # Standard if/elif/else
        if i % 15 == 0:
            val = "FizzBuzz"
        elif i % 3 == 0:
            val = "Fizz"
        elif i % 5 == 0:
            val = "Buzz"
        else:
            val = str(i)
        
        # Verify with match-case
        assert val == fizz_buzz(i)
        
        print(val, end=" ")
    print()

if __name__ == "__main__":
    main()
