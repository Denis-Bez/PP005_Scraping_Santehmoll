import re
import csv


# What about "DRY"?! May be better: https://overcoder.net/q/43486/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D1%80%D0%BE%D0%BA-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8
def repl(str):
    str = re.sub('%2F', '/', str)
    str = re.sub('%3A', ':', str)

    str = re.sub('%25D1%2580%25D0%25BA', 'рк', str)
    str = re.sub('%25E2%2580%2599', '’', str)
    str = re.sub('%3D', '=', str)
    str = re.sub('%25D0%25B0%25D1%2581', 'ас', str)
    str = re.sub('%25D0%25BA', 'к', str)
    str = re.sub('%25E2%2584%25961', '№1', str)

    return str


with open('all.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    with open('clearlinks.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        i = 0
        for row in reader:
            i += 1
            str = re.findall(r"&ulp=(.+)(?=%3F)", row['url'])[0]
            str = repl(str)
            writer.writerow([row['id'], str, row['url']])
            print(f'Success! - ID: {row["id"]}. Номер: {i}')