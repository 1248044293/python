from textblob import TextBlob

while True:
    text = input("请输入需要纠正拼写的文本（输入'quit'退出）：")

    # 判断用户是否要退出循环
    if text == "quit":
        break

    # 进行文本纠错操作
    corrected_text = TextBlob(text).correct()

    # 输出纠正后的结果
    print(corrected_text)
