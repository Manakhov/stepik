import requests
import re

A = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
res_A = requests.get(A)
res_B = requests.get(B)
html_find_A = re.findall(r"<a href=\"([\S]+)\"", res_A.text)
for html in html_find_A:
    res_C = requests.get(html)
    html_find_C = re.findall(r"<a href=\"([\S]+)\"", res_C.text)
    if B in html_find_C:
        print("Yes")
        break
else:
    print("No")
