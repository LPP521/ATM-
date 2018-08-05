#Downtiser

import os
import sys
def get_db_global_path(global_info):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_path=BASE_DIR+'\\data\\accounts_info\\%s'%(global_info)
    return global_path

def get_db_private_path(private_info):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    private_path=BASE_DIR+'\\data\\accounts_info\\%s.json'%(private_info)
    return private_path
