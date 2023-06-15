#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

count=0
total=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    t=line.find("0")
    number= float(line[t:])
    #print(number)
    count=count+1
    total=total+number
    #print(count)
    #print(line)
average=total/count
print("Average spam confidence:", average)
#print(count)
#print("Done")

