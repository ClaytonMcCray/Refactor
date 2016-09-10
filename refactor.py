#!/usr/bin/env python3
from re import sub
import sys

file_name = sys.argv[1] 
with open('backup.txt', 'a') as backup:
    with open(file_name, 'r') as original:
        for line in original:
            backup.write(line)

