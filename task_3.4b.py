import requests
import re

link = "https://pastebin.com/raw/hfMThaGb"
req = requests.get(link)
print(req.text)
print(re.findall(r"<a[^>]*?href=[\"'](.*?)[\"'][^>]*?>", req.text))
