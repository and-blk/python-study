#!/usr/bin/python3.6


import urllib.request
import bs4
import csv

d = {'date', 'value', 'change'}
page = "https://news.yandex.ru/quotes/2002.html"
op_page = urllib.request.urlopen(page)
soup = bs4.BeautifulSoup(op_page.read(), 'html.parser')
htm_txt = soup.find_all('tr')
iter = 0
list_list = []
list_all = []
for i in htm_txt:
    iter += 1
    if iter == 1:
        continue
    l = list(i)
    list_list.append(l)

for item in list_list:
    date_clear = item[0].text.strip()
    value_clear = item[1].text.strip()
    change_clear = item[2].text.strip()
    list_all.append({'date': date_clear, 'value': value_clear, 'change': change_clear})


print("{}   {}   {}".format("Date", "Value", "Changed"))
for item in list_all:
    print(item)

csv_file = open('/opt/python/parsing/csv_file', 'w')
with csv_file:
    fields = ['date', 'value', 'change']
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    for i in list_all:
        writer.restval
