
'''
任务：获取西刺，快代理，无忧代理网的免费代理IP地址并存入数据库，然后验证代理IP的可用性，并提供接口
功能模块：
1.dbs：提供数据库接口和验证数据库代理IP是否可用
2.spier：提供爬取代理IP服务和存入数据库
3.api.py：提供web服务代理IP的API接口
4.config.py：该代理池项目的配置信息
5.main.py：项目的主文件，提供三个进程，分别是获取代理IP存入数据库，数据库代理可用性验证，web服务进程。
'''

import sys
sys.path.append('./spider')
sys.path.append('./dbs')
from multiprocessing import Process
from crawl import Spider
from vaild_db import VailDb
from api import api
import time


def spider_fun(times=30*60):
    while True:
        print('爬取代理IP任务开启！')
        Spider.crawl()
        print('抓取代理IP任务完成！正在等待下一次执行')
        time.sleep(times)


def vaildb(times=5*60):
    while True:
        print('验证数据库可用代理IP任务开启！')
        VailDb.vaild()
        print('验证数据库代理是否可用完成，正在等待下次执行')
        time.sleep(times)


def main():
    web_api = Process(target=api)
    spider = Process(target=Spider.crawl)
    vaildb = Process(target=VailDb.vaild)
    web_api.start()
    spider.start()
    vaildb.start()
    web_api.join()
    spider.join()
    vaildb.join()


if __name__ == '__main__':
    main()