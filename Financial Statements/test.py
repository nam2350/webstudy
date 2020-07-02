import OpenDartReader

api_key = '6f7c4a97fbac7c000f8a17c677f64faaddcfd094'
dart = OpenDartReader(api_key)

# samsung = dart.list('삼성전자', kind='A', start='2019-01-01', end='2019-12-31')
# print(samsung)

# test = dart.finstate_all('삼성전자',2019,11011)
# print(test)

test2 = dart.company('삼성전자')
# print(test2)

# name = test2['corp_name'];
# stock = test2['stock_name'];
# addr = test2['adres'];
# ceo = test2['ceo_nm'];

# doc = {'이름' : name, '주식명': stock, '주소' : addr, '대표' : ceo}
# print(doc);

print(dart.finstate('삼성전자', 2019, reprt_code='11013'))
