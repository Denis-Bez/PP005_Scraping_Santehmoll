# --- MAIN SCRAPING SANTEHMOLL --
# --- Input data: csv file name: ".csv"---
import csv, re
from datetime import datetime

from sqlalchemy import  create_engine, select, update
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import declarative_base, Session

from Class_API_Yandex import API_Requests
from Class_product_card import Product


engine = create_engine('sqlite:///DB_Santehmoll_scraping.db', future=True)
Base = declarative_base()


class Groups_Ads(Base):
    __tablename__ = "groups_ads"
    id = Column(Integer, unique=True, primary_key=True)
    clearurl = Column(String, unique=True, nullable=False)
    name = Column(String)
    product_id = Column(Integer, unique=True, nullable=False)
    price =  Column(Integer)
    old_price =  Column(String)
    picture = Column(String)
    avaible = Column(String(25))
    vCardId = Column(Integer, nullable=False)
    CampaignId = Column(Integer, nullable=False)
    time = Column(DATETIME, default=datetime.utcnow)
    compaign_number = Column(Integer, nullable=False)
    Ads_Id = Column(String)

    def __repr__(self):
         return f"Group_Ads(id={self.id!r}, name={self.name!r}, product_id={self.product_id!r})"


# --- MAIN PROGRAMM SCRIPTS ---
def creatingNewAds():
    
    session = Session(engine)
    
    # Exctrction last ad's date from database
    last_Ad = session.query(Groups_Ads).order_by(Groups_Ads.time.desc()).first()
    
    # Create table
    # Base.metadata.create_all(engine)

    # Reading csv feed
    with open('all 50.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            # Checking available id in database
            if not session.query(Groups_Ads).filter(Groups_Ads.product_id==int(row['id'])).all():
                # Filtering Feed. Only if price >= 20000 and skipping SETs
                if int(row['price'].replace('.00','')) >= 20000 or ( re.search(r"SET", row['vendorCode']) and len(re.findall(r'\w+', row['vendorCode'])) > 2 ):
                    scrapingProduct = Product(row)
                    adTexts = scrapingProduct.DataForNewAd()
                    if adTexts[0]:
                        API_Req = API_Requests(adTexts[1])
                        response = API_Req.add_Compaign(last_Ad)
                        if response[0]:
                            save_to_Databse(response, session, adTexts[1])
                            print(f'Successfully create company: {row["name"]} Id: {row["id"]}')
                        else:
                            addErrorToCSV(adTexts[1], response[1])
                            print(f'Error API request: {response[1]}')
                    else:
                        addErrorToCSV(adTexts[1])
                        print('Error scraping data')
            else:
                print(f"Сompany doesn't match: {row['name']} Id: {row['id']} Price: {row['price']}")
    
    # Send to moderation For convert to list - eval(sess.Ads_Id)

def errorsCorrection():
    pass



def checkAvaible():
    print('Check Avaible')


# --- OTHER FUNCTIONS ---

def save_to_Databse(new_adGroup, session, adTexts):
    newAdGrpoup = Groups_Ads(
        clearurl=adTexts['clearurl'], 
        name=adTexts['name'], 
        product_id=adTexts['id'], 
        price=adTexts['price'], 
        old_price=adTexts['oldprice'], 
        picture=adTexts['picture'], 
        avaible=adTexts['avaible'], 
        vCardId=new_adGroup[1], 
        CampaignId=new_adGroup[0], 
        compaign_number=new_adGroup[3],
        Ads_Id=str(new_adGroup[2])
    )

    session.add_all([newAdGrpoup])
    session.commit()

# Create Error log csv file for correction
def addErrorToCSV(error_data, error_API='None'):

    # Create table for 'Error log'. If table headers don't exist they will created
    # !!!!Not good design. Think!
    try:
        # Was except if 'Log_Errors.csv' don't exist
        with open('Log_Errors.csv', encoding='utf-8', newline='') as csvfile:
            csv.DictReader(csvfile, delimiter=';')
        with open('Log_Errors.csv', 'a', newline='') as file:
            table_value = []
            writer = csv.writer(file, delimiter=';')
            for i in error_data:
                table_value.append(error_data[i])
            table_value.append(error_API)
            writer.writerow(table_value)
    except:
        with open('Log_Errors.csv', 'a', newline='') as file:
            table_title = []
            table_value = []
            writer = csv.writer(file, delimiter=';')
            for i in error_data:
                table_title.append(i)
                table_value.append(error_data[i])
            table_title.append('API_Error')
            table_value.append(error_API)
            writer.writerow(table_title)
            writer.writerow(table_value)


# --- START --
if __name__ == "__main__":
    
    print('\n1.Creating new ads\n2.Check avaible\n3.Errors Correction\n')
    type_algorithm = input('Input script number that you want to do:')
    print(type_algorithm)
    if type_algorithm == '1':
        creatingNewAds()
    elif type_algorithm == '2':
        checkAvaible()
    elif type_algorithm == '3':
        errorsCorrection()

