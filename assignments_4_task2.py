#! /usr/bin/env python


from __future__ import division, print_function
from itertools import izip


def p_distance(str1, str2):
    """ Calculates the p-distance of two aligned sequences, ignoring positions with gaps
     :type str1:str
     :param str1:
     :type str2: str
     :param str2:
     :return:
     """
    if len(str1) != len(str2):
        raise ValueError("Sequences of unequal length")
    mismatches = 0
    for element1, element2 in izip(str1, str2):
        if element1 == "-" or element2 == "-":
            mismatches -= 1
            continue
        if element1 != element2:
            mismatches += 1
        return mismatches

print(p_distance('aaaa--bba','aaaaaa-bb'))
