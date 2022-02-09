import sys
import os
from collections import deque
root = os.path.dirname(os.path.realpath(__file__))
temp = sys.stdout

#Widonws Downloads 경로  C:\Users\azder\Downloads\
def path(input_num, input_name):
    datanum = ''
    datapath = root + '\\Downloads'
    if input_num != 0:
        datanum = f' ({input_num})'
    if input_name != '':
        datapath = f'C:\\Users\\{input_name}\\Downloads'
    return datanum,datapath


#input 입력, 결과값 저장 시작
def S(input_num = 0, input_name = '', plusname=''):
    datanum, datapath = path(input_num, input_name)
    sys.stdout = open(root + '\\my_output.txt','w') # txt로 저장
    sys.stdin = open(datapath+  f'\\{plusname}input{datanum}.txt', 'r')


def E(input_num = 0, input_name = '',plusname=''):
    datanum, datapath = path(input_num, input_name)
    sys.stdout.close
    sys.stdout = temp
    right_answer_que = deque(open(datapath + f'\\{plusname}output{datanum}.txt', 'r').readlines())
    my_answer_que = deque(open(root + '\\my_output.txt', 'r').readlines())
    while right_answer_que:
        answer = right_answer_que.popleft().strip()

        if my_answer_que:
            my_answer = my_answer_que.popleft().strip()
        else:
            my_answer = 'no answer'

        if answer == my_answer:
            print(f'{my_answer} -> O')
        else:
            print(f'{my_answer} -> X, answer: {answer}')
    
def C(input_num = 0, input_name = '', plusname=''):
    datanum, datapath = path(input_num, input_name)
    right_answer_que = deque(open(datapath + f'\\{plusname}output{datanum}.txt', 'r').readlines())
    my_answer_que = deque(open(root + '\\my_output.txt', 'r').readlines())
    while right_answer_que:
        answer = right_answer_que.popleft().strip()
        if my_answer_que:
            my_answer = my_answer_que.popleft().strip()
        else:
            my_answer = 'no answer'
        if answer == my_answer:
            print(f'{my_answer} -> O')
        else:
            print(f'{my_answer} -> X, answer: {answer}')

