import time
import random
from user_agent import user_agent_data

import requests
from bs4 import BeautifulSoup

# Object is certain product in catalog
class Product:

    # Correct input data to 'row'
    def __init__(self, url):
        # self.id =             # From feed
        # self.name =           # From feed
        self.url = url          # From feed
        # self.cleanurl =       # From url
        # self.vendor =         # From feed
        # self.vendorCode =     # From feed
        # self.picture =        # From feed
        # self.series =         # From site
        # self.type =           # From site
        # self.avaible =        # From site
        # self.price =          # From site
        # self.oldprice =       # From site
        self.row = {'available': 'true', 'categoryId': 'Мебель для ванной/Мебель 40 - 50 см', 'currencyId': 'RUB', 'delivery': 'true', 
                    'description': '', 'id': '225836', 'modified_time': '1657693026', 
                    'name': 'Тумба белый глянец/ясень шимо 44,7 см Акватон Вита 1A221401VTD70', 'oldprice': '', 'pickup': 'true', 
                    'picture': 'https://santehmoll.ru/wa-data/public/shop/products/36/58/225836/images/386839/386839.970.jpg', 
                    'price': '7510.00', 'shop-sku': '1A221401VTD70', 'type': '', 
                    'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2F1a221401vtd70%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5', 
                    'vendor': 'Акватон', 'vendorCode': '1A221401VTD70', 'weight': '9.680'}


# Getting 'html' and object 'soup' and checking link working and server response. Try 3 times open link
    def getSoup(self):        
        for i in range(1, 4):
            try:
                headers = {'user-agent': random.choice(user_agent_data), 'accept': '*/*'}
                html = requests.get(self.row['url'], headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    self.__items = soup.find('div', class_='content')
                    return print('All good!')
                return f'Status code {html.status_code}'    
            except Exception as e:
                print(f"Something went wrong, {e}. Repeat {i}")
                time.sleep(i*5)
            
        return False


    def getAvaible(self):
        try:
            self.avaible = self.__items.find('div', class_='p-available').get_text(strip=True) 
        except Exception:
            print("Error reading 'p-available'")
            self.avaible = 'Ссылка не работает'

        return self.avaible
    
    def clenurl(self):
        pass
        

        


