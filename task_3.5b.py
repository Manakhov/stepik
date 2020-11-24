import requests
import json
import sys

client_id = '68599a8966fff2fce4bd'
client_secret = '2d2b0e952780f5b2b556a1ad4aea39ce'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI1ZmJkMGIxZmJhNTQxYTA5MThkOGI5N2MiLCJleHAiOjE2MDY4Mjk0NzEsImlhdCI6MTYwNjIyNDY3MSwiYXVkIjoiNWZiZDBiMWZiYTU0MWEwOTE4ZDhiOTdjIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjVmYmQwYjFmYTM5MjgyMDAxMjQwZTM3NCJ9.Tfw4rua_6QlB6UDNVsrA8mRsPBs1B8i5l09jAEF7dkU'
headers = {"X-Xapp-Token": token}
list = []
for ident in sys.stdin:
    ident = ident.rstrip()
    r = requests.get("https://api.artsy.net/api/artists/" + ident, headers=headers)
    j = json.loads(r.text)
    list.append(j['birthday'] + j['sortable_name'])
    # print(j['sortable_name'])
# print(list)
list.sort()
for name in list:
    print(name[4:])
