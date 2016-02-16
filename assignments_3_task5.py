#! /usr/bin/env python

from __future__ import division, print_function
import operator

def calculate(numbers, operations):
    """
    This function use operations from (operations) to numbers from (numbers)
    :param numbers: List of the numbers
    :param operations: List of the operations
    (supported only "+" and "-" operations)
    :return: Result of calculations
    """
    if len(numbers) != len(operations) + 1:
        raise ValueError("Errors in given data")
    operation_dict = {
        "+": operator.add,
        "-": operator.sub
    }
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, oper in zip(numbers_iterator, operations):
        oper_func = operation_dict.get(oper)
        if not oper_func:
            raise ValueError("Operation {} is not supported".format(oper))
        acc = oper_func(acc, num)
    return acc

def evaluate_string(string):
    if len(string) == 0:
        raise ValueError("Empty data")
    string_iterator = iter(string)
    open_bra = 0
    close_bra = 0
    numbers = []
    operations = []
    s = []                              # next symbol in string
    last_elem = []                      # the last used symbol in string
    for elem in string_iterator:
        if elem == ' ':
            last_elem = elem
            continue
        elif elem == '.':
            if next(string_iterator).isdigit():
                raise ValueError("The programm does not support float numbers")
            else:
                raise ValueError("Invalid data format")
        elif elem == '(':
            open_bra += 1
            continue
        elif elem == ')':
            close_bra += 1
            if close_bra > open_bra:
                raise ValueError("Invalid brackets")
            continue
        elif elem.isdigit():
            s.append(elem)
            continue
        elif elem == '+' or elem == '-':
            if s == []:
                raise ValueError("Too many operations")
            operations.append(elem)
            numbers.append(int(''.join(s)))
            s = []
            continue
        raise ValueError("Operation {} is not supported".format(elem))
    if s != []:
        numbers.append(int("".join(s)))
    if open_bra != close_bra:
        raise ValueError("Invalid brackets")
    return calculate(numbers, operations)
print (evaluate_string("1 +2 (*-2-1) +5"))








