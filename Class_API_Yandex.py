import requests, json, re
from config import CONFIG
from datetime import date
from Dictionary_TextForAPIYandex import Compaings_name, NegativeKeywords, SitelinkSetId, AdExtensionIds, vCardId


# !!! Need to create comfortable Dictionary with setting
class API_Requests:

    
    def __init__(self, adTexts):
        self.__token = CONFIG['ACCESS_TOKEN']
        self.__headers = {
                            'Authorization': 'Bearer ' + self.__token, 
                            'Accept-Language': 'ru'
                        }
        self.__serviceURL = {
                            'campaignsURL': 'https://api.direct.yandex.com/json/v5/campaigns/',
                            'adgroupsURL':  'https://api.direct.yandex.com/json/v5/adgroups',
                            'dictionaries': 'https://api.direct.yandex.com/json/v5/dictionaries',
                            'vcard': 'https://api.direct.yandex.com/json/v5/vcards',
                            'adimages': 'https://api.direct.yandex.com/json/v5/adimages',
                            'sitelinks': 'https://api.direct.yandex.com/json/v5/sitelinks',
                            'adextensions': 'https://api.direct.yandex.com/json/v5/adextensions',
                            'keywords': 'https://api.direct.yandex.com/json/v5/keywords',
                            'Ads': 'https://api.direct.yandex.com/json/v5/ads',
                            }
        
        self.adTexts = adTexts


    def Send_Request(self, body, serviceURL):
        jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
        result = requests.post(serviceURL, jsonBody, headers=self.__headers)

        return result.json()
    

    def create_Body(self, method, params):
        body = {
                'method': method,
                'params': params
                }   

        return body


# --- CREATE ADS ---
 
    # Create new Compaign. It's main method for create ads
    # if error - deleted all chain
    def add_Compaign(self):
        
        # If current company already has 1000 Grours create new
        # TODO Take last compaign's id from database
        CampaignId = Compaings_name['SantehmollAPP_1']
        vCardId = vCardId['SantehmollAPP_1']
        if self.GroupsCount(Compaings_name['SantehmollAPP_1']) >= 1000:
            startdate = date.today().isoformat()
            method = 'add'
            params = {
                        "Campaigns": [{
                            "Name": "SantehmollAPP_1", # Need dinamyc Generate parametrs "SantehmollAPP_" + lastCompanyNumber + 1
                            "StartDate": startdate,
                            "DailyBudget":{
                                "Amount": "300000000",
                                "Mode":"STANDARD",
                            },
                            "NegativeKeywords": {
                                "Items": NegativeKeywords,
                            },
                            "TextCampaign": {
                                "BiddingStrategy": {
                                    "Search": {"BiddingStrategyType": "HIGHEST_POSITION",},
                                    "Network": {"BiddingStrategyType": "SERVING_OFF",},
                                },
                            }
                        }]
                    }
        
            body = self.create_Body(method, params)
            try:
                CampaignId = self.Send_Request(body, self.__serviceURL['campaignsURL'])
                CampaignId = CampaignId['result']['AddResults'][0]['Id']
                # Creating 'vCard'
                resultVCard = self.add_vCard(CampaignId)
                if resultVCard:
                    vCardId = resultVCard['AddResults'][0]['Id']
                else:
                    return "Error! Fail to create vCard"                    
            except:
                return f"Error! Fail to create new company {CampaignId}"
        
        # Create Ad's Group
        try:
            AdGroupId = self.add_adGroup(CampaignId)
            AdGroupId = AdGroupId['result']['AddResults'][0]['Id']
        except:
            return "Error! Fail to create new Ad's group"

        # Create Keywords
        try:
            self.add_Keywords(AdGroupId)['result']['AddResults'][0]['Id']
        except:
            return "Error! Fail to create new Ad's group"
        
        # Create Ad
        result = self.add_Ads(AdGroupId, vCardId)
        if not result[0]:
            return f"Error! Fail to create new Ads: {result[1]}"

        # TODO If don't have errors send to moderation
        return "Created!"


    # Create new ad Group and ads in Group
    def add_adGroup(self, CampaignId):
        method = 'add'
        params = {
                "AdGroups": [{
                    "Name": self.adTexts['groupName'],
                    "CampaignId": CampaignId,
                    "RegionIds": ["225", "977"],
                }]
        }

        body = self.create_Body(method, params)
        
        return self.Send_Request(body, self.__serviceURL['adgroupsURL'])
        

    # Create new 3 ads (input: id adgroup)
    def add_Ads(self, groupId, vCardId):
        method = 'add'
        for i in range(0, 2):
            params = {
                "Ads": [{
                    "AdGroupId": groupId,
                    "TextAd": {
                        "Title": self.adTexts['mainTitle'][i],
                        "Title2": self.adTexts['subTitle'][i],
                        "Text": self.adTexts['text'][i],
                        "Href": self.adTexts['url'],
                        "Mobile": "NO",
                        "DisplayUrlPath":self.adTexts['suburl'],
                        "VCardId": vCardId,
                        "SitelinkSetId": SitelinkSetId,
                        "AdExtensionIds": [AdExtensionIds],
                        "PriceExtension": {
                            "Price": int(self.adTexts['price'])*1000000,
                            "PriceQualifier": "NONE",
                            "PriceCurrency": "RUB",
                        },
                    },
                }]
            }
            # Invite 'old price' if it exist
            if not re.search(r"Don't", self.adTexts['oldprice']):
                params["Ads"][0]["TextAd"]["PriceExtension"]["OldPrice"] = int(self.adTexts['oldprice'])*1000000
            
            body = self.create_Body(method, params)
            result = self.Send_Request(body, self.__serviceURL['Ads'])
            try:
                result['result']['AddResults'][0]['Id']
            except:
                return [False, result]

        # Creating mobile ad the some as second ad
        params["Ads"][0]["TextAd"]["Mobile"] = "YES"
        body = self.create_Body(method, params)
        result = self.Send_Request(body, self.__serviceURL['Ads'])
        try:
            result['result']['AddResults'][0]['Id']
        except:
            return [False, result]
        
        return [True]


    # Invite Keywords in ad's group (input: id adgroup)
    def add_Keywords(self, adGroupId):
        method = 'add'

        params = {"Keywords": []}
        
        for key in self.adTexts['keyPhrases']:
            params["Keywords"].append({"Keyword": key, "AdGroupId": adGroupId, "Bid": "10000000",})
        
        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['keywords'])


    # Create vCard. Start to get vCard id and save it in
    def add_vCard(self, CampaignId):
        method = 'add'

        params = {
            "VCards": [{
                "CampaignId": CampaignId, 
                "Country": "Россия",
                "City": "Москва",
                "CompanyName": "Магазин сантехники СантехМолл",
                "WorkTime": "0;6;09;0;22;0",
                "Phone": {
                    "CountryCode": "8",
                    "CityCode": "800",
                    "PhoneNumber": "333-00-48",
                },
                "Street": "Рязанский пр-т",
                "House": "2",
                "Building": "3",
                "ExtraMessage": "У нас в магазине можно купить сантехнику отечественного и зарубежного производства по доступным ценам. Мы сотрудничаем с 60 брендами из Италии, Франциии, России, Испании и других стран.",
                "ContactEmail": "zakaz@santehmoll.ru",
                "Ogrn": "1167746096484",
            }]
        }

        body = self.create_Body(method, params)
        result =  self.Send_Request(body, self.__serviceURL['vcard'])
        print(result)
        return result.get('result', False)
    

    # Create set extension for ads (return: 'AdExtensionIds' for add_Ads()). Once for all company. Handly save in 'Dictionary_TextForAPIYandex'
    def adExtension(self):
        method = 'add'

        params = {
            "AdExtensions": [{
                "Callout": {"CalloutText": "Кредит, Рассрочка"},
                "Callout": {"CalloutText": "В Наличии"},
                "Callout": {"CalloutText": "Бережная доставка"},
                "Callout": {"CalloutText": "Поддержка 9:00-22:00"},
            }]
        }

        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['adextensions'])
    

    # Create set fast links for ads (return: 'SitelinkSetId' for add_Ads()). Once for all company. Handly save in 'Dictionary_TextForAPIYandex'
    def adSitelinks(self):
        method = 'add'

        params = {
            "SitelinksSets": [{
                "Sitelinks": [
                    {"Title": "Каталог сантехники", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?ulp=https%3A%2F%2Fsantehmoll.ru%2Fcategory%2Fsantekhnika%2F", "Description": "Большой выбор сантехники. Скидки и подарки. Доставка по РФ",},
                    {"Title": "Мебель для ванной", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?ulp=https%3A%2F%2Fsantehmoll.ru%2Fcategory%2Fmebel-dlya-vannoy%2F", "Description": "Каталог мебели для ванной комнаты. Скидки, уцененные товары",},
                    {"Title": "Инженерная сантехника", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?ulp=https%3A%2F%2Fsantehmoll.ru%2Fcategory%2Finzhenernaja-santehnika%2F", "Description": "Широкий выбор труб, арматуры, фасонных частей",},
                    {"Title": "Каталог скидок", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?ulp=https%3A%2F%2Fsantehmoll.ru%2Fdiscounts%2F", "Description": "Купить сантехнику со скидкой. Работаем с 2014 года",},
                    {"Title": "Доставка", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?subid=3&ulp=https%3A%2F%2Fsantehmoll.ru%2Fdostavka-i-oplata%2F%3Fshipping%3Ddostavka", "Description": "Аккуратная доставка по России и Москве",},
                    {"Title": "Сантехника в кредит", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?subid=3&ulp=https%3A%2F%2Fsantehmoll.ru%2Fsantekhnika-v-kredit%2F", "Description": "Купить сантехнику в кредит или рассрочку",},
                    {"Title": "Гарантия", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?subid=3&ulp=https%3A%2F%2Fsantehmoll.ru%2Fpriem-i-vozvrat-tovara%2F", "Description": "Получения и возврат товара, гарантия, сервис",},
                    {"Title": "Контакты", "Href": "https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?subid=3&ulp=https%3A%2F%2Fsantehmoll.ru%2Fkontakty%2F", "Description": "Организуем доставку заказа в любую точку России",},
                    ]
            }]
        }

        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['sitelinks'])


# --- GETTING INFORMATION ---

    # Getting list of region's codes (input: region that you want to find)
    def dictionry_regions(self, searchRegion):
        method = 'get'
        params = {
                    "DictionaryNames": ["GeoRegions"],
                 }
        
        body = self.create_Body(method, params)
        regions = self.Send_Request(body, self.__serviceURL['dictionaries'])
        regions = regions['result']['GeoRegions']

        for i in regions:
            if i["GeoRegionName"] == searchRegion:
                return i
        
        return "Region isn't found"
    

    # TODO Error "Not enough points" (https://yandex.ru/dev/direct/doc/examples-v5/python3-requests-points.html)
    def balance_Points(self):
        pass


    # Count the groups in the campaign. All groups including archived groups (input: compaign id, return: count groups)
    def GroupsCount(self, CampaignId):
        method = 'get'
        params = {
                    'SelectionCriteria': { 'CampaignIds': [CampaignId] },
                    'FieldNames': ['Id']
                 }
        
        body = self.create_Body(method, params)
        result = self.Send_Request(body, self.__serviceURL['adgroupsURL'])

        return len(result['result']['AdGroups'])
    

    # Getting information about all company
    def getCampaigns(self):
        method = 'get'
        params = {
                    'SelectionCriteria': {"States":["ON"]},
                    'FieldNames': ['Id', 'Name', 'Status'],
                 }
        
        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['campaignsURL'])