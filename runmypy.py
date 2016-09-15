#!/usr/bin/env python3
import os 

while True:
    number = input()
    print()
    if not number:
        continue
    filename = "annotations{:0>2}.py".format(number)

    value = 1
    try:
        value = os.system("mypy --strict-optional {}".format(filename))
    except Exception as e:
        print(type(e).__name__ + ": ")
        print(e)
    
    if not value:
        print("No errors found!")
    
    print()
