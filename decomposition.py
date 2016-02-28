#! /usr/bin/env python


from __future__ import division, print_function

def decompose(n):
    """
    :type: number
    :param n: natural number
    :return: tuple of numbers
    """
    answer = []
    def search_answer (n, min):
        if n - min > min:
            answer.append(min)
            search_answer(n - min, min + 1)
        else:
            answer.append(n)
            return
    search_answer(n, 1)
    return answer

def main():
    s = raw_input('Please input number: ')
    if not s.isdigit():
        raise ValueError("Input is not the number")
    n = int(s)
    if n < 1 or n > 10**9:
        raise ValueError("Number is out of range")
    print("Output: ", end = " ")
    for char in decompose(n):
        print(char, " ", end = " ")


if __name__ == "__main__":
    main()
