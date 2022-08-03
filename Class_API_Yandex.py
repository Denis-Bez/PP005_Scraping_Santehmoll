import requests, json
from config import CONFIG


CampaignId = '76829270'

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


# --- Create ad ---
 
    # Create new Compaign
    def add_Compaign(self):
        method = 'add'
        params = {
                    "Campaigns": [{
                        "Name": "Тестовая компания_01", # Need dinamyc Generate parametrs
                        "StartDate": "2022-08-03", # Need dinamyc Generate parametrs
                        "DailyBudget":{
                            "Amount": "300000000",
                            "Mode":"STANDARD",
                        },
                        "NegativeKeywords": { # Need dinamyc Generate parametrs
                            "Items": ['или', '!как', '!кого', '!кто', '!ли', '!не', '!сантех', '!сиденье', '!чего', '!чем', '!что', '[!для смесителя]'],
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
        return self.Send_Request(body, self.__serviceURL['campaignsURL'])


    # Create new ad Group and ads in Group
    def add_adGroup(self):
        method = 'add'
        params = {
                "AdGroups": [{
                    "Name": self.adTexts['groupName'],
                    "CampaignId": CampaignId,
                    "RegionIds": ["225"],
                }]
        }

        body = self.create_Body(method, params)
        #groupId = self.Send_Request(body, self.__serviceURL['adgroupsURL'])
        #!!!Need to get Group id to created ads
        return self.add_Ads(groupId)


    # Create new 3 ads (input: id adgroup)
    def add_Ads(self, groupId):
        method = 'add'
        for i in range(0, 3):
            params = {
                "Ads": [{
                    "AdGroupId": groupId,
                    "TextAd": {
                        "Title": self.adTexts['mainTitle'][i],
                        "Title2": self.adTexts['subTitle'][i],
                        "Text": self.adTexts['text'][i],
                        "Href": self.adTexts['url'],
                        "Mobile": "NO", # Need to change to create mobile ads
                        "DisplayUrlPath":self.adTexts['suburl'],
                        #"SitelinkSetId": (long), # ?????????
                        #"AdExtensionIds": [(long), ... ], # ?????????
                        "PriceExtension": {
                            "Price": self.adTexts['price']*1000000,
                            # "OldPrice": 0, # Invite if exist
                            "PriceCurrency": "RUB",
                        },
                    },
                }]
            }        
            body = self.create_Body(method, params)
            return self.Send_Request(body, self.__serviceURL['campaignsURL'])


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
                "CampaignId": CampaignId,  # Need to connect with create compaign
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
        return self.Send_Request(body, self.__serviceURL['vcard']) # Need correct return
    

    # Create set extension for ads (return: 'AdExtensionIds' for add_Ads())
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
    

    # Create set fast links for ads (return: 'SitelinkSetId' for add_Ads()) 
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


# --- Getting information ---

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

    # Count the groups in the campaign (input: compaign id, return: count groups)
    def GroupsCount(self, CampaignId):
        method = 'get'
        params = {
                    'SelectionCriteria': { 'CampaignIds': CampaignId },
                    'FieldNames': ['Id']
                 }
        
        body = self.create_Body(method, params)
        result = self.Send_Request(body, self.__serviceURL['adgroupsURL'])['result']['AdGroups']
        
        return len(result)
    

    # Getting information about all company
    def getCampaigns(self):
        method = 'get'
        params = {
                    'SelectionCriteria': {"States":["ON"]},
                    'FieldNames': ['Id', 'Name', 'Status'],
                 }
        
        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['campaignsURL'])