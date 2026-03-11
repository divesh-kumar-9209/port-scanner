import socket
import time
import threading

target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

print("\n---------------------------------")
print("Target:", target)
print("Scanning ports", start_port, "to", end_port)
print("---------------------------------\n")

start_time = time.time()

open_ports = []

def scan_port(port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        result = scanner.connect_ex((target, port))

        if result == 0:
            banner = ""

            try:
                scanner.send(b"Hello\r\n")
                banner = scanner.recv(1024).decode(errors="ignore").split("\n")[0]
            except:
                banner = "Service detected"

            print(f"[OPEN] Port {port} → {banner}")
            open_ports.append(port)

    finally:
        scanner.close()

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print("\n---------------------------------")
print("Scan completed.")
print("Open ports:", sorted(open_ports))
print("Total scan time:", round(end_time - start_time, 2), "seconds")
print("---------------------------------")