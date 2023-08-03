#Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

url = input('Enter the URL: ')
surl = url.split('/')
try:
    server = surl[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = ('GET'+' '+url+' '+'HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    count=0
    while True:
        data = mysock.recv(3000)
        count+=len(data)
        if len(data) < 1 or count>3000:
            break
        print(data.decode(),end='')
        print(count)

    mysock.close()

except:
    print('URL cannot be opened:')
    exit()
