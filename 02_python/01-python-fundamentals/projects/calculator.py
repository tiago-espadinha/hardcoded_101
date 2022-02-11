"""
CLI calculator with history.
Features: +, -, *, /, **, sqrt, history (last 10 operations)
Input loop with error handling for invalid expressions
"""
import math
from collections import deque

def main():
    history = deque(maxlen=10)
    print("Python CLI Calculator (type 'exit' or 'history' to use)")
    
    while True:
        try:
            expr = input("calc > ").strip().lower()
            if expr == 'exit':
                break
            if expr == 'history':
                print(f"History: {list(history)}")
                continue
            
            # Simple eval (security risk in real apps, but ok for fundamentals demo)
            # Restricting allowed names for a bit more safety
            allowed_names = {"sqrt": math.sqrt, "__builtins__": {}}
            result = eval(expr, {"__builtins__": {}}, allowed_names)
            
            print(f"Result: {result}")
            history.append(f"{expr} = {result}")
            
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print(f"Error: Invalid expression ({e})")

if __name__ == "__main__":
    main()
