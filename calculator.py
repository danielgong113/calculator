#!/usr/bin/env python

def add(num_1, num_2):
    """
    :param num_1: left operand
    :param num_2: right operand
    :return: adds right operand to the left operand and returns sum
    """
    print("[Operator] Addition")
    # TODO
    pass

def substract(num_1, num_2):
    """
    :param num_1: left operand
    :param num_2: right operand
    :return: subtracts right operand from the left operand and returns differences
    """
    print("[Operator] Substraction")
    # TODO
    pass

def multiply(num_1, num_2):
    """
    :param num_1: left operand
    :param num_2: right operand
    :return: multiplies right operand with the left operand
    """
    print("[Operator] Multiplication")
    # TODO
    pass

def divid(num_1, num_2):
    """
    :param num_1: left operand
    :param num_2: right operand
    :return: divides left operand with the right operand
    """
    print("[Operator] Division")
    # TODO
    pass

def exponent(base, power):
    """
    :param num_1: left operand
    :param num_2: right operand
    :return: performs exponential (power) calculation on operators and assign value to the left operand
    """
    print("[Operator] Exponent")
    # TODO
    pass


def main():
    print("[main] Start calculator")

    # num_1 + num_2
    add(num_1, num_2)

    # num_1 + num_2
    substract(num_1, num_2)

    # num_1 * num_2
    multiply(num_1, num_2)

    # num_1 / num_2 (be careful of the case that divides by zero)
    divid(num_1, num_2)

    # num_1 ^ num_2
    exponent(num_1, num_2)


if __name__ == '__main__':
    print "Initialize calculator..."
    main()