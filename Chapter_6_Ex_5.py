#Exercise 5: Take the following Python code that stores a string: Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence:0.8475'
nstr=str.find(':')
anstr=str[19:]
fanstr=float(anstr)
print(nstr)
print(anstr)
print(fanstr)