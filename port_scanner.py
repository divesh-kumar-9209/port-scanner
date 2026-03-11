import socket
import time

target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\n---------------------------------")
print("Target:", target)
print("Scanning ports", start_port, "to", end_port)
print("---------------------------------\n")

start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print("[OPEN] Port", port)

    scanner.close()

end_time = time.time()

print("\n---------------------------------")
print("Scan completed.")
print("Open ports:", open_ports)
print("Total scan time:", round(end_time - start_time, 2), "seconds")
print("---------------------------------")