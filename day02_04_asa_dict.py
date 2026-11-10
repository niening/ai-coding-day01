import re

asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

pattern = (r"TCP\s+Student\s+(\d+\.\d+\.\d+\.\d+):(\d+)\s+"
           r"Teacher\s+(\d+\.\d+\.\d+\.\d+):(\d+),\s+"
           r"idle\s+\d+:\d+:\d+,\s+bytes\s+(\d+),\s+flags\s+(\w+)")

asa_dict = {}
for conn in asa_conn.split("\n"):
    result = re.match(pattern, conn)
    if result:
        src, src_port, dst, dst_port, bytes_, flags = result.groups()
        asa_dict[(src, src_port, dst, dst_port)] = (bytes_, flags)

print("打印分析后的字典！\n")
print(asa_dict)

print("\n格式化打印输出\n")
line1 = "{:<10}: {:<16} | {:<10}: {:<6} | {:<10}: {:<16} | {:<10}: {}"
line2 = "{:<10}: {:<16} | {:<10}: {}"
for key, value in asa_dict.items():
    print(line1.format("src", key[0], "src_port", key[1],
                       "dst", key[2], "dst_port", key[3]))
    print(line2.format("bytes", value[0], "flags", value[1]))
    print("=" * 84)