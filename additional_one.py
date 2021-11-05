import xml.etree.ElementTree as ET


def main(js):
    root = ET.Element('array')
    for i in js:
        person = ET.SubElement(root, 'lecture')
        ET.SubElement(person, 'day').text = i['day']
        ET.SubElement(person, 'time').text = i['time']
        ET.SubElement(person, 'audience').text = i['audience']
        ET.SubElement(person, 'place').text = i['place']
        ET.SubElement(person, 'name').text = i['name']
        ET.SubElement(person, 'lector').text = i['lector']
        ET.SubElement(person, 'format').text = i['format']
        ET.SubElement(person, 'week').text = i['week']
    tree = ET.ElementTree(root)
    tree.write('additionalOne.xml', encoding='UTF-8')