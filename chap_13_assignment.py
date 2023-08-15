#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1829039.xml (Sum ends with 80)
#ou do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format and Approach
#The data consists of a number of names and comment counts in XML as follows:

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst=list()
number=0
url = input('Enter URL: ')
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
    
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for count in counts:
    number=number+1
    lst.append(int(count.text))
print(number)            
print(sum(lst))


