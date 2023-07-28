import socket



def get_hostname():
    return socket.gethostname()


def get_server_ip(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None
    
    
    
hostname = get_hostname()
server_ip = get_server_ip(hostname)
print(server_ip)