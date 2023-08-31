from playsound import playsound
import time

# 定义音乐路径
music_path = "D:/FFOutput/wake/wake.mp3"

hour = int(input("请输入小时数："))
minute = int(input("请输入分钟数："))
second = int(input("请输入秒数："))

# 计算时间差
wake_time = time.time() + hour * 3600 + minute * 60 + second

# 等待时间到达后播放音乐并提示用户
while True:
    if time.time() >= wake_time:
        playsound(music_path)
        print("时间到了！")
        break
