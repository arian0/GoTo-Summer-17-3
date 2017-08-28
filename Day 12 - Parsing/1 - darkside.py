import requests
import lxml.html as html



concerts = {}

def add_concert(name):
    global concerts
    name = name.lower().replace('.', '').replace(' /', ',').replace('/ ', ', ')
    for band in name.split(', '):
        if band in concerts:
            concerts[band] += 1
        else:
            concerts[band] = 1

url = "http://darkside.ru/show/index.phtml?cp={}"
for p in range(0, 8497, 144):
    print("downloading - {}".format(p))
    response = requests.get(url.format(p))
    page = html.fromstring(response.text)

    for elem in page.find_class('titleshow'):
        add_concert(elem.text_content())

    for elem in page.find_class('titles'):
        link = elem.find('./a')
        add_concert(link.text_content())

sorted_concerts = sorted(concerts.items(), key=lambda x:x[1], reverse=True)

for item in sorted_concerts:
    print('{} - {}'.format(item[0], item[1]))

