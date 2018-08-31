import socket
import time
import concurrent.futures

# Constant for the number of maximum threads to use in the port scanner
MAX_THREADS = 100

def get_service(port):
    """
    Get the service name for the given port number.

    :param port: Integer port number
    :return: String service name
    """
    try:
        # Get the service name
        service = socket.getservbyport(port)
        return service
    except:
        # No service found for the port
        return None

def scan_port(target, port):
    """
    Try connecting to the specified port on the target host.

    :param target: String host name or IP address
    :param port: Integer port number
    :return: True if the port is open, False otherwise
    """
    try:
        # Define socket object with timeout
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            # Try connecting to the port
            s.connect((target, port))
            return port
    except:
        return None

def port_scanner(target, startPort=1, endPort=1024):
    """
    Scan the target host for open ports.

    :param target: String host name or IP address
    """
    target_IP = socket.gethostbyname(target)
    print(f'Starting scan on host: {target_IP}')

    # To keep track of the open ports
    open_ports = []
    
    # We'll use threading to speed up the scanning process
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Start the scan operations and mark each future with its port
        future_to_port = {executor.submit(scan_port, target_IP, port): port for port in range(startPort, endPort)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            if future.result():
                open_ports.append(port)

    # Print open ports
    if open_ports:
        open_ports.sort()
        for port in open_ports:
            print(f'Port {port}: OPEN')
            print(f' - Service: {get_service(port)}')
    else:
        print("No open ports found.")

def main():
    target = input('Enter the host to be scanned: ')
    if target:
        startTime = time.time()
        port_scanner(target, startPort=1, endPort=1024)
        print(f'Time taken: {time.time() - startTime:.2f} seconds')
    else:
        print("Invalid target host. Please try again.")

if __name__ == '__main__':
    main()
