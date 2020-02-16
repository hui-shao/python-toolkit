import requests
import json

url = "https://get.xunfs.com/app/listapp.php"
hea = {"User-Agent": "Mozilla/4.0 compatible; MSIE 6.13; Windows NT 5.1;SV1", "Accept-Encoding": "gzip"}
par = {"a": "get18", "system": "android", "v": "2.2.4"}
r = requests.post(url, headers=hea, data=par)
dic = json.loads(r.text)
print("原响应：\n%s\n" % (dic))
print("地址：")
print(dic["url1"])
print(dic["url2"])
print("%s\n" % (dic["url3"]))
