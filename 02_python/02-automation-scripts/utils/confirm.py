def ask_yes_no(question):
    while True:
        choice = input(f"{question} [y/N]: ").lower().strip()
        if not choice or choice == "n":
            return False
        if choice == "y":
            return True
        print("Please enter 'y' or 'n'.")
