import re

#sample= "Ammonia : {{cite journal|author=Knacke, R. F., McCorkle, S., Puetter, R. C., Erickson, E. F., Kraetschmer, W. |year=1982|journal= APJ|volume= 260|page= 141|bibcode=1982ApJ...260..141K|doi=10.1086/160241|title=Observation of interstellar ammonia ice}}"

with open("journal_names.txt") as infile:
    for line in infile:
        result = re.sub(r'[^a-zA-Z\s]', u'', line, flags=0)
        result= result.replace(" ","").upper()
        print result
        #journal = re.search(r'(?<=journal=)[^\|]+', line)
        #if journal:
            #print journal.group(0)

