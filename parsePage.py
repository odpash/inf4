import requests
import bs4
import json


def getHtml():
    h = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    return requests.get('https://itmo.ru/ru/schedule/0/P3114/schedule.htm', headers=h).text


def parseToJson(text):
    lessons = []
    soup = bs4.BeautifulSoup(text, features='html.parser').find('article', {'class': 'content_block'})
    days = soup.find_all('h4', {'class': 'rasp_day_mobile'})
    contents = soup.find_all('div', {'class': 'rasp_tabl_day'})
    for i in range(len(days)):
        d1 = contents[i].find_all('td', {'class': 'time'})
        lesson = contents[i].find_all('td', {'class': 'lesson'})
        format_lesson = contents[i].find_all('td', {'class': 'lesson-format'})
        for x in range(len(d1)):
            time = d1[x].find('span').text.strip()
            week = d1[x].find('div').text.strip()
            audience = d1[x].find('dd').text.strip()
            place = d1[x].find('dt').text.strip()
            lesson_name = lesson[x].find('dd').text.strip()
            person_name = lesson[x].find('b').text.strip()
            lesson_format = format_lesson[x].text.strip()
            print(time, week, audience, place, lesson_name, person_name, lesson_format)
        break
        day_name = days[i].text.strip()
        time = contents[i].find('td', {'class': 'time'}).text.strip()
        print(day_name, time)
    exit(0)
    """
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
    """



def write(js):
    with open('result.json', 'w', encoding='UTF-8') as outfile:
        json.dump(js, outfile, ensure_ascii=False)
    outfile.close()

def main():
    write(parseToJson(getHtml()))
main()
