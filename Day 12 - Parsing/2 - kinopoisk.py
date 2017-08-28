#
import requests
import lxml.html as html

headers = {
    "Cookie": "_ym_uid=1491214362234308458; sessionid=b8d138ac6c1973fb5ae165acc54b681f; _ym_isad=1; csrftoken=4wwYvxIFpkd0KBYQQXAEIpTAMUD1AmaX; _ym_visorc_26396970=w"
}

url = "http://anytask.org/course/200/gradebook/"
result = requests.get(url, headers=headers)
page = html.fromstring(result.text)

for link in page.find_class('table-link'):
    print(link.text_content())

