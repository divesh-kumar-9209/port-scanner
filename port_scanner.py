import socket

target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\n---------------------------------")
print("Target:", target)
print("Scanning ports", start_port, "to", end_port)
print("---------------------------------\n")

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("[OPEN] Port", port)

    scanner.close()

print("\nScan completed.")