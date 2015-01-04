import re

#sample= "Ammonia : {{cite journal|author=Knacke, R. F., McCorkle, S., Puetter, R. C., Erickson, E. F., Kraetschmer, W. |year=1982|journal= APJ|volume= 260|page= 141|bibcode=1982ApJ...260..141K|doi=10.1086/160241|title=Observation of interstellar ammonia ice}}"

with open("pagetitle_journal.txt") as infile:
    for line in infile:
        
        line_split= line.split()
        if line_split:
            page= line_split[0]
            if not page:
                page= ""
            
            journal = re.search(r'(?<=journal=)[^\|]+', line)
            if journal:
                journal = journal.group(0)
                journal = re.sub(r'[^a-zA-Z\s]', u'', journal, flags=0).replace(" ","").upper()
            else:
                journal= ""
        
            year = re.search(r'(?<=year=)[^\|]+', line)
            if year:
                try:
                    year= year.group(0).lstrip()[:4]
                except:
                    year= ""

            try:
                total= page + " : " + journal + " " + year
            except:
                total= line

            print total