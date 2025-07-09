import time

import pandas as pd
import requests
import json

import tqdm
from china_city import CHINA_CITY
search_url = r"https://bing.ydcloud.org/api/v1/v7.0/search"
key = "8e6bbe7f-5466-4491-a973-a9d7108072c6"


def request_info(q):
    """
    :param q: 查询参数 ----查询内容
    :return: None ---访问失败
    """
    headers = {"Ocp-Apim-Subscription-Key": key, "count": '10'}
    params = {"q": q, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    try:
        assert response.status_code == 200
        inte_data = json.loads(response.text)["webPages"]['value']
        url_list = []
        abstract_list = []
        title_list = []
        for data in inte_data:
            url = data["url"]
            abstract = data["snippet"]
            title = data["name"]
            url_list.append(url)
            abstract_list.append(abstract)
            title_list.append(title)
        return pd.DataFrame({"url": url_list, "abstract": abstract_list, "title": title_list})
    except:
        return None


if __name__ == '__main__':
    for year in tqdm.tqdm(range(2021,2024)):
        for city in tqdm.tqdm(CHINA_CITY):
            report_name = f"{year}年{city}市国民经济和社会发展统计公报"
            request_info(report_name).to_csv("./test_data/" + report_name + ".csv", index=False)
            time.sleep(0.1)