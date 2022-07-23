import requests, json
from config import CONFIG


class API_Requests:

    
    def __init__(self):
        self.__token = CONFIG['ACCESS_TOKEN']
        self.__headers = {
                            'Authorization': 'Bearer ' + self.__token, 
                            'Accept-Language': 'ru'
                        }
        self.__serviceURL = {
                            'campaignsURL': 'https://api-sandbox.direct.yandex.com/json/v5/campaigns/',
                            'adgroupsURL':  'https://api-sandbox.direct.yandex.com/json/v5/adgroups'
                            }


    def Send_Get_Request(self, body, serviceURL):
        jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
        result = requests.post(serviceURL, jsonBody, headers=self.__headers)

        return result.json()
    

    def create_Body(self, method, params):
        body = {
                'method': method,
                'params': params
                }   

        return body


# Getting information about all company
    def getCampaigns(self):
        method = 'get'
        params = {
                    'SelectionCriteria': {},
                    'FieldNames': ['Id', 'Name', 'Status']
                 }
        
        body = self.create_Body(method, params)

        return self.Send_Get_Request(body, self.__serviceURL['campaignsURL'])
    

# Delete Campaign by 'id'
    def deleteCampaign(self, CampaignId):
        method = 'delete'
        params = {
                    'SelectionCriteria': { 'Ids': [CampaignId] }
                 }
        
        body = self.create_Body(method, params)

        return self.Send_Get_Request(body, self.__serviceURL['campaignsURL'])

# TODO
    def archiveCampaign(self, CampaignId):
        pass


# Count the groups in the campaign
    def GroupsCount(self, CampaignId):
        method = 'get'
        params = {
                    'SelectionCriteria': { 'CampaignIds': [CampaignId] },
                    'FieldNames': ['Id']
                 }
        
        body = self.create_Body(method, params)

        result = self.Send_Get_Request(body, self.__serviceURL['adgroupsURL'])['result']['AdGroups']
        
        return len(result)
