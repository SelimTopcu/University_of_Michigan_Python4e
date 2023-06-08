#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
numlist = list()

while (True):
    inp=input('Please enter a number> ')
    if inp=='done': 
        break
        
    try:
        value=int(inp)
        numlist.append(value)
    except:
        print('Invalid input')
        continue
    
print("Maximum is", max(numlist))
print("Minimum is", min(numlist))
