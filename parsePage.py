import requests
import yaml
import sys
import json


def getHtml():
    h = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    return requests.get('https://itmo.ru/ru/schedule/0/P3114/schedule.htm', headers=h).text


def parseToJsonV1(text):
    lessons = []
    text = text.replace("class='rasp_day_mobile'>", 'class="rasp_day_mobile">')
    for dayText in text.split('class="rasp_day_mobile">')[1::]:
        if '<dt style="font-size:14px;">' in dayText:
            week = dayText.split('<dt style="font-size:14px;">')[1].split("</dt>")[0].strip()

        else:
            week = ""
        dayText = dayText.split('</table></div>')[0]

        dayName = dayText.split('<span>')[1].split("</span")[0].strip()
        for i in dayText.split(' <td class="time">')[1::]:
            timePeriod = i.split("<span>")[1].split("</span>")[0].strip()
            audience = i.split('<dd class="rasp_aud_mobile">')[1].split("</dd>")[0].strip()
            place = i.split('<i class="fa fa-map-marker"></i><span>')[1].split('</span>')[0].strip()
            lessonInfo = i.split('<td class="lesson">')[1].split('</td>')[0]
            lessonName = lessonInfo.split("<dd>")[1].split("</dd>")[0].strip()
            lector = lessonInfo.split("<b>")[1].split("</b>")[0].strip()
            if '</a>' in lector:
                lector = lector.split("</a>")[1].strip()
            formatLesson = lessonInfo.split('<td class="lesson-format">')[1].split("</td>")[0].strip()
            lessons.append({
                "day": dayName,
                "time": timePeriod,
                "audience": audience.replace(" ауд.", ''),
                "place": place,
                "name": lessonName,
                "lector": lector,
                "format": formatLesson,
                "week": week
            })

    return lessons


def parseToYaml(js):
    #sys.stdout.write(yaml.dump(js, allow_unicode=True))
    res = []
    for i in js:
        fl = False
        for j in i.keys():
            if not fl:
                fl = True
                res.append(f"- {j}: {i[j]}")
            else:
                res.append(f'  {j}: {i[j]}')
    return res, js


def write(y, js):
    with open('result.json', 'w', encoding='UTF-8') as outfile:
        json.dump(js, outfile, ensure_ascii=False)
    outfile.close()

    with open('result.yaml', 'w', encoding='UTF-8') as outfile:
        for i in y:
            outfile.write(i)
            outfile.write('\n')
    outfile.close()


def main():
    a, b = parseToYaml(parseToJsonV1(getHtml()))
    write(a, b)
main()
