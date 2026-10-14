import socket
import sys

try:
    target = "localhost"
    ports = [22, 80, 443, 8080, 3306, 5432, 6379, 27017, 5000, 8000]
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
except KeyboardInterrupt:
        print("Scan interrupted by user.")
except socket.gaierror:
        print("Error resolving hostname.")
sys.exit()