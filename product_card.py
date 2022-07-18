import time
import random
from user_agent import user_agent_data

import requests
from bs4 import BeautifulSoup

# Object is certain product in catalog
class Product:


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

# Getting 'html' and object 'soup' and checking link working and server response. Try 3 times open link
    def getSoup(self):        
        for i in range(1, 4):
            try:
                headers = {'user-agent': random.choice(user_agent_data), 'accept': '*/*'}
                html = requests.get(self.url, headers=headers)
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
    
    def display(self):
        print(self.__items)

        


