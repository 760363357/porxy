import sys
import time
sys.path.insert(0, '../')
sys.path.append('../spider')


from mongo_db import MongoDb
from spider.vaild import Vaild


class VailDb(object):
    @staticmethod
    def vaild():
        cur = list(MongoDb.get())
        Vaild.vaild_many(cur)
        for i in range(Vaild.proxies.qsize()):
            proxy = Vaild.proxies.get()
            if proxy['proxyip'] not in cur:
                proxy['delay'] = '-1'
            else:
                proxy['last_time'] = time.strftime('%Y/%m/%d/%H:%M:', time.localtime(time.time()))
            MongoDb.update(proxy)
