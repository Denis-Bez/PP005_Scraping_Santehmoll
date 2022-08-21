import re
import csv
from datetime import datetime
from unittest import result
from Class_product_card import Product
from Class_API_Yandex import API_Requests
import time
from Dictionary_shortName import titles_pattern
from Dictionary_TextCorrecting import correct_Text
from datetime import date
import json


adTexts = {
'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2Fagger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5',
'clearurl': 'https://santehmoll.ru/product/agger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker/',
'name': 'Верхний душ Hansgrohe Raindance E Air 1jet 400×400 мм, ½’ 26252000',
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


def getType(a, b=0):
    print(f'{a}-{b}')
        

def repl():
    
    adTexts = '[135463, 2313, 12313]'

    OldPrice_Update = []
    
    for i in eval(adTexts):
                diction = {}
                diction['Id'] = i
                diction['TextAd'] = {'PriceExtension': {'OldPrice': 0}}
                OldPrice_Update.append(diction)
    
    print(OldPrice_Update)



if __name__ == "__main__":
    repl()