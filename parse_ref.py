import re

title= ""

with open("ref_head.txt") as infile:
    for line in infile:
        t = re.search('<title>(.+?)</title>', line)
        if t:
            title= t.group(1)
        #print title
    
        r = re.search('&lt;ref&gt;(.+?)&lt;/ref&gt;', line)
        #r= re.search('ref(.+?)ref', line)
        if r:
            print title + " : " + r.group(1)
        
        """
        if "<title>" in line:
            title= line
            print title
        """