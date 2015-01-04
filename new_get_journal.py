import re

title= ""
journal= ""

with open("pagetitle_journal.txt") as infile:
    for line in infile:
        title= re.search("^[^:]*", line).group()
        t1= re.search('journal= (.*)\|volume', line) #.group(1)
        t2= re.search('journal= (.*)\|year', sample) #.group(1)
        if t1 and t2 and (len(t1.group(1)) > len(t2.group(1))):
            print title + " : " + t2.group(1)
        else if t1 and t2:
            print title + " : " + t1.group(1)
        else if t1:
            print title + " : " + t1.group(1)
        else if t2:
            print title + " : " + t2.group(1)

