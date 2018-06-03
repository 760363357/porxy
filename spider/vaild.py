import time
import sys
import queue
import requests
sys.path.insert(0, '../')
requests.packages.urllib3.disable_warnings()
from multiprocessing.pool import ThreadPool
from config import VAILD_URL
from config import THREAD_NUM
from config import HEADER_INFO



class Vaild(object):
    proxies = queue.Queue()

    @staticmethod
    def valid_one(proxy):
        method = proxy.get('protocol_type').lower()
        ip = proxy.get('proxyip')
        port = proxy.get('port')
        proxs = {method: ip + ':' + port}
        start = time.time()
        try:
            res = requests.get(VAILD_URL[method], headers=HEADER_INFO, verify=False, proxies=proxs, timeout=10)
        except Exception as e:
            print(f'代理{proxy}代理暂时不可用！')
        else:
            end = time.time()
            if res.status_code == 200:
                print(f'完成验证通过，该代理可用{proxy}')
                proxy['delay'] = '{:.2f}'.format(end - start)
                proxy['last_time'] = time.strftime('%Y/%m/%d/%H:%M', time.localtime(end))
                proxy['protocol_type'] = proxy['protocol_type'].lower()
                Vaild.proxies.put(proxy)
            else:
                print(f'该代理有响应但无法正确连接{proxy}')

    @staticmethod
    def vaild_many(proxies):
        pool = ThreadPool(THREAD_NUM)
        pool.map(Vaild.valid_one, proxies)







