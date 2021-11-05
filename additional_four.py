import csv


def main(js):
    with open('output.tsv', 'wt', encoding='UTF-8') as out_file:
        for i in js:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(['day', i['day'], 'time', i['time'], 'audience', i['audience'], 'place', i['place'], 'name', i['name'], 'lector', i['lector'], 'format', i['format'], 'week', i['week']])



