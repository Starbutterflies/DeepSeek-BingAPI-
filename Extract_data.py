import pandas as pd
import os
import re

def extract_data(file_name):
    with open(file_name,"r") as f:
        content = f.read()
        content = "[" + content + "]"
    new_data = pd.DataFrame(eval(content),columns=["标题","保有量(万辆)"])
    new_data["年份"] = new_data["标题"].apply(lambda row: row[:4])
    return new_data

if __name__ == '__main__':
    extract_data('test.txt').to_csv("测试提取数据.csv")