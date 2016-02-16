#! /usr/bin/env python

def my_filter(fn, sequence, **kwargs):
    '''
    returns the list of elements for which the result of function fn is True
    :param fn: name of the function
    :param sequence: list of elements of the function fn
    :param kwargs: parameters of function fn
    :return: list of elements
    '''

    result = []
    for elem in sequence:
        if bool(fn(elem, **kwargs)):
            result.append(elem)
    return result

# Task 5

def evaluate_string(operations):
    '''
    calculates the result of substitution and addition of integer numbers
    :param operations: string of numbers and "+" and "-" signs
    :return: result of arithmetical expressions
    '''
    data = []
    if not isinstance(data, str):
        raise ValueError ("Please enter the string")
    operation_dict = {
        "+": operator.add
        "-": operator.sub
    }
