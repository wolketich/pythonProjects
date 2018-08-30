from socket import *
import time

def port_scanner(target):
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()   

def main():
    target = input('Enter the host to be scanned: ')
    startTime = time.time()
    port_scanner(target)
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    main()

