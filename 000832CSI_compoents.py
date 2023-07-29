from iFinDPy import *
import pandas as pd
import datetime as dt
# 登录函数
def thslogindemo():
    # 输入用户的帐号和密码
    id = ''
    password = ''
    thsLogin = THS_iFinDLogin(id, password)
    print(thsLogin)
    if thsLogin != 0:
        print('登录失败')
    else:
        print('登录成功')

thslogindemo()
def compontent(dates):
    data = []
    for date in dates:
        print(date)
        try:
            sub_data = THS_DR('p03473',f'iv_date={date};iv_zsdm=000832.CSI','p03473_f002:Y','format:dataframe').data
            sub_data.columns = [date]
            data.append(sub_data)
        except:
            print('error')
    return pd.concat(data,axis=1)
dates = pd.bdate_range(start='20170101',end='20230725')
dates = [date.strftime('%Y%m%d') for date in dates]
data = compontent(dates)
dates = pd.to_datetime(data.columns)
dates = [date.strftime('%Y-%m-%d') for date in dates]
data.columns = dates
data.to_excel('000832CSI_components.xlsx')