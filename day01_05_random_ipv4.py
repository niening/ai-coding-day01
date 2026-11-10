import random

a = random.randint(0, 255)
b = random.randint(0, 255)
c = random.randint(0, 255)
d = random.randint(0, 255)

ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
print("随机产生的IPv4地址为：" + ip)