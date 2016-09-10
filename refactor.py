#!/usr/bin/env python3
from re import sub
import sys

try:
    original_file_name = sys.argv[1] 
    regex_pattern = sys.argv[2]
    new_phrase = sys.argv[3]
except IndexError:
    print('Error: must pass arguments \nfile_name old_phrase new_phrase')
    sys.exit()
with open('backup.txt', 'w') as backup:  # creates the backup file
    # below, we begin to write out the backup file
    with open(original_file_name, 'r') as original:
        for line in original:
            backup.write(line)

# below rewrites the original file from backup.txt
# but using the sub method to replace given word
with open('backup.txt', 'r') as backup:  # 'r' protects the file from being deleted
    with open(original_file_name, 'w') as rewrite:  # 'w' ensures that the file will be overwritten
        for line in backup:
            new_line = sub(regex_pattern, new_phrase, line)
            rewrite.write(new_line)

