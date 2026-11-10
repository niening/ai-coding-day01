devices = [
    {"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
    {"name": "Firewall", "ip": "10.1.1.2", "role": "防火墙"},
    {"name": "WLC", "ip": "10.1.1.3", "role": "无线控制器"},
]

print("设备名称          管理地址          角色")
for device in devices:
    print("{:<18}{:<18}{}".format(device["name"], device["ip"], device["role"]))