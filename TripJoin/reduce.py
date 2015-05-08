#!/usr/bin/python

import sys

current_key = None 
current_file_flag = None

for line in sys.stdin:
    values = line.strip().split(',')
    keys = values[:4] 
    file_flag = values[4]
    others = values[5:] 

    if file_flag == current_file_flag:  
        # to avoid repeats (there are some in the wednesday files)
        continue
    else: 
        current_file_flag = file_flag 

    if keys == current_key:
        value_list = value_list + others        # append value
    else:
        if current_key: 
            print ''.join([','.join(current_key), ",", ','.join(value_list)]) 

        current_key = keys
        current_file_flag = file_flag
        value_list = others

print ''.join([','.join(current_key), ",", ','.join(value_list)]) 
