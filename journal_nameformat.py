"""import re
import pandas as pd

errors=0

journal_year = pd.DataFrame(index=range(1900, 2015))

text = open('/data/wiki/pagetitle_journal.txt').read()

for line in text.split('\n'):
    
    journal = re.search(r'(?<=journal=)[^\|]+', line)
    if journal: journal = str.lower(journal.group(0)[:-1])
    
    year = re.search(r'(?<=year=)[^\|]+', line)
    if year:
        try:
            year = int(year.group(0)[:-1])
        except:
            errors += 1
            year = None
    
    if journal and year and year > 1900 and year < 2015:
        
        if journal in journal_year.columns:
            journal_year.loc[year, journal] += 1
        else:
            journal_year[journal] = 0
            journal_year.loc[year, journal] = 1

#journal_year.to_csv('journalyearcounts.csv')
print errors
"""
import re

text = "It's a lovely day!!! Shabba"
result = re.sub(r'[^a-zA-Z\s]', u'', text, flags=re.UNICODE)
result= result.replace(" ","").upper()
print result
