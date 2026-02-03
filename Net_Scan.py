from socket import *

def con_scan(target_host, target_port):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((target_host, target_port))
        print('[+]%d/tcp open'% target_port)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% target_port)

def port_scan(target_host,target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print('[-] Cannot resolve %s '% target_host)
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print('\n[+] Scan result of:  %s '% target_name[0])
    except:
        print('\n[+] Scan result of:  %s '% target_ip)
    setdefaulttimeout(1)
    for target_port in target_ports:
        print('Scanning Port: %d'%  target_port)
        con_scan(target_host, int(target_port))

if __name__ == '__main__':
    port_scan('google.com', [80, 22])