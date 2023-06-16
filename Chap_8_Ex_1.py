#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
def chop(t):
    del t[0],t[-1]
    
letters = ['a', 'b', 'c', 'd']
chop_list=chop(letters)
print(letters)          #returns ['b', 'c']
print(chop_list)        #returns None

#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(t):
    return t[1:-1]
letters=['a', 'b', 'c', 'd', 'e']
rest=middle(letters)
print(rest)             #returns ['b', 'c', 'd']