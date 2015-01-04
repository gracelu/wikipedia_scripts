with open("ref_head.txt") as infile:
    for line in infile:
        if "journal" in line:
            print line
