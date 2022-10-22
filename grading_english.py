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
    for grade in grades:
        residual = 5 - grade % 5
        if grade >= 38 and residual < 3:
            round = grade + residual
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
