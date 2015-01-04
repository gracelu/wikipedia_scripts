from collections import defaultdict
import re

years= defaultdict(int)
journals= defaultdict(int)

with open("test_pagename_journal_date3.txt") as infile:
    for line in infile:
        colon_split= line.split(":")
        line_split= colon_split[-1].split()
        if (len(line_split) >= 2):
            journal= line_split[-2]
            year= line_split[-1]
            years[year] = years[year] + 1
            journals[journal] = journals[journal] + 1

for key,value in sorted(journals.items()):
    # if re.search(r'[12]\d{3}', key) and int(key) < 2016 and int(key) > 1600:
    print key,":", value