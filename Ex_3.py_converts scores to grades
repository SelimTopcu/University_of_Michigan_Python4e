#  Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
#Error, please enter a score between 0.0 and 1.0
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6      F

inp=input('Please enter a score: ')
try:
    f=float(inp)
except:
    print('Error, please enter a score between 0.0 and 1.0')
    quit()
    
print(f)    
if f>=0.9 and f <=1.0:
    print('Grade:', 'A')
else:
    if f>= 0.8:
        print('Grade:', 'B')
    else:
        if f >= 0.7:
            print('Grade:', 'C')
        else:
            if f>= 0.6:
                print('Grade', 'D')
            else:
                if f< 0.6:
                    print('Grade:', 'F')
