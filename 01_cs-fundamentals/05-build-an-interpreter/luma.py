import sys
from lexer import Lexer, LexError
from parser import Parser, ParseError
from interpreter import Interpreter, LumaRuntimeError

def run(source: str, interpreter: Interpreter):
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        statements = parser.parse()
        
        interpreter.interpret([s for s in statements if s is not None])
    except LexError as e:
        print(e)
    except ParseError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")

def run_file(path: str):
    interpreter = Interpreter()
    try:
        with open(path, 'r') as f:
            run(f.read(), interpreter)
    except FileNotFoundError:
        print(f"Error: Could not find file {path}")

def run_repl():
    interpreter = Interpreter()
    print("Luma 0.1.0 REPL")
    print("Press Ctrl+C to exit")
    
    buffer = ""
    while True:
        try:
            prompt = ">> " if not buffer else ".. "
            line = input(prompt)
            buffer += line + "\n"
            
            # Simple check for balanced braces
            if buffer.count("{") <= buffer.count("}"):
                if buffer.strip():
                    run(buffer, interpreter)
                buffer = ""
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            buffer = ""
            continue

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python luma.py [script.luma]")
        sys.exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_repl()
