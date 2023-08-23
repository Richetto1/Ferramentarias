import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target_host = '10.3.77.20'
    start_port = 1000
    end_port = 5000
    scan_ports(target_host, start_port, end_port)

