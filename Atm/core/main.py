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
from core import transaction
from core import auth
from data import account_sample
operation={
    '1':'查询账户信息',
    '2':'还款',
    '3':'取款',
    '4':'转账',
    '5':'退出'
}
management={
    '1':'注册账号',
    '2':'申请额度',
    '3':'账号解冻',
    '4':'账号冻结',
    '5':'账号更新',
    '6':'退出'


}

print("-----Welcome to Downiser's ATM System 1.0-----")

def run(count=1):
    while True:
        choice = input('\033[32;1m请输入任意值以继续，或输入q退出>>>\033[0m')
        if choice == 'q':
            print('您已退出ATM系统')
            break

        card_num = input('请输入您的信用卡账号>>>')
        password = input('请输入密码>>>')
        if auth.is_exist(card_num)==False:
            print('账户不存在，请检查输入是否正确！')
            continue
        jud=auth.acc_auth(card_num,password,'r',count)

        while jud==True:
            print('------请选择您的操作------')
            print('1 %s'%operation['1'])
            print('2 %s'%operation['2'])
            print('3 %s'%operation['3'])
            print('4 %s'%operation['4'])
            print('5 %s'%operation['5'])
            user_choice=input('请选择一项服务>>>')
            if user_choice=='1':
                user_info=accounts.read_info(card_num)
                print('------账户信息------')
                print('开户人：%s'%(user_info['account_id']))
                print('信用卡账号：%s'%(user_info['card_num']))
                print('信用卡额度: %s'%(user_info['limit']))
                print('信用卡到期时间: %s-%s-%s'%(time.gmtime(user_info['expired_time']).tm_year,time.gmtime(user_info['expired_time']).tm_mon,time.gmtime(user_info['expired_time']).tm_mday))
                logger.private_access_log(user_info,'查询账户信息')
                time.sleep(3)
                continue
            elif user_choice=='2':
                repay_amount=transaction.repay(card_num)
                user_info = accounts.read_info(card_num)

                continue
            elif user_choice=='3':
                res=transaction.withdrawls(card_num)
                user_info = accounts.read_info(card_num)

                print(res)
                continue
            elif user_choice=='4':
                recipient_card_num=input('请输入您想转账的账户>>>')
                transaction.transfer(card_num,recipient_card_num)
                continue


            elif user_choice=='5':
                print('您已登出！')
                break

            else:
                print('不合法的输入！')
                continue
        else:
            if jud==False:
                continue
            else:
                count=jud
                continue



def manage():
    while True:
        choice = input('\033[32;1m请输入任意值以继续，或输入q退出管理系统>>>\033[0m')
        if choice == 'q':
            print('您已退出ATM管理系统')
            break
        print('----请选择一种服务----')
        print('1 %s'%management['1'])
        print('2 账户管理')
        print('3 %s'%management['5'])
        user_choice=input('请输入对应服务序号以继续>>>')
        if user_choice=='1':
            account_sample.creat_account()
            continue
        elif user_choice=='2':
            while True:
                choice = input('\033[32;1m请输入任意值以继续，或输入b返回>>>\033[0m')
                if choice == 'b':
                    print('您已退出,即将返回初始界面')
                    for i in range(10):
                        print('. ', end='')
                        time.sleep(0.5)
                    print('\n')
                    break
                card_num = input('请输入您的信用卡账号>>>')
                password = input('请输入密码>>>')
                if auth.is_exist(card_num) == False:
                    print('账户不存在，请检查输入是否正确！')
                    continue
                jud = auth.acc_auth(card_num,password,'m')
                while jud==True:
                    print('1 %s' % management['2'])
                    print('2 %s' % management['3'])
                    print('3 %s' % management['4'])
                    print('4 %s' % management['5'])
                    print('5 %s' % management['6'])

                    user_choice2 = input('请输入对应服务序号以继续>>>')
                    if user_choice2=='1':
                        new_limit=input('请输入您想申请的额度>>>')
                        present_info=accounts.read_info(card_num)
                        present_info['limit']=float(new_limit)
                        accounts.write_info(card_num,present_info)
                        logger.public_operation_log(present_info,'申请额度 %s 元'%new_limit)
                        logger.private_access_log(present_info,'申请额度 %s 元'%new_limit)
                        print('审核中')
                        for i in range(10):
                            print('. ',end='')
                            time.sleep(0.5)

                        print('\n申请成功')
                        continue
                    elif user_choice2=='2':
                        present_info = accounts.read_info(card_num)
                        present_info['state'] = True
                        accounts.write_info(card_num, present_info)
                        logger.public_operation_log(present_info, '解冻账户')
                        logger.private_access_log(present_info, '解冻账户')
                        print('审核中')
                        for i in range(10):
                            print('. ', end='')
                            time.sleep(0.5)

                        print('\n您的账户已解冻')
                        continue

                    elif user_choice2=='3':
                        confirm=input('您确认要冻结您的账号吗?输入任意值以确认，输入b以取消>>>')
                        if confirm=='b':
                            continue
                        else:
                            present_info = accounts.read_info(card_num)
                            present_info['state'] = False
                            accounts.write_info(card_num, present_info)
                            logger.public_operation_log(present_info, '冻结账户' )
                            logger.private_access_log(present_info, '冻结账户' )
                            print('审核中')
                            for i in range(10):
                                print('. ', end='')
                                time.sleep(0.5)

                            print('\n您的账户已冻结')
                            continue

                    elif user_choice2=='4':
                        present_info = accounts.read_info(card_num)
                        present_info['expired_time']=time.mktime(time.gmtime())+172800
                        accounts.write_info(card_num, present_info)
                        logger.public_operation_log(present_info, '更新账户')
                        logger.private_access_log(present_info, '更新账户')
                        print('审核中')
                        for i in range(10):
                            print('. ', end='')
                            time.sleep(0.5)
                        print('\n您的账户已更新')
                        continue
                    elif user_choice2=='5':
                        print('您的账户已登出！')
                        break
                    else:
                        print('不合法的输入，请再次输入')
                        continue
        elif user_choice=='3':
            print('您已登出')
            break
        else:
            print('不合法的输入，请重新输入!')
            continue






















