"""
  @Author : Young
  @Email : 1293271923@qq.com
"""

# 手机截屏功能：
#  1.以当前时间命名，并导出到桌面
import os
import random
import time

def screenshot():
	time1 = time.localtime(time.time())
	time2 = time.strftime("%Y%m%d_%H%M%S",time1)
	path = r"/sdcard/pic_"+ time2 +".png"
	os.system(r"adb shell screencap %s" % path)
	os.system(r"adb pull %s" % path)

if __name__ == "__main__":
	screenshot()
