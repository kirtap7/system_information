'''
Created on Jan 25, 2019

@author: patrick
'''

import platform
import multiprocessing
import socket
import psutil

hostname = socket.gethostname()   
IP = socket.gethostbyname(hostname)   
 

def main():
    print('name of machine:', hostname)
    print('OS name:', platform.system())
    print('OS version:', platform.release())
    print('Number of CPUs:', multiprocessing.cpu_count())
    print('Memory info: ', psutil.virtual_memory())
    print('IP Address:', IP)
    return  


if __name__ == '__main__':
    main()