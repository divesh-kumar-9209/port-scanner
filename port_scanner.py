import socket

target = input("Enter target IP address: ")

print("\nScanning target:", target)
print("Scanning ports 1 to 1024...\n")

for port in range(1, 1025):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    scanner.close()

print("\nScan completed.")