#  Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate):
    if hours>40:
        print('Pay:', pay+(hours-40)*(rate*0.5))
    else:
        print('Pay:', pay)
    return pay
    
hours=input('Enter hours: ')
rate=input('Enter rate: ')
fh=float(hours)
fr=float(rate)
pay=fh*fr

xp=computepay(fh,fr)

