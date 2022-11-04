from Class_API_Yandex import API_Requests
from Class_product_card import Product
import csv

import main_Smoll

def checkAvaible():
    count = 0
    current_data = main_Smoll.Groups_Ads.Scrap_current_data()
    
    for row in current_data:
        new = []    
        new.append(row.id)
        status = API_Requests(0).GetStatus_Ads(row.Ads_Id)
        new.append(status)
        count+=1
        print(count)

        with open('checking.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(new)

if __name__ == "__main__":
    checkAvaible()
