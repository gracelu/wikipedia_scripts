import re

sample= "Ammonia : {{cite journal|author=Knacke, R. F., McCorkle, S., Puetter, R. C., Erickson, E. F., Kraetschmer, W. |year=1982|journal= APJ|volume= 260|page= 141|bibcode=1982ApJ...260..141K|doi=10.1086/160241|title=Observation of interstellar ammonia ice}}"

"""
t= re.search('journal=', sample)
if t:
    print t.group(0)
"""
#print re.sub("[^A-Z\d]", "", re.search("^[^:]*", sample).group(0).upper())
print re.search("^[^:]*", sample).group()
#t= re.search("(?<=journal)(.*)", sample);
t= re.search('journal= (.*)\|volume', sample)
if t:
    t=t.group(1)
    print t

t2= re.search('journal= (.*)\|page', sample)
if t:
    t2=t2.group(1)
    print t2

if t and (len(t) > len(t2)):
    print "hi"
else:
    print "bye"

"""
mystring =  "hi my name is ryan, and i am new to python and would like to learn more"
keyword = 'name'
befor_keyowrd, keyword, after_keyword = mystring.partition('keyword')
"""

"""
import re

with open("pagetitle_journal.txt") as infile:
    for line in infile:
        if "journal" in line:
            print line
"""