#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195
maximum=0
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
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
#print(counts)

for address in counts:
    #print(address)
    if counts[address] is None or counts[address] > maximum:     # Checks if new maximum
        # Update the maximum if needed
        maximum = counts[address]
        # Stores the address of maximum
        maximum_address = address

print(maximum_address, maximum)            
            


