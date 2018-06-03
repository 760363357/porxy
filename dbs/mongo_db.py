import pymongo


class MongoDb(object):
    __mog = pymongo.MongoClient()
    __db = __mog['ProxyPool']
    __con = __db['pool']
    __con.ensure_index('proxyip', unique=True)

    # __con.drop()

    @classmethod
    def insert(cls, date_dict):
        status = 0
        try:
            cls.__con.insert(date_dict)
            print(f'插入{date_dict}代理成功！')
            status = 1
        except pymongo.errors.DuplicateKeyError as e:
            print(f'插入{date_dict}数据重复！')
        return status


    @classmethod
    def update(cls, data_dict):
        cls.__con.update({'proxyip': data_dict['proxyip']}, {'$set': {'delay': data_dict['delay'],
                                                                      'last_time': data_dict['last_time']}})
        print(f'更新{data_dict}数据成功！')

    @classmethod
    def get(cls, mothed='all'):
        if mothed == 'all':
            cur = cls.__con.find().sort('delay', pymongo.ASCENDING)
        elif mothed == 'available':
            cur = cls.__con.find({'delay': {'$gte': '0'}}).sort('delay', pymongo.ASCENDING)
        else:
            cur = cls.__con.find({'delay': {'$gte': '-1'}})
        print(f'成功查询到{cur.count()}条数据')
        return cur



