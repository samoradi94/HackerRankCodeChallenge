#!/bin/python3

import os



def camelcase(s):
    count = 0
    for a in s:
        if a.isupper():
            count+=1
    print(count + 1)



if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'result.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
