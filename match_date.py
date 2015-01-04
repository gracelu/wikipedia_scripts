import re

with open("pagetitle_journal.txt") as infile:
    for line in infile:
        year= re.search(r'(?<=archivedate=)[^\|]+', line)
       
        if year:
            print year.group(0)
            ayear=re.search(r'\d{4}-\d{2}-\d{2}', year.group(0).lstrip().rstrip())
            if ayear:
                print ayear.group(0)[:4]
            else:
                print year.group(0).lstrip().rstrip()[-4:]