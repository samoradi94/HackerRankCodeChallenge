#!/bin/python3

import math
import os
import random
import re
import sys

'''
4
73
67
38
33
'''


def grading_students(grades):
    round = 0
    for grade in grades:
        residual = 5 - grade % 5
        if grade >= 38:
            if residual < 3:
                round = grade + residual
            elif residual >= 3:
                round = grade
        else:
            round = grade
        print(round)


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    grading_students(grades)
