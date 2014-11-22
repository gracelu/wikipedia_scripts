#Code to parse through file with Wikipedia page titles and references and get rid of unwanted tags and text.
#Original file had lines that were <title></title> for Wikipedia page title or contained the tag "&lt;ref&gt;" for references. This script takes out tags and associates page title with each reference.

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
