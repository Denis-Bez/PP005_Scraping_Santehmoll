import re
import csv
from unittest import result
from Class_product_card import Product
from Class_API_Yandex import API_Requests
import time
from Dictionary_shortName import titles_pattern
from Dictionary_TextCorrecting import correct_Text


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
    pass
        

def repl():

    adTexts = {
'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2Fagger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5',
'clearurl': 'https://santehmoll.ru/product/agger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker/',
'name': 'Смеситель для ванны Agger Exact A2121100',
'shortname': 'Смеситель для ванны',
'id': '215841',
'vendor': 'Agger',
'vendorCode': 'A2121100',
'price': '5090',
'oldprice': '7090',
'picture': 'https://santehmoll.ru/wa-data/public/shop/products/41/58/215841/images/221567/221567.970.jpg',
'serie': 'Exact',
'avaible': 'В наличии',
'groupName': '_215841_Смеситель для ванны Agger Exact A2121100',
'keyPhrases': ['Agger A2121100', 'A2121100', 'Exact A2121100', 'Смеситель для ванны A2121100'],
'mainTitle': ['Смеситель для ванны Exact A2121100', 'Смеситель для ванны Agger A2121100'],
'subTitle': ['В Наличии. Доставка', 'Быстрая доставка. В Наличии'],
'text': ['Смеситель для ванны Agger Exact A2121100', 'Смеситель для ванны Agger Exact A2121100'],
'suburl': '#Agger#'
}

    # code_text = RequestResult['error']['error_detail']
    
    # API_Req = API_Requests(adTexts)
    # response = API_Req.balance_Points()
    # print(response)

    # a = "Don't get it"

    # b = {
    #     "Key1": {
    #         "Key1-1": "Yep",
    #     },
    # }

    # if re.search(r"Don't", a):
    #     b["Key1"]["Key1-2"] = 'Two'


    params = {"Keywords": []}
    print(params)

    params["Keywords"].append({"Keyword": "key", "AdGroupId": "adGroupId", "Bid": "10000000",})
    params["Keywords"].append({"Keyword": "key", "AdGroupId": "adGroupId", "Bid": "100000ewrwr00",})

    print(params)

            

    # i = 0 
    # with open('all 50.csv', encoding='utf-8', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile, delimiter=';')
    #     for row in reader:
    #         i += 1
    #         if i > 2:
    #             return
    #         card_object = Product(row)
    #         print(f'Number: {i}, Data: {card_object.DataForNewAd()}')
    
    





if __name__ == "__main__":
    repl()