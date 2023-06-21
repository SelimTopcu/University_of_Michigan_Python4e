#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

counts = dict()
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line=line.rstrip()
    words = line.split()
        
    if not line.startswith('From '): continue
            
    else:
        atpos = words[1].find('@')       # Position of '@'
        domain = words[1][atpos+1:]       # Store characters after '@'
        
        if domain not in counts:
            counts[domain] = 1               #First entry
        else:
            counts[domain] += 1               # Additional counts
            
print(counts)
