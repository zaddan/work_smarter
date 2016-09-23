import os
import copy
out_line = []
temp_file_to_store_history = os.path.expanduser('~/tempo') 

with open(temp_file_to_store_history, "r") as f:
    for index,line in enumerate(f):
        output_line = [] 
        new_line = line.rstrip().replace(',', ' ').replace('/',' ').replace(';', ' ').split(' ') 
        for el in new_line:
            if len(el)> 0:
                output_line.append(el)
        output_line[0] = str(index-20)
        out_line.append("  ".join(output_line))

for el in out_line:
    print el
