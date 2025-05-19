# Advanced Calculator

Advanced Calculator is a command-line calculator written in Python that supports advanced mathematical operations and memory functions.

## Features

- **Basic operations:** Addition, subtraction, multiplication, division, exponentiation, modulo (`+`, `-`, `*`, `/`, `**`, `%`)
- **Parentheses:** For complex expressions
- **Math functions:** `sin(x)`, `cos(x)`, `tan(x)`, `sqrt(x)`, `log(x)`, `exp(x)`, and more
- **Memory functions:**
  - `M` : Use the value stored in memory in expressions
  - `M+` : Add to memory
  - `M-` : Subtract from memory
  - `MR` : Recall memory value
  - `MC` : Clear memory
- **Last result:** Use `ans` to refer to the last calculated result
- **History:** View calculation history

## Usage

1. Make sure you have Python 3 installed.
2. Run the following command in your terminal:

   ```sh
   python advanced_calculator.py
   ```

3. Enter mathematical expressions or use the following commands:

   - `help` : Show usage instructions
   - `history` : Show calculation history
   - `exit` : Quit the program

## Example

```
Enter expression or command: 2 + 3 * 4
Result: 14

Enter expression or command: sin(0)
Result: 0.0

Enter expression or command: M+ 10
Added 10.0 to memory.

Enter expression or command: M
Result: 10.0

Enter expression or command: ans * 2
Result: 20.0

Enter expression or command: history
2 + 3 * 4 = 14
sin(0) = 0.0
M = 10.0
ans * 2 = 20.0
```

## Contribution & License

This project is for educational purposes. Feel free to contribute by opening a pull request.
