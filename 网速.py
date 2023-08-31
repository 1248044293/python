import speedtest  
  
speed = speedtest.Speedtest()  
download_speed = speed.download() / 1024 / 1024  
upload_speed = speed.upload() / 1024 / 1024  
  
print(f'下载速度为：{download_speed:.2f} MB/s')  
print(f'上传速度为：{upload_speed:.2f} MB/s')
