#Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

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
        wds=words[5][:2]
        #print(wds)
        counts[wds] = counts.get(wds,0) + 1
#print(counts)

tmp=list()
for k, v in counts.items():
    newt=(k,v)
    tmp.append(newt)
    
tmp=sorted(tmp)
for k,v in tmp:
    print(k,v)
            


