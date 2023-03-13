import socket
import sys
from datetime import datetime
import os

start_time = datetime.now()

ip = socket.gethostbyname(sys.argv[1])

ping = os.system("ping {} -c 1 > /dev/null".format(ip))

print("-"*51)
print("[+] Target: ", sys.argv[1])
print("[+] Ports:  ", sys.argv[2])

if ping == 0:
	print("[+] {} is up and running".format(sys.argv[1]))
else:
	print("[+] {} is down".format(sys.argv[1]))
	print("Exiting...")
	exit()

print("[+] Scanning started at: {}".format(start_time))
print("-"*51)

def scan_specific_ports():
	ports = sys.argv[2]
	ports = ports.split(',')

	for i in ports:
		x = socket.SOCK_STREAM
		sock = socket.socket(socket.AF_INET, x)
		result = sock.connect_ex((ip, int(i)))
		try:
			service = socket.getservbyport(int(i))
		except:
			service = "None"

		if (result == 0):
			print(" Port: {}\t State: Open\t Service: {}".format(i, service))
		elif (result == 110):
			print(" Port: {}\t State: Filtered\t Service: {}".format(i, service))
		else:
			print(" Port: {}\t State: Closed\t Service: {}".format(i, service))

		sock.close()

	print("-"*51)
	time_passed = datetime.now() - start_time
	print("Scanning is completed in", time_passed)

def scan_multiple_ports():
	start_port = int(sys.argv[2])
	end_port = int(sys.argv[3])

	if start_port > end_port:
		tmp = start_port
		start_port = end_port
		end_port = tmp

	for ports in range(start_port,end_port+1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((ip, ports))
		try:
			service = socket.getservbyport(int(i))
		except:
			service = "None"

		if (result == 0):
			print(" Port: {}\t State: Open\t Service: {}".format(i, service))
		elif (result == 110):
			print(" Port: {}\t State: Filtered\t Service: {}".format(i, service))
		else:
			print(" Port: {}\t State: Closed\t Service: {}".format(i, service))
		
		sock.close()

	print("-"*51)
	time_passed = datetime.now() - start_time
	print("Scannig is completed in", time_passed)

if __name__ == "__main__":
	try:
		if (len(sys.argv) == 3):
			scan_specific_ports()
		elif (len(sys.argv) == 4):
			scan_multiple_ports()
		else:
			print("Invalid number of arguments")
			print("Usage: python3 portscanner <IP> <START_PORT> <END_PORT>")
			print("Usage: python3 portscanner <IP> <PORT1,PORT2,...>")

	except KeyboardInterrupt:
		print("\nExiting...")

	except OverflowError:
		print("\nPort must be 0-65535.")