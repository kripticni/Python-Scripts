#!/usr/bin/env python
import sys

while True:
    buff = input()
    print("".join(sys.argv[1:]) + buff)
