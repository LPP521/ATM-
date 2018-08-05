#Downtiser
import os
import sys
import json
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler
from core import logger
from core import accounts

#path=data_handler.get_db_path()







def is_exist(card_num):
    db_global_path=data_handler.get_db_global_path('card_num.txt')
    global_info=open(db_global_path,'r',encoding='utf-8')
    global_data=global_info.read()
    if card_num in global_data:
        global_info.close()
        return True
    else:
        global_info.close()
        return False

def acc_auth(card_num,password,mode,count=1):
    db_private_path=data_handler.get_db_private_path(card_num)
    private_info=accounts.read_info(card_num)
    if mode=='r':
        time_stamp=time.mktime(time.gmtime())
        if count<4:
            if private_info['password']==password and private_info['state']==True and time_stamp<=private_info['expired_time']:
                print('登录成功！')
                logger.public_operation_log(private_info,'成功登录')
                return True
            elif time_stamp>=private_info['expired_time']:
                print('您的账户已过期，请前往管理端口处理！')
                logger.public_operation_log(private_info, '登录失败')
                return False
            elif private_info['state']==False :
                print('您的账户已被冻结，请前往管理端口处理！')
                logger.public_operation_log(private_info, '登录失败')
                return False
            else:
                print('密码错误！')
                logger.public_operation_log(private_info, '登录失败')
                count=count+1
                return count
        else:
            print('密码输错次数过多，您的账户已被冻结！')
            private_info['state']=False
            accounts.write_info(private_info)
            logger.public_operation_log(private_info, '账户被冻结')
            logger.private_access_log(private_info,'账户被冻结')
            return False

    if mode=='m':
        if private_info['password'] == password:
            print('登录成功！')
            logger.public_operation_log(private_info, '成功登录')
            return True
        else:
            print('密码错误！')
            logger.public_operation_log(private_info, '登录失败')
            return False









