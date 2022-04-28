import socket
from datetime import datetime

ip = input('Enter IP: ')

print('-' * 41)
print('Scanning: ' + ip)
print('Time Started: ' + str(datetime.now()))
print('-' * 41)

port_list = []
scanned = 0

for port in range(1, 80):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = connection.connect_ex((ip, port))
    scanned += 1

    if result == 0:
        print('Port:', port, 'is open')
        port_list.append(port)
    else:
        print('Port:', port, 'is closed')
print(f'{scanned} ports were scanned')
print('Open ports: ' + str(port_list))
