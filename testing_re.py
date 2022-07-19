import re
import csv

#https://santehmoll.ru/product/1a221401vtd70/
#https%3A%2F%2Fsantehmoll.ru%2Fproduct%2F1a221401vtd70 %2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5

str = 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2F1a221401vtd70%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5'


# str = re.split(r'&ulp=', str, maxsplit=1)[1]
# str = re.split(r'%3F', str, maxsplit=1)[0]
str = re.findall(r"&ulp=(.+)(?=%3F)", str)[0]

# May be better: https://overcoder.net/q/43486/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D1%80%D0%BE%D0%BA-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8
str = re.sub('%2F', '/', str)
str = re.sub('%3A', ':', str)

with open('all.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    with open('clearlinks.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        i = 0
        for row in reader:
            i += 1
            str = re.findall(r"&ulp=(.+)(?=%3F)", row['url'])[0]
            str = re.sub('%2F', '/', str)
            str = re.sub('%3A', ':', str)
            writer.writerow([row['id'], str, row['url']])
            print(f'Success! - ID: {row["id"]}. Номер: {i}')