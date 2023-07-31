# Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

#Enter file:mbox.txt
#38549

#Enter file:mbox-short.txt
#39756

import re
count=0
total=0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New \S*: ([0-9.]+)', line)
    if len(x) > 0:
        for n in x:
            number=int(n)
            count=count+1
            total=total+number
            #print(number)
        
average=int(total/count)
print("Average:", average)
