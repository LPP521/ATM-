#Downtiser
import os
import sys
import json
import time


def public_operation_log(info,operation='None'):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    access_path = BASE_DIR + '\\log\\access.log'
    sys.path.append(BASE_DIR)
    access_file=open(access_path,'a+',encoding='utf-8')
    log_time_formate='%Y-%m-%d %X'
    log_time=time.strftime(log_time_formate)
    log_item='%s %s %s %s\n'%(log_time,info['account_id'],info['card_num'],operation)
    access_file.write(log_item)
    access_file.close()


def private_access_log(info,operation):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    access_path = BASE_DIR + '\\log\\private_access_%s.log'%info['card_num']

    #access_file = open(access_path, 'w', encoding='utf-8')
    if os.path.isfile(access_path):
        private_access_file = open(access_path, 'a', encoding='utf-8')
        log_time_formate = '%Y-%m-%d %X'
        log_time = time.strftime(log_time_formate)
        log_item = '%s %s %s %s\n' % (log_time, info['account_id'], info['card_num'], operation)
        private_access_file.write(log_item)
        private_access_file.close()
    else:
        private_access_file = open(access_path, 'w', encoding='utf-8')
        log_time_formate = '%Y-%m-%d %X'
        log_time = time.strftime(log_time_formate)
        log_item = '%s %s %s %s\n' % (log_time, info['account_id'], info['card_num'], operation)
        private_access_file.write(log_item)
        private_access_file.close()




