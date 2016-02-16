/usr/bin/python2.7 /home/katrin8

'''
Lesson 5 code


'''
from _future_ import division, print print_function

# Task 2
def my_max(*args):

    if len(args) == 1:
        sequence = args[0]
        if not isinstance(sequence, (tuple, list)):
            raise VAlueError("Recieved one arguments that is not of"
                             "type Union (tuple, list)")
        current_max =
        for element in sequence:
            if not isinstance(element, int):
                raise ValueError("")
            if current_max < element:
                current_max = element
        return current_max
    sequence = args[0]
    for element in sequence:
        if not isinstance(element, int):
            raise ValueError("")
        if current_max < element:
            current max = element
        return current_max


def my_max(*args):
    if not args:
        raise ValueError("No agruments passed")
    def find_max(sequence):
        if not isinstance(sequence, (tuple, list)):
            raise VAlueError("Recieved one arguments that is not of"
                             "type Union (tuple, list)")


        if len(args) == 1:
        sequence = args[0]

        current_max =
        for element in sequence:
            if not isinstance(element, int):
                raise ValueError("")
            if current_max < element:
                current_max = element
        return current_max
    sequence = args[0]
    for element in sequence:
        if not isinstance(element, int):
            raise ValueError("")
        if current_max < element:
            current max = element
        return current_max

# Task 2.1
def my_max(*args):
    if not args:
        raise ValueError("No agruments passed")


# Task 3.
def my_map(fn, elements, **kwargs):
    result = []
    for element in elements:
        result.append(fn(element, **kwargs))
    return result

# Task 4
def calculate(numbers,operations):
    if len(numbers) != len(operations)+1:
        raise ValueError("msg")
    operation_dict = {
        "+": operator.add,
        "*": operator.mul,
        "/": operaqtor.div,
    }
    numbers_iterator = iter(numbers)
    acc = next(numbers_iterator)
    for num, operation in zip(numbers_iterator, operations):
       oper_func = operation_dict.get(oper)
       if not oper_func:
           raise ValueError ("Operation {} is not supported".format(oper))
       acc = oper_func(acc, num)
    return acc


