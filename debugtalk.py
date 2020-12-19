import time
import hashlib

import requests


def sleep(n_secs):
    time.sleep(n_secs)


def sign():
    phoneNum = "123434"
    optCode = "testfan"
    timestamp = "12112121212"
    sign1 = phoneNum + optCode + timestamp
    new_sign = hashlib.md5(sign1.encode()).hexdigest()
    return {"phoneNum": phoneNum, "optCode": optCode, "timestamp": timestamp, "sign": new_sign}

def get_token():
    #对登录接口进行访问，获取响应内token字段
    url = "http://localhost:8080/pinter/bank/api/login21"
    data ={'userName':'admin','password':1234}
    resp = requests.post(url,data=data)
    try:
        token = resp.json().get('data')
    except:
        token=""
    return token

def str_to_int():
    '''
    b接口依赖于a接口的返回数据，对a接口返回数据做处理
    :return: 
    '''

def hook_up():
    '''
    对请求的数据做处理的函数
    :return: 
    '''
    print("执行setup_hooks")

def hook_down():
    '''
    :return: 
    '''
    print("执行teardown_hooks")


def hook_log(info):
    '''
    :return: 
    '''
    print(info)

def get_data():
    return [
         ['正常登录', 'admin', '1234', 'success'],
         ['密码为空','admin',"",'参数为空'],
         ['用户名为空',"",'1234','参数为空'],
         ['用户名和密码为空',"","",'参数为空']
    ]

if __name__ == '__main__':
    print(get_token())