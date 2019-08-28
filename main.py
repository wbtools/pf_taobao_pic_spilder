# -*- coding:utf-8 -*-
import os
import threading
import time
from pathlib import Path
from getImage.getImage import get_img
from getImage.getImage import read_excel
from getImage.getImage import read_data
from fake_useragent import UserAgent


def self_thread(data, thread_num):
    # print(data)
    print("开始爬取：" + str(thread_num))
    for i in data:
           # print(i)
        get_img(i[1], i[2], i[0])


if __name__ == '__main__':
    goods_list = read_data()
    #print(goods_list)
    #print(goods_list)
    # print(goods_list)
    # for i in goods_list:
    #     get_img(i[1], i[2], i[0])
    # excel_path = os.getcwd() + '/excel/test.xls'
    # data_list = read_excel(excel_path)
    # thread_list = []
    if len(goods_list) > 10:
        thread_data = [goods_list[i:i + 10] for i in range(0, len(goods_list), 10)]
        # print(thread_data)
        j = 1
        for i in thread_data:
            self_thread(i, j)
            j+=1 
    else:
        self_thread(goods_list, 1)

