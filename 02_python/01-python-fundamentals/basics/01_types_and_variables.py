"""
Demonstrates Python types and variables.
Covers: int, float, str, bool, None, type(), isinstance()
"""

def main():
    # Types
    x = 42          # int
    y = 3.14        # float
    name = "Alice"  # str
    is_active = True # bool
    data = None     # None

    print(f"x: {x}, type: {type(x)}")
    print(f"y: {y}, type: {type(y)}")
    print(f"name: {name}, type: {type(name)}")
    print(f"is_active: {is_active}, type: {type(is_active)}")
    print(f"data: {data}, type: {type(data)}")

    # Exercise: Ask for name and age, print formatted greetings
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    
    # % formatting
    print("Hello, %s! You are %s years old." % (user_name, user_age))
    
    # .format()
    print("Hello, {}! You are {} years old.".format(user_name, user_age))
    
    # f-strings
    print(f"Hello, {user_name}! You are {user_age} years old.")

if __name__ == "__main__":
    main()
