import re

mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

match = re.match(r"(\d+)\s+([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\s+(\w+)\s+(\S+)", mac_table)

print("{:<6}: {}".format("VLAN", match.group(1)))
print("{:<6}: {}".format("MAC", match.group(2)))
print("{:<6}: {}".format("Type", match.group(3)))
print("{:<6}: {}".format("Port", match.group(4)))