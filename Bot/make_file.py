import pandas as pd
from parser import parse

def file_to_xlsx():
    URL = input()
    res_dict = parse(URL)
    data = pd.DataFrame.from_dict(res_dict)
    data.to_excel('/home/antpotapov2019/Bot/bot/data/data.xlsx')
def file_to_csv():
    URL = input()
    res_dict = parse(URL)
    data = pd.DataFrame.from_dict(res_dict)
    data.to_csv('/home/antpotapov2019/Bot/bot/data/data.xlsx')