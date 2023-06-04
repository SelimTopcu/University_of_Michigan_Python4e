#  Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
h=input('Enter hours: ')
r=input('Enter rate: ')
fh=float(h)
fr=float(r)
pay=fh*fr
if fh>40:
    print('Pay:', pay+(fh-40)*(fr*0.5))
else:
    print('Pay:', pay)
