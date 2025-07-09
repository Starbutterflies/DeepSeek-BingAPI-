import os
import numpy as np
import pandas as pd
import tqdm

from Deepseek_api import Deep_judge,Deep_info_extract
from request_gov_html import request_html,clean_html_lxml
def Main_loop(file_name):
    base_path = os.path.dirname(__file__)
    name_list = os.listdir('./' + file_name)
    path_list = [os.path.join(base_path, file_name, name) for name in name_list]
    for name, path in tqdm.tqdm(zip(name_list, path_list),total=len(path_list)):
        try:
            df = pd.read_csv(path)
            year = name[:4]
            begin_index = name.find("年")
            end_index = name.find("市")
            city_name = name[begin_index + 1:end_index]
            able_list = []
            for value in df.values:
                url = value[0]
                abstract = value[1]
                title = value[2]
                if (city_name in title) and (year in title):
                    able_list.append([url, abstract, title])
            if len(able_list) == 0:  # 如果没有可以使用的东西的话
                inte_name = name.rstrip(".csv")
                index = Deep_judge(inte_name)
                if index != False:
                    ok_df = df.loc[index, :]
                    for value in ok_df.values:
                        able_list.append(list(value))
                else:
                    pass
            print(name)
            if len(able_list) != 0:
                for url, abstract, title in able_list:
                    try:
                        inte_html = request_html(url)
                        print(f"正在打开:{url}")
                        byl = Deep_info_extract(name,clean_html_lxml(inte_html))["机动车保有量"]
                        if (byl > 0) & (byl < 7000):
                            with open(r'.\test.txt', 'a') as f:
                                print((name,byl))
                                f.write(rf'{name,byl},')
                                break
                    except Exception as e:
                        print(e)
            else:
                continue
        except Exception as e:
            pass


if __name__ == '__main__':
    file_name = 'test_data'
    Main_loop(file_name)