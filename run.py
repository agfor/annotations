#!/usr/bin/env python3
while True:
    number = input()
    print()
    filename = "annotations{:0>2}.py".format(number)
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        continue

    try:
        exec(content)
    except Exception as e:
        print(type(e).__name__ + ": ")
        print(e)
    print()
