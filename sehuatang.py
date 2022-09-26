import requests
from lxml import etree
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['name', 'magnet'])

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

for i in range(1, 735):
    base_url = 'https://hjhdt.8fo3.com/forum-103-' + str(i) + '.html'
    response = requests.get(url=base_url, headers=headers)
    html = etree.HTML(response.text)
    href_url = html.xpath('//table[@id="threadlisttableid"]//a[@class="s xst"]/@href')
    for href in href_url:
        try:
            href_url = 'https://hjhdt.8fo3.com/' + href
            href_response = requests.get(url=href_url, headers=headers)
            href_html = etree.HTML(href_response.text)
            name = href_html.xpath('//*[@id="thread_subject"]/text()')[0]
            magnet = href_html.xpath('//*[@class="blockcode"]//ol/li/text()')[0]
            ws.append([name, magnet])
            wb.save('学习资料.xlsx')
            print(name, magnet)
        except:
            pass

wb.close()
