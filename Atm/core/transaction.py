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

def repay(card_num):
    repay_amount=input('请输入还款金额：')
    modified_info=accounts.read_info(card_num)
    modified_info['limit']=round(modified_info['limit']+float(repay_amount),2)
    accounts.write_info(card_num,modified_info)
    logger.public_operation_log(modified_info,'还款%s元'%(repay_amount))
    logger.private_access_log(modified_info,'还款%s元'%(repay_amount))
    print('还款成功！')
    return repay_amount

def withdrawls(card_num):
    withdrawls_amount=input('请输入取款金额：')
    modified_info = accounts.read_info(card_num)
    if float(withdrawls_amount)>modified_info['limit']:
        print('余额不足！')
        return '取款失败，余额不足'
    else:
        modified_info['limit']=round(modified_info['limit']-float(withdrawls_amount)*1.05,2)
        accounts.write_info(card_num, modified_info)
        logger.public_operation_log(modified_info, '取款%s元' % (withdrawls_amount))
        logger.private_access_log(modified_info, '取款%s元' % (withdrawls_amount))
        print('取款成功')
        return '取款 %s 元'%withdrawls_amount


def transfer(transfer_card,recipient_card):
    db_global_path = data_handler.get_db_global_path('card_num.txt')
    public_file=open(db_global_path,'r')
    public_info=public_file.read()
    public_file.close()
    if recipient_card in public_info:
        transfer_amount=input('请输入您想转账的金额>>>')
        transfer_card_info=accounts.read_info(transfer_card)
        recipient_card_info=accounts.read_info(recipient_card)
        if transfer_card_info['limit']<float(transfer_amount):
            logger.public_operation_log(transfer_card_info,'转账失败')
            logger.private_access_log(transfer_card_info,'转账失败')
            print('余额不足！')
        else:
            print('接受账户开户人:%s****%s'%(recipient_card_info['account_id'][0],recipient_card_info['account_id'][-1]))
            user_choice=input('请确认是否转账(输入任意值以继续或输入b以取消)>>>')
            if user_choice=='b':
                logger.public_operation_log(transfer_card_info, '取消转账')
                logger.private_access_log(transfer_card_info, '取消转账')
                print('您已取消转账!')
                return False

            else:
                transfer_card_info['limit']=transfer_card_info['limit']-float(transfer_amount)
                recipient_card_info['limit']=recipient_card_info['limit']+float(transfer_amount)
                accounts.write_info(transfer_card,transfer_card_info)
                accounts.write_info(recipient_card,recipient_card_info)
                logger.public_operation_log(transfer_card_info, '成功转账 %s 元至账号 %s'%(transfer_amount,recipient_card))
                logger.private_access_log(transfer_card_info, '')
                print('转账成功')
                return True
    else:
        print('账户不存在，请检查输入是否正确！')
        return False







