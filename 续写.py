# 导入requests库
import requests

# 定义API的地址
api_url = "https://zj.v.api.aa1.cn/api/wzxx/"

# 获取用户输入的文章内容
content = input("请输入要续写的文章内容：")

# 定义API的参数
api_params = {
    "content": content
}

# 发送请求并获取响应
response = requests.get(api_url, params=api_params)

# 判断响应状态码是否为200
if response.status_code == 200:
    # 解析响应内容为json格式
    data = response.json()
    # 判断返回的状态码是否为0，表示成功
    if data["code"] == 0:
        # 获取返回的续写内容
        result = data["data"]
        # 从字典中提取续写内容
        result = result["generate_writing"][0]
        # 去掉无关内容，只保留续写内容
        result = result.replace("！", "")
        # 打印续写内容
        print(result)
    else:
        # 打印错误信息
        print(data["msg"])
else:
    # 打印请求失败的状态码
    print(response.status_code)
