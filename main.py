# --- MAIN SCRAPING SANTEHMOLL --
import csv

from sqlalchemy import  create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///DB_Santehmoll_scraping.db', echo=True, future=True)
Base = declarative_base()
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __repr__(self):
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


adTexts = {
'url': 'https://ad.admitad.com/g/dra8qamlvk037e654884d22e56a5b7/?f_id=18282&ulp=https%3A%2F%2Fsantehmoll.ru%2Fproduct%2Fagger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker%2F%3Futm_source%3Dadmitad%26utm_medium%3Dpartner-network&i=5',
'clearurl': 'https://santehmoll.ru/product/agger_exact_a2121100_odnozakhvatnyy_smesitel_dlya_vanny_dusha_s_dlinnym_povorotnym_izlivom_350_mm_ker/',
'name': 'Смеситель для ванны Agger Exact A2121100',
'shortname': 'Смеситель для ванны',
'id': '215841',
'vendor': 'Agger',
'vendorCode': 'A2121100',
'price': '5090',
'oldprice': '7090',
'picture': 'https://santehmoll.ru/wa-data/public/shop/products/41/58/215841/images/221567/221567.970.jpg',
'serie': 'Exact',
'avaible': 'В наличии',
'groupName': '_215841_Смеситель для ванны Agger Exact A2121100',
'keyPhrases': ['Agger A2121100', 'A2121100', 'Exact A2121100', 'Смеситель для ванны A2121100'],
'mainTitle': ['Смеситель для ванны Exact A2121100', 'Смеситель для ванны Agger A2121100'],
'subTitle': ['В Наличии. Доставка', 'Быстрая доставка. В Наличии'],
'text': ['Смеситель для ванны Agger Exact A2121100', 'Смеситель для ванны Agger Exact A2121100'],
'suburl': '#Agger#'
}


# --- MAIN PROGRAMM SCRIPTS ---
def creatingNewAds():
    # Base.metadata.create_all(engine)
    with Session(engine) as session:
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([patrick])
        session.commit()

def checkAvaible():
    print('Check Avaible')

def errorsCorrection():
    print('errorsCorrection')


# --- OTHER FUNCTIONS ---



# Create Error log csv file for correction
def addErrorToCSV(self, needtosendsomething=0):
    # if not self.__items: enter - "url don't work"

    # Create table for 'Error log'. If table headers don't exist they will created
    # !!!!Not good design. Think!
    try:
        with open('Log_Errors.csv', encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
        with open('Log_Errors.csv', 'a', newline='') as file:
            table_value = []
            writer = csv.writer(file, delimiter=';')
            for i in self.all_data:
                table_value.append(self.all_data[i])
            writer.writerow(table_value)
    except:
        with open('Log_Errors.csv', 'a', newline='') as file:
            table_title = []
            table_value = []
            writer = csv.writer(file, delimiter=';')
            for i in self.all_data:
                table_title.append(i)
                table_value.append(self.all_data[i])
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

