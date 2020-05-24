import socket


def port_scan(host, ports):
    print(f'Scan host {host}')

    for port in ports:
        conn_scan(host, port)


def conn_scan(host, port):
    print('[*] Scanning port {}'.format(port), end='')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(b'KNOK...KNOK\r\n')
            data = s.recv(1024)
        print(' ... open')
        #print(data)
    except:
        print(' ... close')


if __name__ == '__main__':
    host = '185.240.248.25'
    ports = [22, 143, 80]
    port_scan(host, ports)

