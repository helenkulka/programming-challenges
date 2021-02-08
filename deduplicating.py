#! /usr/bin/python3
import sys
import collections
from scipy import special

files_raw=[]
files_sorted =[]
num_files = 0
unique = 0
collisions = 0
s_list = []

for line in sys.stdin:
    line = line.rstrip()
    if line.isdigit():
        num_files = int(line)
        if num_files == 0:
            for i in s_list:
                print(i)
            s_list = []
            sys.exit(0)
        files_raw=[]
        files_sorted=[]
    else:
        files_raw.append(line)
        files_sorted.append(''.join(sorted(line)))

    if (len(files_raw) == num_files):
        unique = len(set(files_raw))

        col_list = sum([count for item, count in collections.Counter(files_sorted).items() if count > 1])
        collisions = special.comb(col_list,2) - (len(files_raw) - unique)

        s = str(unique) + " " + str(int(collisions))
        s_list.append(s)