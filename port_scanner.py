import socket
import time
import threading
import argparse

# Terminal colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"""
{CYAN}
========================================
        BYTESBREACH PORT SCANNER
========================================
{RESET}
""")

parser = argparse.ArgumentParser(description="Multithreaded Port Scanner")

parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("-p", "--ports", help="Port range (example: 20-200)", required=True)

args = parser.parse_args()

target = args.target
port_range = args.ports.split("-")

start_port = int(port_range[0])
end_port = int(port_range[1])

try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()

print(f"{YELLOW}Target      : {target}{RESET}")
print(f"{YELLOW}Port Range  : {start_port} - {end_port}{RESET}\n")

start_time = time.time()

open_ports = []

def scan_port(port):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        result = scanner.connect_ex((target, port))

        if result == 0:

            try:
                scanner.send(b"Hello\r\n")
                banner = scanner.recv(1024).decode(errors="ignore").split("\n")[0]
            except:
                banner = "Service detected"

            print(f"{GREEN}[OPEN]{RESET} {port:<5} → {banner}")
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

print("\n----------------------------------------")
print(f"{CYAN}Scan completed{RESET}")
print("Open ports:", sorted(open_ports))
print("Scan time :", round(end_time - start_time, 2), "seconds")
print("----------------------------------------")