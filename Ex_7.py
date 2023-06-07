#  Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
#Error, please enter a score between 0.0 and 1.0
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6      F

def computegrade(score):
    if f>=0.9 and f <=1.0:
        grade='A'
        print('Grade:', grade)
    elif f>= 0.8 and f<0.9:
        grade= 'B'
        print('Grade:', grade)
    elif f >= 0.7 and f<0.8:
        grade='C'
        print('Grade:', grade)
    elif f>= 0.6 and f<0.7:
        grade='D'
        print('Grade', grade)
    elif f< 0.6:
        grade='F'
        print('Grade:', grade)
    else:
        if f > 1.0:
            grade=print("Bad score")
        
    return grade
inp=input('Please enter a score: ')
try:
    f=float(inp)
except:
    print('Error, please enter a score between 0.0 and 1.0')
    quit()
    

score=f
grade = computegrade(score)
