#  Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
#Error, please enter a score between 0.0 and 1.0
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6      F

def computegrade(scr):
    if scr >=0.9 and scr <=1.0:
        return(print('Grade:', 'A'))
    elif scr >= 0.8 and scr <0.9:
        return (print('Grade:', 'B'))
    elif scr >= 0.7 and scr <0.8:
        return(print('Grade:', 'C'))
    elif scr >= 0.6 and scr <0.7:
        return (print('Grade', 'D'))
    elif scr < 0.6:
        return (print('Grade:', 'F'))
    else:
        if scr > 1.0:
            return(print("Bad score"))
        
inp=input('Please enter a score: ')
try:
    scr=float(inp)
except:
    print('Error, please enter a score between 0.0 and 1.0')
    quit()
    
computegrade(scr)


