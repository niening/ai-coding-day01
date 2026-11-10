version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

version = version_raw.strip()
print("去掉空格：" + version)
print("转大写：  " + version.upper())
print("替换版本：" + version.replace("17.03.04", "17.06.01"))