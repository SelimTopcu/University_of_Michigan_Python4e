#We will write a Python program to read through the lines of the file, break each line into a list of words, and then loop through each of the words in the line and count each word using a dictionary.

fname = input('Enter the file name: ')
unique_words = dict()


try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words[word]=1
        else:
            unique_words[word]+=1
            
print(unique_words)