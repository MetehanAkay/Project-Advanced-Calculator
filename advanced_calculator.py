import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.last_result = None

    def evaluate(self, expression):
        try:
            # Allow math functions and memory in eval
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            allowed_names["M"] = self.memory
            result = eval(expression, {"__builtins__": None}, allowed_names)
            self.last_result = result
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {e}"

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def show_history(self):
        return '\n'.join(self.history) if self.history else "No history yet."

def main():
    calc = Calculator()
    print("Advanced Calculator. Type 'help' for options.")
    while True:
        user_input = input("Enter expression or command: ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'help':
            print("""
Available:
- Basic operations: +, -, *, /, **, %
- Parentheses: ( )
- Math functions: sin(x), cos(x), tan(x), sqrt(x), log(x), exp(x), etc.
- Memory: M (use in expressions), M+, M-, MR, MC
- Use 'ans' for last result
- 'history' to see calculation history
- 'exit' to quit
""")
        elif user_input.lower() == 'history':
            print(calc.show_history())
        elif user_input.upper() == 'MC':
            calc.memory_clear()
            print("Memory cleared.")
        elif user_input.upper() == 'MR':
            print(f"Memory: {calc.memory_recall()}")
        elif user_input.upper().startswith('M+'):
            try:
                value = float(user_input[2:].strip()) if user_input[2:].strip() else calc.last_result or 0
                calc.memory_add(value)
                print(f"Added {value} to memory.")
            except:
                print("Invalid value for M+.")
        elif user_input.upper().startswith('M-'):
            try:
                value = float(user_input[2:].strip()) if user_input[2:].strip() else calc.last_result or 0
                calc.memory_subtract(value)
                print(f"Subtracted {value} from memory.")
            except:
                print("Invalid value for M-.")
        else:
            expr = user_input.replace('ans', str(calc.last_result) if calc.last_result is not None else '0')
            result = calc.evaluate(expr)
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
