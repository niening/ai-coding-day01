import os
import re

route_n_result = os.popen("route -n").read()

pattern = r"^0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\.\d+\.\d+\.\d+\s+UG"
result = re.search(pattern, route_n_result, re.M)

if result:
    print(f"网关为：{result.group(1)}")
else:
    print("未找到默认路由")