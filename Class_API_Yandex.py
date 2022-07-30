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


    # Create new ad Group
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
        #id = self.Send_Request(body, self.__serviceURL['adgroupsURL'])
        #!!!Need to get Group id to created ads
        return self.add_Ads(id)


    # Create new 3 ads (input: id adgroup)
    def add_Ads(self, id):
        pass

    # Delete Campaign by 'id'
    def deleteCampaign(self, CampaignId):
        method = 'delete'
        params = {
                    'SelectionCriteria': { 'Ids': [CampaignId] }
                 }
        
        body = self.create_Body(method, params)
        return self.Send_Request(body, self.__serviceURL['campaignsURL'])


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
    

    # TODO
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