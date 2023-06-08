#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
    
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333

numlist = list()
try:
    while (True):
        inp = input('Enter a number: ')
        if inp == 'done': break
        value = int(inp)
        numlist.append(value)

    print('Max:', max(numlist))
    print('Min:', min(numlist))

except:
    print("Error, please enter a numeric value")
    continue