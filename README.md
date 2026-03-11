# Python Multithreaded Port Scanner

A multithreaded TCP port scanner built using Python.  
This tool scans a specified range of ports on a target host and identifies which ports are open.

## Features

- Scan custom port ranges
- Detect open TCP ports
- Multithreaded scanning for faster performance
- Scan time measurement
- Hostname support
- Clean terminal output

## How It Works

The scanner attempts to establish a TCP connection to each port within the given range.  
If the connection succeeds, the port is marked as open.

Multithreading allows multiple ports to be scanned simultaneously, significantly reducing scan time.

## Example Usage

Run the scanner:

python port_scanner.py

Example:

Enter target IP address: scanme.nmap.org  
Enter start port: 20  
Enter end port: 200

Output:

[OPEN] Port 22  
[OPEN] Port 80  

Scan completed.  
Open ports: [22, 80]

## Disclaimer

This project is for educational purposes only.  
Only scan systems you own or have permission to test.