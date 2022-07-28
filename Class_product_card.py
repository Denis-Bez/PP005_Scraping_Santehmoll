import time
import random
import re
from user_agent import user_agent_data
from Dictionary_shortName import titles_pattern, correct_shortName_utf8
from Dictionary_TextCorrecting import cleaning_url, correct_vendor, correct_vendorCode

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
        self.series = self.getSeries()
        self.shortName = self.getShortName()


# --- Other methods ---


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


# Is Generated and return dictionary with all necessay data for creating ads
# DRY!!!! Don't forgot example all_data = {self.getUpdate(), self.id ...}
    def forCreateNewAd(self):
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
        self.type = self.getType()

        GroupName = self.nameAdGroup()
    
        all_data = {}

        for a in all_data:
            if re.search(r'{Error!}', all_data[a]):
                self.addErrorToCSV()
                return False


    # Is Generated dictionary for updating avaible and correcting price
    def getUpdate(self):
        self.id = self.product['id']
        self.avaible = self.getAvaible()
        self.price = self.getPrice()
        self.oldprice = self.getOldPrice()
 

    def addErrorToCSV(self):
        pass
        # if not self.__items: enter - "url don't work"


# --- Scraping data for create ads ---
    
    # Checking avaible of item
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
            return series
        except Exception:
            print("Error reading 'series'")
            return False
        
    
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
            return oldprice
        except Exception:
            print("Error reading 'oldprice'")
            return False
    

    # Is being cleared url from partner's id
    def getCleanurl(self):
        cleanurl = re.findall(r"&ulp=(.+)(?=%3F)", self.product['url'])[0]    

        # Replacement reserved url-symbols
        for v in cleaning_url:
            cleanurl = re.sub(v, cleaning_url[v], cleanurl)

        return cleanurl


    # Getting short product's name
    def getShortName(self):
        
        # Searching short pattern in long name
        for title in titles_pattern:
            result = re.search(r'{}'.format(title), self.product['name'])
            if result:
                # Checking for non-Cyrillic: 
                for c in correct_shortName_utf8:
                    result = re.sub(c, correct_shortName_utf8[c], result)
                return result.group().capitalize()

        return "Product Is not found in 'Dictionary_shortName'"


# --- Ad texts create and validation ---  

    # Return ad's group name
    def nameAdGroup(self):
        try:
            nameAdGroup = '_' + self.product['id'] + '_' + self.product['name']
            return nameAdGroup
        except:
            return "Couldn't extract 'id' or 'name'"
    
    # Return a list of key phreses for the ad group
    def keyPhrases(self):
        keyPhrases = []
        self.series
        self.shortName
        vendor = self.product['vendor']
        vendorCode = self.product['vendorCode']

        # Clear from prohibited simbols (for series, vendor and vendorCode)
        for c in correct_vendor:
            vendor = re.sub(c, correct_vendor[c], vendor)
        for c in correct_vendorCode:
            vendor = re.sub(c, correct_vendorCode[c], vendor)

         
        #re.sub("\.", "", a)
        # No more 7 phrases

        
		# For phrase's algorithm 'Vendor + VendorCode'
        # Checking length of VendorCode for a separate phrase
        if (re.findall('[a-zA-Zа-яА-я]', vendorCode) and len(vendorCode) > 5) or (
            not re.findall('[a-zA-Zа-яА-я]', vendorCode) and len(vendorCode) > 7):
            keyPhrases.append(vendorCode)
            
		
        # For phrase's algorithm 'series + VendorCode'
        #if self.series:
            
		
        # For phrase's algorithm 'series + VendorCode'

        # For phrase's algorithm  'shortName + vendorCode'

        

        return keyPhrases


        

        


