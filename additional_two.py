import re
import xml.etree.ElementTree as ET


def main():
    a = open('start_file.json', 'r', encoding='UTF-8').read()
    r = re.split('"', a)[1::]
    lectures = []
    idx = 0
    lecture = []
    for i in range(2, len(r) - 1, 4):
        idx += 1
        lecture.append(r[i])
        if idx == 8:
            idx = 0
            lectures.append(lecture)
            lecture = []
    write(lectures)


def write(idx):
    root = ET.Element('array')
    for i in idx:
        person = ET.SubElement(root, 'lecture')
        ET.SubElement(person, 'day').text = i[0]
        ET.SubElement(person, 'time').text = i[1]
        ET.SubElement(person, 'audience').text = i[2]
        ET.SubElement(person, 'place').text = i[3]
        ET.SubElement(person, 'name').text = i[4]
        ET.SubElement(person, 'lector').text = i[5]
        ET.SubElement(person, 'format').text = i[6]
        ET.SubElement(person, 'week').text = i[7]
    tree = ET.ElementTree(root)
    tree.write('additionalTwo.xml', encoding='UTF-8')
