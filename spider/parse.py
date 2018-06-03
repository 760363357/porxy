from lxml import etree
import re


class Parse(object):
    @staticmethod
    def _parse(key, rule, result_list, response, method):
        if method == 'xpath':
            html = etree.HTML(response)
            res = html.xpath(rule)
        elif method == 're':
            res = re.findall(rule, response, re.S)
        else:
            res = []
            print('解析数据错误，不知名解析类型！')
        assert res
        if not result_list:
            for r in res:
                d = {}
                d[key] = r
                result_list.append(d)
        else:
            for r in range(min(len(res), len(result_list))):
                result_list[r][key] = res[r]

    @staticmethod
    def re_parse(key, rule, result_list, response):
        res = re.findall(rule, response, re.S)
        assert res
        if not result_list:
            for r in res:
                d = {}
                d[key] = r
                result_list.append(d)
        else:
            for r in range(min(len(res), len(result_list))):
                result_list[r][key] = res[r]

    @staticmethod
    def parse(key, rule, result_list, response, method='xpath'):
        if method == 'xpath':
            if '/' in rule:
                Parse._parse(key, rule, result_list, response, method)
        else:
            if '(' in rule:
                Parse._parse(key, rule, result_list, response, method)


