#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    #addition = a + b
    print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))

    #subtraction = a - b
    print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))

    #multiplication = a * b
    print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))

    #division = a / b
    print("{:d} / {:d} = {:.0f}".format(a, b, calc.div(a, b)))
