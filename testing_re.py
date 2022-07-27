import re
import csv
from unittest import result
from Class_product_card import Product
import time
from Dictionary_shortName import titles_pattern


# title = re.sub(r'\s*\b{}\b'.format(series), '', self.product['name'], re.IGNORECASE)
# result = re.findall(r'\s*\b{}\b'.format(titles), '', name) 

""" title = re.sub(r'\s*\b{}\b'.format(series), '', self.product['name'], re.IGNORECASE)
 result = re.findall(r'\s*\b{}\b'.format(titles), '', name) """

row = {'available': 'true', 'categoryId': 'Мебель для ванной/Мебель 40 - 50 см', 'currencyId': 'RUB', 'delivery': 'true', 
                    'description': '', 'id': '225836', 'modified_time': '1657693026', 
                    'name': 'Тумба белый глянец/ясень шимо 44,7 см Акватон Вита 1A221401VTD70', 'oldprice': '', 'pickup': 'true', 
                    'picture': 'https://santehmoll.ru/wa-data/public/shop/products/36/58/225836/images/386839/386839.970.jpg', 
                    'price': '7510.00', 'shop-sku': '1A221401VTD70', 'type': '', 
                    'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2F1a221401vtd70%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5', 
                    'vendor': 'Акватон', 'vendorCode': '1A221401VTD70', 'weight': '9.680'}
row1 = {'available': 'true', 'categoryId': 'Сантехника/Раковины', 'currencyId': 'RUB', 'delivery': 'true', 'description': '', 'id': '210400', 'modified_time': '1654944331', 'name': 'Раковина 53х38 см Bien Dune DNLG05301FD0W3000', 'oldprice': '19660.00', 'pickup': 'true', 'picture': 'https://santehmoll.ru/wa-data/public/shop/products/00/04/210400/images/207954/207954.970.jpg', 'price': '12780.00', 'shop-sku': 'DNLG05301FD0W3000', 'type': '', 'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2Fdune_rakovina_na_stoleshnicu_530kh380kh130%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5', 'vendor': 'Bien', 'vendorCode': 'DNLG05301FD0W3000', 'weight': '8.800'}


def getType():
    name = 'Коврик Aquanet MA3172L'
    vendor = 'Hansgrohe'
    vendorCode = '72020000'
    series = 'Talis S'
    titles = 'Смеситель для раковины'
    result = False
    
    for title in titles_pattern:
        result = re.search(r'{}'.format(title), name)
        if result: 
            return result.group()        

    return "No title in library"

def repl():

    #print(getType())



    # i = 0
    # with open('all.csv', encoding='utf-8', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile, delimiter=';')
    #     with open('title.csv', 'a', encoding='utf-8', newline='') as file:
    #         writer = csv.writer(file, delimiter=';')
    #         for row in reader:
    #             i += 1
    #             #card_object = Product()
    #             ad_title = Product.adTitle(row)

    #             writer.writerow([row['id'], row['url'], row['name'], ad_title])
    #             print(f'Success! - ID: {row["id"]} Numer: {i}')


# Checking string len:
                #     if len_title > 56:
                #     correct_marker = 'Too long'
                # elif len_title <= 56:
                #     correct_marker = 'Accepted'
                # elif len_title < 56*0.33:
                #     correct_marker = 'Too short'
                # else:
                #     correct_marker = 'Error len defenition'


if __name__ == "__main__":
    repl()