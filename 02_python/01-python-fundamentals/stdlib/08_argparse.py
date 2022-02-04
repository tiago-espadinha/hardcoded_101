"""
Demonstrates argparse in Python.
Covers: build a CLI with subcommands, flags, and help text
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="A sample CLI tool.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Increase output verbosity")
    
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # greet subcommand
    greet_parser = subparsers.add_parser("greet", help="Greet a person")
    greet_parser.add_argument("name", help="Name of the person to greet")
    greet_parser.add_argument("--formal", action="store_true", help="Use formal greeting")

    # calc subcommand
    calc_parser = subparsers.add_parser("calc", help="Perform simple arithmetic")
    calc_parser.add_argument("x", type=int, help="First number")
    calc_parser.add_argument("y", type=int, help="Second number")
    calc_parser.add_argument("--op", choices=["add", "sub", "mul"], default="add", help="Operation")

    args = parser.parse_args()

    if args.verbose:
        print(f"Executing command: {args.command}")

    if args.command == "greet":
        if args.formal:
            print(f"Good day, {args.name}.")
        else:
            print(f"Hi, {args.name}!")
    
    elif args.command == "calc":
        if args.op == "add":
            print(f"Result: {args.x + args.y}")
        elif args.op == "sub":
            print(f"Result: {args.x - args.y}")
        elif args.op == "mul":
            print(f"Result: {args.x * args.y}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
