import requests
import traceback
import chardet
import time
import sys
sys.path.append('../')


from config import RULE_LIST
from config import HEADER_INFO
from config import DOWN_DELAY
from parse import Parse
from vaild import Vaild
from dbs.mongo_db import MongoDb

requests.packages.urllib3.disable_warnings()


class Spider(object):
    @staticmethod
    def send_get(url):
        try:
            response = requests.get(url, headers=HEADER_INFO, verify=False)
            if response.status_code == 200:
                res_coding = chardet.detect(response.content)
                time.sleep(DOWN_DELAY)
                return response.content.decode(res_coding['encoding'])
            else:
                traceback.print_exc()
                raise requests.HTTPError
        except requests.HTTPError as e:
            print('请求异常，请检查URL配置参数是否正确！', e)
        except requests.Timeout as e:
            print('请求超时！', e)
        except requests.ConnectionError as e:
            print('网络连接出错，请检查本地连接', e)

    @staticmethod
    def crawl():
        proxies = []
        for rule_list in RULE_LIST:
            print(f"正在获取{rule_list['name']}的代理IP")
            for url in rule_list.get('url_list'):
                print(f'正在获取URL{url}的代理IP')
                response = Spider.send_get(url)
                date = []
                for item in rule_list.get('date_dict').items():
                    Parse.parse(item[0], item[1], date, response, method=rule_list['parse_type'])
                proxies.extend(date)
                print(f'从该URL中获取{len(date)}个代理IP')
        print('获取代理完成，下面开始验证代理的可用性！')
        print(f'共获取到{len(proxies)}个代理IP')
        Vaild.vaild_many(proxies)
        num = 0
        for i in range(Vaild.proxies.qsize()):
            num += MongoDb.insert(Vaild.proxies.get())
        print(f'获取代理IP完成，成功插入{num}条数据！')

