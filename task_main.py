import json


def main(js):
    write_xml(build_xml(js))


def read_json():
    return json.loads(open('start_file.json', encoding='UTF-8').read())


def build_xml(js):
    text = "<array>\n"
    for e in js:
        text += f'\t<lecture>\n\t\t<day>{e["day"]}</day>\n\t\t<time>{e["time"]}</time>\n\t\t<audience>{e["audience"]}</audience>\n\t\t<place>{e["place"]}</place>\n\t\t<name>{e["name"]}</name>\n\t\t<lector>{e["lector"]}</lector>\n\t\t<format>{e["format"]}</format>\n\t\t<week>{e["week"]}</week>\n\t</lecture>\n'
    text += '</array>'
    return text


def write_xml(t):
    f = open('taskMain.xml', 'w', encoding='UTF-8')
    f.write(t)
    f.close()
