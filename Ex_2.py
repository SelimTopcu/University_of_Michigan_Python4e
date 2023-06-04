#  Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

h=input('Enter hours: ')
r=input('Enter rate: ')
try:
    fh=float(h)
    fr=float(r)
except:
    print('Error, please enter numeric input')
    quit()
print(fh,fr)    
pay=fh*fr
if fh>40:
    print('Pay:', pay+(fh-40)*(fr*0.5))
else:
    print('Pay:', pay)
