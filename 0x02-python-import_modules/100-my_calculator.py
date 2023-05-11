#!/usr/bin/python3
import calculator_1
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.sub(a, b)
    elif operator == "*":
        result = calculator_1.mul(a, b)
    elif operator == "/":
        result = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")
