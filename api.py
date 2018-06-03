import sys
sys.path.insert(0, '../')
import flask
from dbs.mongo_db import MongoDb
import json
import random
from config import API_PORT


class Api(object):
    __app = flask.Flask(__name__)

    @__app.route('/')
    def api():
        args = flask.request.args
        try:
            num = int(args.get('count'))
            assert num
        except:
            return '获取代理池有误！请重新获取'
        else:
            cur = list(MongoDb.get('available'))
            cur.sort(key=lambda x: x['delay'])
            for i in range(len(cur)):
                cur[i].pop('_id')
            if len(cur) < num:
                return json.dumps(cur)
            else:
                return json.dumps(random.sample(cur, num))

    def __call__(self, *args, **kwargs):

        Api.__app.run(port=API_PORT)


def api():
    print('web接口服务器开启，正在提供服务')
    api = Api()
    api()

