import re

route_n_result = """Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.214.2   0.0.0.0         UG    100    0        0 eno16777984
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
192.168.214.0   0.0.0.0         255.255.255.0   U     100    0        0 eno16777984
202.100.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno33554944"""

pattern = r"^0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\.\d+\.\d+\.\d+\s+UG"
result = re.search(pattern, route_n_result, re.M)

if result:
    print(f"网关为：{result.group(1)}")
else:
    print("未找到默认路由")