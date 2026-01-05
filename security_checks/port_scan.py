import sys
import socket
from datetime import datetime

#checks for one argument(<IP/Hostname>) 
if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1])

else:
  print("Invalid arguemt")
  print("Synatx: python3 port_scan.py <IP/Hostname>")
  sys.exit()

print("-" * 50)
print(f"Scanning the target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
  #scans for ports from 1 to 1025
  for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    results = s.connect_ex((target, port))
    if result == 0:
      try:
        service = socket.getservbyport(port)
      except:
        service = "Unknown service"
      print(f"Port {port] is open > Service: {service}")
    s.close()

except KeyboardInterrupt:
  print("\nProgram terminated")
  sys.exit()

except socket.gaierror:
  print("Could not find the IP/Hostname")
  sys.exit()

except socket.error:
  print("Unable to connect to the server")
  sys.exit()

  
  
