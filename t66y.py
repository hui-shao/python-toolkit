import requests

url = "https://get.xunfs.com/app/listapp.php"
hea = {"User-Agent":"Mozilla/4.0 compatible; MSIE 6.13; Windows NT 5.1;SV1","Accept-Encoding":"gzip"}
par = {"a":"get18","system":"android","v":"2.2.4"}

r = requests.post(url,headers=hea,data=par)
print(r.text)
