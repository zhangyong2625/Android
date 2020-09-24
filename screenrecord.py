"""
  @Author : Young
  @Email : 1293271923@qq.com
"""

# 手机录屏功能：
#  1.接收录制时间参数，若不传，默认为10s
#  2.以当前时间命名，并导出到桌面
import os
import random
import time
import sys

def screen_record(showtime):
	time1 = time.localtime(time.time())
	time2 = time.strftime("%Y%m%d_%H%M%S",time1)
	path = r"/sdcard/"+ time2 +".mp4"
	os.system(r"adb shell screenrecord --time-limit %d %s" % (showtime,path))
	os.system(r"adb pull %s" % path)

if __name__ == "__main__":
	# 接收时间参数，若不传，默认为10
	try:
		showtime = int(sys.argv[1])
	except:
		print("默认录制10s")
		showtime = 10
	screen_record(showtime)