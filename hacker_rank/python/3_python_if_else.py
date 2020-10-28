#!/bin/python3
# https://www.hackerrank.com/challenges/py-if-else/problem
import math
import os
import random
import re
import sys

def run(n):
    if n %2 == 1:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    run(n)