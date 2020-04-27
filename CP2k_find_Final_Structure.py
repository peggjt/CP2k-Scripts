'''
The script extracts the final ionic coordinates from the '.xyz' file
and prints them to a file named final_structure.xyz.

To use this script:

    python CP2k_find_Final_Structure.py

Author: James T. Pegg

'''

final_structure = 0
with open('POSXYZ.xyz', 'r') as f:
    for n, line in enumerate(f):
        if 'i = ' in line:
            final_structure = n

with open('POSXYZ.xyz', 'r') as posxyz, open('final_structure.xyz', 'w') as Final_Structure:
    for n, line in enumerate(posxyz):
        if (n >= final_structure):
            Final_Structure.write(line)
