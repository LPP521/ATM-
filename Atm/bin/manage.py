#Downtiser
import sys
import os
import time

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main
while True:
    time_format='%Y-%m-%d %X'
    print('------%s------'%time.strftime(time_format))
    user_aggr=input('请输入任意值以确认进入ATM管理系统，或输入q以结束本程序>>>')
    if user_aggr=='q':
        exit('您已退出管理程序')
    else:
        main.manage()