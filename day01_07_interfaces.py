interfaces = [
    {"name": "Gi0/0", "status": "up", "speed": "1G"},
    {"name": "Gi0/1", "status": "down", "speed": "1G"},
    {"name": "Gi0/2", "status": "up", "speed": "10G"},
]

print("接口      状态    速率")
print("-" * 20)
for intf in interfaces:
    print("{:<10}{:<8}{}".format(intf["name"], intf["status"], intf["speed"]))