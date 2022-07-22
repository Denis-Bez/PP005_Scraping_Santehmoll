import requests, json
from config import CONFIG


def request_api():

# --- Input Date ---
    CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns/'
    AdGroupsURL = 'https://api-sandbox.direct.yandex.com/json/v5/adgroups/'
    AdsURL = 'https://api-sandbox.direct.yandex.com/json/v5/ads/'
    KeywordsURL = 'https://api-sandbox.direct.yandex.com/json/v5/keywords/'
    token = CONFIG['ACCESS_TOKEN']

    # Params
    SelectionCriteria = {
        
    }
    FieldNames = [
        'Id', 'Name',
    ]
    AdGroups = [{
        'Name': 'Новая группа',
        'CampaignId': '439275',
        'RegionIds': [213],
    }]


# --- Preparing and execution request ---
    headers = {'Authorization': 'Bearer ' + token, 
            'Accept-Language': 'ru',
            }

    # Create and coding body request
    body = {'method': 'add',
            'params': {
                        #'SelectionCriteria': SelectionCriteria,
                        #'FieldNames': FieldNames,
                        'AdGroups': AdGroups,
                    }}
    jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')

    # Get request
    result = requests.post(AdGroupsURL, jsonBody, headers=headers)

    print(result.json()['result'])


if __name__ == "__main__":
    request_api()