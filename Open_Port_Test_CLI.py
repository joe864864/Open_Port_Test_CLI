"""
Title: Open_Port_Test
Author: Joseph Scott
Build Date: December 2019
Description: CLI application to test what ports for an IP Address or host are open. Allows user to specify ip address, port range, and timeout.
"""

import socket

def testPort(address,port, timeout):
    s = socket.socket()
    s.settimeout(timeout)
    open = -1
    try:
        s.connect((address, port))
    except:
        print("Could not connect to: ",address,':',port,sep='')
    else:
        print("Connected: ",address,':',port,sep='')
        open = port
    finally:
        s.close()
    return open


def main():
    print("Test for open ports")
    openPorts = []

    ip = input("Please enter IP or host: ")

    portStart = int(input("Please enter starting port: "))
    portEnd = int(input("Please enter ending port: "))

    timeout = float(input("Please enter preferred timeout: "))
    print('', end='')

    currentPort = portStart

    while(currentPort <= portEnd):
        temp = testPort(ip,currentPort,timeout)
        currentPort+=1

        if temp >= 0:
            openPorts.append(temp)

    print('--------------------------')
    print("Done")
    print('--------------------------')
    print("Open ports for ", ip, ": ", sep='', end='')

    for count in range(len(openPorts)):
        if count+1 == len(openPorts):
            print(openPorts[count], end='')
        elif count+2 == len(openPorts) and len(openPorts) == 2:
            print(openPorts[count], " and ", sep='', end='')
        elif count+2 == len(openPorts):
            print(openPorts[count], ", and ", sep='', end='')
        else:
            print(openPorts[count], ", ", sep='', end='')
    print('\n', end='')

    print("Ports tested: ", portStart,"-", portEnd, sep='')

main()