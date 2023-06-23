#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

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
        counts[words[1]] = counts.get(words[1],0) + 1
#print(counts)

tmp=list()
for k, v in counts.items():
    newt=(v,k)
    tmp.append(newt)
#print('Flipped', tmp)
tmp=sorted(tmp, reverse=True)
for v,k in tmp[:1]:
    print(k,v)
            


