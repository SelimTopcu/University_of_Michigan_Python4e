fahr=input('Please enter the temperature in Fahrenheit: ')
try:
    float(fahr)
    cel=(float(fahr)-32.0)*5.0/9.0
    print("Celcius", cel)
except:
    print('Please enter a number')
