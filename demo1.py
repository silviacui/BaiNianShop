# -*-  coding:utf-8 -*-
import random

def random_demo():
    hello = [3, 5, 7, 9, 1, 11]
    for i in range(2):
        print(random.sample(hello, 1)) # sample的第一个参数是列表，第二个是每次随机抽取的数量

if __name__ == '__main__':
    random_demo()