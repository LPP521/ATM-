#Downtiser
import os
import sys
import json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler

# data=account_info_id.read()
# print(data)

def read_info(card_num):
    read_path=data_handler.get_db_private_path(card_num)
    account_file=open(read_path,'r',encoding='utf-8')
    account_info=json.load(account_file)
    account_file.close()
    return account_info

def write_info(card_num,modified_info):
    write_path=data_handler.get_db_private_path(card_num)
    account_file=open(write_path,'w',encoding='utf-8')
    account_file.write(json.dumps(modified_info))
    account_file.flush()
    account_file.close()



