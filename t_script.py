# -*- coding: utf-8 -*-
"""
@project:   Tools
@author:    bantao
@file:      t_script.py
@time:      2019-10-10 10:02
"""

import json
import pandas as pd
s_back = {"describe": "操作成功",
          "result": "{\"error_msg\":\"OK\",\"type\":\"第二代身份证背面\",\"issue_organization\":\"乐清市公安局\","
          "\"cropped_image \":\"\",\"error_code\":\"0\",\"validity\":\"2012.12.07-2032.12.07\","
          "\"bw_image\":\"\"}", "code": "200"}

s_former = {"describe": "操作成功",
            "result": "{\"birthday\":\"1979年6月27日\",\"ethnic\":\"汉\",\"id_number\":\"420111197906275604\","
            "\"address\":\"武汉市洪山区鲁磨路388-382号2号\",\"error_msg\":\"OK\",\"sex\":\"女\","
            "\"type\":\"第二代身份证\",\"cropped_image \":\"\",\"name\":\"林靓\",\"error_code\":\"0\","
            "\"bw_image\":\"\"}", "code": "200"}


print(s_back['result'])
print(json.loads(s_back['result']))
print(json.loads(s_former['result']))

item = json.loads(s_former['result'])
result = [(item['type'], item['name'], item['sex'], item['ethnic'],
          item['birthday'], item['address'], item['id_number'])]

df = pd.DataFrame(result)
df.columns = ['type', 'name', 'sex', 'ethnic', 'birthday', 'address', 'id_number']
df.to_excel('summary.xls')
