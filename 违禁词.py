# 导入requests库
import requests

# 定义一个函数，接受一个文本参数，返回替换后的文本
def replace_banned_words(text):
  # 调用接口，传入text参数，获取返回的json数据
  response = requests.get("https://api.jixs.cc/api/wenan-wjcth/?text=" + text)
  data = response.json()
  # 判断返回的状态码是否为200，表示成功
  if data["code"] == 200:
    # 返回替换后的文本
    return data["data"]
  else:
    # 返回错误信息
    return "接口调用失败，请检查网络或参数"

# 获取用户输入的文本
text = input("请输入要检查的文本：")
print("原文：", text)
print("替换后：", replace_banned_words(text))
