"""
  @Author : Young
  @Email : 1293271923@qq.com
"""

# 1.获取手机栈顶app应用的包名
# 2.将apk包导出到电脑，文件名：包名.apk
import os
import re
import time

def get_package():
	os.system("adb shell dumpsys activity activities >1.txt")
	package = ""
	path = ""
	filename = ""
	with open("1.txt","r",encoding="utf-8") as fp:
		contents = fp.readlines()
		for line in contents:
			if "ResumedActivity" in line:
				pattern = "[" + " /" + "]"
				list_a = re.split(pattern,line)
				for val in list_a:
					if "." in val:
						package = val
						break
	print(package)
	os.remove("1.txt")
	os.system("adb shell pm path %s >2.txt"%package)
	with open("2.txt","r",encoding="utf-8") as fp:
		path = fp.readline()[8:]
		print(path)
		filename = path.strip().split("/")[-1]
		print(filename)
	os.remove("2.txt")
	os.system("adb pull %s"%path)
	# time.sleep(3)
	os.renames(filename,package+".apk")
	
if __name__ == "__main__":
	get_package()
	
















