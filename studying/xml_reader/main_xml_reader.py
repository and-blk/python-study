
from lxml import etree
data = {}
list_data = []

with open('./xml_file.xml', 'rb') as xmlf:
    tree = etree.parse(xmlf)
    root = tree.getroot()
    for i in root:
        children = i.getchildren()
        for a in i:
            data[a.tag] = a.text
        list_data.append(data)

for item in list_data:
    for i in item:
       print(str(i) + ' ' + str(item[i]))
    print('-----------------------')

with open('./out_xml.xml', 'wb') as xmlout:
    root_list = ['books', 'strings']
    for i in root_list:
        root = etree.Element(i)
        for book in list_data:
            element = etree.SubElement(root, 'book')
            print(item.items())
            for key, value in book.items():
                child = etree.SubElement(element, key)
                child.text = value
        et = etree.ElementTree(root)
        et.write(xmlout, xml_declaration=True, encoding='utf-8', pretty_print=True)




