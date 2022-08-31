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
    all_data = {'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2Frgw_pa_36_b_pa_06b_z_050_2b_derzh_13%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5', 'clearurl': 'https://santehmoll.ru/product/rgw_pa_36_b_pa_06b_z_050_2b_derzh_13/', 
    'name': 'Душевой уголок 80х70 см RGW PA-36-B (PA-06B+Z-050-2B+держатель) Passage 41083687-014 прозрачное', 'shortname': 'Душевой уголок', 'id': '103478899999', 
    'vendor': 'RGW', 'vendorCode': '41083687-014', 'price': '31443', 'oldprice': "Don't exist 'oldprice'", 
    'picture': 'https://santehmoll.ru/wa-data/public/shop/products/88/47/1034788/images/672844/672844.970.jpg', 'serie': 'Passage', 'avaible': 'Под заказ', 
    'groupName': '_103478899999_Душевой уголок 80х70 см RGW PA-36-B (PA-06B+Z-050-2B+держатель) Passage 41083687-014 прозрачное', 
    'keyPhrases': ['RGW 41083687-014', '41083687-014', 'Passage 41083687-014', 'Душевой уголок 41083687-014'], 
    'mainTitle': ['Душевой уголок Passage 41083687-014', 'Душевой уголок RGW 41083687-014'], 
    'subTitle': 'Error', 
    'text': "Error! Ad's text is too long", 'suburl': '#RGW#'}

    for key in all_data:
        try:
            if re.search(r'Error', all_data[key]):
                print(f'Try 1 Was work! {all_data[key]}')
        except:
            for i in all_data[key]:
                print(i)
                if re.search(r'Error', i):
                    print(f'Except Was work! {i}')
        


if __name__ == "__main__":
    repl()