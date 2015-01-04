# -*- coding: utf-8 -*-
import re
"""
All Flesh Must Be Eaten  : PYRAMIDMAGAZINE 2-25
All Flesh Must Be Eaten  : PYRAMIDMAGAZINE 1-12
All Flesh Must Be Eaten  : PYRAMIDMAGAZINE 4-19
All Flesh Must Be Eaten  : PYRAMIDMAGAZINE 4-11
All Flesh Must Be Eaten  : PYRAMIDMAGAZINE 9-26
"""
#sample= "Ammonia : {{cite journal|author=Knacke, R. F., McCorkle, S., Puetter, R. C., Erickson, E. F., Kraetschmer, W. |year=1982|journal= APJ|volume= 260|page= 141|bibcode=1982ApJ...260..141K|doi=10.1086/160241|title=Observation of interstellar ammonia ice}}"

f = open('line_outputs2.txt', 'w')

with open("pagetitle_journal.txt") as infile:
    for line in infile:
        
        line_split= line.split(":")
        if line_split:
            page= line_split[0]
            if not page:
                page= ""
        
            journal = re.search(r'(?<=journal =)[^\|]+', line)
            if not journal:
                journal = re.search(r'(?<=journal=)[^\|]+', line)
            if not journal:
                journal = re.search(r'(?<=work=)[^\|]+', line)
                #if journal:
                #print journal.group(0)
            if journal:
                journal = journal.group(0)
                journal = re.sub(r'[^a-zA-Z\s]', u'', journal, flags=0).replace(" ","").upper()
                    #else:
                    #journal= ""
            
                year = re.search(r'(?<=year=)[^\|]+', line)
                if not year:
                    year = re.search(r'(?<=year =)[^\|]+', line)
                if year:
                    year= year.group(0).lstrip().rstrip()[:4]
                if not year:
                    year= re.search(r'(?<=date=)[^\|]+', line)
                    if year:
                        ayear=re.search(r'\d{4}-\d{2}-\d{2}', year.group(0).lstrip().rstrip())
                        if ayear:
                            year= ayear.group(0)[:4] #year.group(0).lstrip().rstrip()[4:]
                        else:
                            year= year.group(0).lstrip().rstrip()[-4:]
                    #ele:
                #year= year.group(0).lstrip().rstrip()[-4:]
                """
                if not year:
                    year= re.search(r'(?<=date=)[^\|]+', line)
                    if year:
                        year= year.group(0).lstrip().rstrip()[-4:]
                """
                """
                if year:
                    year= year.group(0).lstrip()[:4]
                  
                    try:
                        year= year.group(0).lstrip()[:4]
                    except:
                        year= re.search(r'(?<=date=)[^\|]+', line)
                        
                    #print "here"
                """
                    #if year:
                    #print year
                try:
                    total= page + " : " + journal + " " + year
                    print total
                except:
                    f.write(line)
                    #print line
            else:
                f.write(line)

f.close()
#print line