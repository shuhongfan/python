"""
@Time ： 2021/11/30 15:29
@Auth ： 021321752215舒洪凡
@File ：33.py
@IDE ：PyCharm
"""

import requests
import requests_ftp
requests_ftp.monkeypatch_session()
url = 'ftp://192.168.40.14'
s = requests.Session()
res = s.list(url, auth=('anonymous', ''))
res.encoding = 'gbk'
print(res.text)
