RULE_LIST = [
{
        'name': '西刺代理IP网',
        'url_list': [f'http://www.xicidaili.com/nn/{page}' for page in range(1, 4)],
        'parse_type': 'xpath',
        'date_dict': {'proxyip': r'//table[@id="ip_list"]/tr/td[2]/text()',
                      'port': r'//table[@id="ip_list"]/tr/td[3]/text()',
                      'protocol_type': r'//table[@id="ip_list"]/tr/td[6]/text()',
                      'delay': '1.5',
                      'last_time': ''}

},
    {
        'name': '无忧代理',
        'url_list': ['http://www.data5u.com/free/gngn/index.shtml'],
        'parse_type': 'xpath',
        'date_dict': {'proxyip': r'//ul[@class="l2"]/span[1]/li/text()',
                      'port': r'//ul[@class="l2"]/span[2]/li/text()',
                      'protocol_type': r'//ul[@class="l2"]/span[4]/li/a/text()',
                      'delay': '1.5',
                      'last_time': ''}
},
{
        'name': '快代理',
        'url_list': [f'https://www.kuaidaili.com/free/inha/{page}/' for page in range(1, 4)],
        'parse_type': 're',
        'date_dict': {'proxyip': r'<td data-title="IP">(.*?)</td>',
                      'port': r'<td data-title="PORT">(.*?)</td>',
                      'protocol_type': r'<td data-title="类型">(.*?)</td>',
                      'delay': '1.5',
                      'last_time': ''}
    }


]

HEADER_INFO = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

VAILD_URL = {'http': 'http://www.httpbin.org/ip', 'https': 'https://www.baidu.com'}

THREAD_NUM = 50

DOWN_DELAY = 1.5

API_PORT = 2000