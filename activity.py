"""
  @Author : Young
  @Email : 1293271923@qq.com
"""

# 获取手机栈顶app的activity信息
import os

def get_activity():
	os.system("adb shell dumpsys activity activities >activity.txt")
	with open("activity.txt","r",encoding="utf-8") as fp:
		contents = fp.readlines()
		for line in contents:
			if "ResumedActivity" in line:
				print(line)
				break
	os.remove("activity.txt")

if __name__ == "__main__":
	get_activity()