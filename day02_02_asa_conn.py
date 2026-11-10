import re

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

match = re.match(r"(\w+)\s+server\s+([\d.]+):(\d+)\s+localserver\s+([\d.]+):(\d+)", conn)

print("{:<12}: {}".format("Protocol", match.group(1)))
print("{:<12}: {}".format("Server IP", match.group(2)))
print("{:<12}: {}".format("Server Port", match.group(3)))
print("{:<12}: {}".format("Client IP", match.group(4)))
print("{:<12}: {}".format("Client Port", match.group(5)))