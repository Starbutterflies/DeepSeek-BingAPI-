# import requests
import openai
import pandas as pd
import requests

API_KEY = "sk-2d5773e9a6724f5f8721bacea49b4c53"
url = "https://api.deepseek.com/chat/completions"
def Deep_judge(title):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "deepseek-chat",  # 指定使用 R1 模型（deepseek-reasoner）或者 V3 模型（deepseek-chat）
        "messages": [
            {"role": "system", "content": "你是一个冷漠无情的读文件助手，为兼容python，你只能告诉我哪一行所对应的网站最可能是特定年份，特定城市的报告，并以index的形式返回给我。且只能说这个index，以python列表的形式返回。如果没有对应年份和城市的报告，请返回False。"},
            {"role": "user", "content": f"输入标题：{title}\n" + str(pd.read_csv(rf"./test_data/{title}.csv"))}
        ],
        "stream": False , # 关闭流式传输
        "temperature":0,
    }
    return eval(requests.post(url, headers=headers,json=data).json()['choices'][0]['message']['content'])

def Deep_info_extract(title,text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "deepseek-chat",  # 指定使用 R1 模型（deepseek-reasoner）或者 V3 模型（deepseek-chat）
        "messages": [
            {"role": "system", "content": "你是一个冷漠无情的读报告助手，你的职责是:读我发给你的报告和标题，并只提取其中和标题相关的，机动车保有数量信息。为兼容python，请你返回一个字典——格式为:{‘机动车保有量’:468}，如果其中没有信息或者信息你拿不准，请你返回:{'机动车保有量':0},记住，单位为万辆！"},
            {"role": "user", "content": f"请务必核对输入标题的地区、年份和text中的地区、年份是否一致！\n输入标题：{title}\n" + "报告正文\n" + text}
        ],
        "stream": False , # 关闭流式传输
        "temperature":0,
    }
    return eval(requests.post(url, headers=headers,json=data).json()['choices'][0]['message']['content'])

if __name__ == '__main__':
    # print(Deep_judge("2014年二连浩特市国民经济和社会发展统计公报"))
    text = ""
    print(Deep_info_extract("2014年二连浩特市国民经济和社会发展统计公报",text))