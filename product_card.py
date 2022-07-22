import time
import random
import re
from user_agent import user_agent_data

import requests
from bs4 import BeautifulSoup


# Object is certain product in catalog
class Product:

    
    def __init__(self, product):
        # self.product = {'available': 'true', 'categoryId': 'Мебель для ванной/Мебель 40 - 50 см', 'currencyId': 'RUB', 'delivery': 'true', 
        #             'description': '', 'id': '225836', 'modified_time': '1657693026', 
        #             'name': 'Тумба белый глянец/ясень шимо 44,7 см Акватон Вита 1A221401VTD70', 'oldprice': '', 'pickup': 'true', 
        #             'picture': 'https://santehmoll.ru/wa-data/public/shop/products/36/58/225836/images/386839/386839.970.jpg', 
        #             'price': '7510.00', 'shop-sku': '1A221401VTD70', 'type': '', 
        #             'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2F1a221401vtd70%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5', 
        #             'vendor': 'Акватон', 'vendorCode': '1A221401VTD70', 'weight': '9.680'}
        self.product = product
        self.cleanurl = self.getCleanurl()
        self.__items = self.getSoup()
        # self.type =           # From site


# Getting 'html' and object 'soup' and checking link working and server response. Try 3 times open link
    def getSoup(self):        
        for i in range(1, 4):
            try:
                headers = {'user-agent': random.choice(user_agent_data), 'accept': '*/*'}
                html = requests.get(self.cleanurl, headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    items = soup.find('div', class_='content')
                    return items
                return f'Status code {html.status_code}'    
            except Exception as e:
                print(f"Something went wrong, {e}. Repeat {i}")
                time.sleep(i*5)            
        return False


# Is Generated dictionary with all necessay data for creating ads
# DRY!!!! Don't forgot
    def getProductCard(self):
        self.id = self.product['id']
        self.name = self.product['name']
        self.url = self.product['url']
        self.vendor = self.product['vendor']
        self.vendorCode = self.product['vendorCode']
        self.picture = self.product['picture']
        self.avaible = self.getAvaible()
        self.series =  self.getSeries()
        self.price = self.getPrice()
        self.oldprice = self.getOldPrice()


# Is Generated dictionary for updating avaible and correcting price
    def getUpdate(self):
        self.id = self.product['id']
        self.avaible = self.getAvaible()
        self.price = self.getPrice()
        self.oldprice = self.getOldPrice()


# Is being cleared url of partner's id
    def getCleanurl(self):
        # What about "DRY"?! May be better: https://overcoder.net/q/43486/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D1%80%D0%BE%D0%BA-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8
        cleanurl = re.findall(r"&ulp=(.+)(?=%3F)", self.product['url'])[0]    
        cleanurl = re.sub('%2F', '/', cleanurl)
        cleanurl = re.sub('%3A', ':', cleanurl)
        cleanurl = re.sub('%25D1%2580%25D0%25BA', 'рк', cleanurl)
        cleanurl = re.sub('%25E2%2580%2599', '’', cleanurl)
        cleanurl = re.sub('%3D', '=', cleanurl)
        cleanurl = re.sub('%25D0%25B0%25D1%2581', 'ас', cleanurl)
        cleanurl = re.sub('%25D0%25BA', 'к', cleanurl)
        cleanurl = re.sub('%25E2%2584%25961', '№1', cleanurl)

        return cleanurl


# Getting data for create ads
    def getAvaible(self):
        try:
            avaible = self.__items.find('div', class_='p-available').get_text(strip=True)
        except Exception:
            print("Error reading 'p-available'")
            avaible = "Couldn't scraping avaible"
        return avaible
    

    def getSeries(self):
        try:
            series = self.__items.find(itemprop='model').get_text(strip=True)
        except Exception:
            print("Error reading 'series'")
            seriess = "Couldn't scraping series"
        return series
    

    def getPrice(self):
        try:
            price = self.__items.find(itemprop='price').get_text(strip=True)
        except Exception:
            print("Error reading 'price'")
            price = "Couldn't scraping price"
        return price


    def getOldPrice(self):
        try:
            oldprice = self.__items.find('span', class_='p-price__compare-at-price').get_text(strip=True)
        except Exception:
            print("Error reading 'oldprice'")
            oldprice  = "Couldn't scraping oldprice"
        return oldprice
    

    def getType(product):
        type = product['name']
        type = re.findall(r"(.+)(?= {})".format(product['vendor']), type)

        return type

        

        


