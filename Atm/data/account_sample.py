#Downtiser
import os
import sys
import json
import time

#f=open('accounts_info\\sam2.txt','w+',encoding='utf-8')
#print(hash('downtiser'))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import logger
from core import data_handler
from core import accounts
def creat_account():
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    new_path=BASE_DIR+'\\data\\accounts_info\\card_num.txt'
    sys.path.append(BASE_DIR)

    card_num_record=open(new_path,'r+',encoding='utf-8')

    num_data=card_num_record.read()
    user_choice='none'
    while True:
        user_choice = input('\033[32;1m请输入任意值以继续，或输入b返回上一级>>>\033[0m')

        if user_choice=='b':
            exit('\033[31;1m取消创建账户！\033[0m')
        account_id=input('\033[32;1m请输入您的姓名>>>\033[0m')
        card_num=input('\033[32;1m请输入一个合法的卡号(卡号为8位纯数字)，此卡号以后将成为您的信用卡账户：\033[0m')
        password=input('\033[32;1m请输入您的密码>>>\033[0m')
        password_confirm=input('\033[32;1m请再次输入您的密码以确定>>>\033[0m')
        user_limit=input('\033[32;1m请输入您想申请的信用卡额度>>>\033[0m')


        if card_num in num_data or len(card_num)!=8 or card_num.isdigit()==False:
            print('\033[31;1m账号已存在！\033[0m')
            continue
        elif password!=password_confirm:
            print('\033[31;1m两次密码输入不一致\033[0m')
            continue
        elif user_limit.isdigit()!=True:
            print('\033[31;1m信用额度只能为数字！\033[0m')
            continue
        elif  int(user_limit)<0:
            print('\033[31;1m额度不合法！\033[0m')
            continue
        else:

            card_num_record.write('%s\n'%(card_num))
            card_num_record.close()
            time_stamp=time.mktime(time.gmtime())+172800
            info={
                'account_id':account_id,
                'card_num':card_num,
                'password':password,
                'limit':float(user_limit),
                'expired_time':time_stamp,
                'state':True
            }
            real_path=data_handler.get_db_private_path(info)
            accounts.write_info(card_num,info)

            print('\033[32;1m成功创建账户！\033[0m')
            logger.public_operation_log(info,'创建账户')

            break

