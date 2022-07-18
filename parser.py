# Scraping Santehmoll

import csv



# Reading avaible information from got html
def read_avaible(items):
    
    try:
        avaible = items.find('div', class_='p-available').get_text(strip=True) 
    except Exception:
        print("Error reading 'p-available'")
        avaible = 'Ссылка не работает'

    return avaible


# Choice random header for request not to was blocked
def random_headers():

    user_agent = user_agent_data
    headers = {'user-agent': random.choice(user_agent), 'accept': '*/*'}

    return headers


# Get information about avaible poriduct from site-page
def get_content(url):

    # Trying extract data 3 times
    for i in range(1, 4):
        try:
            headers = random_headers()
            html = requests.get(url, headers=headers)
            soup = BeautifulSoup(html.text, 'html.parser')
            items = soup.find('div', class_='content')
            return read_avaible(items)
        except Exception:
            print(f"Something went wrong. Repeat {i}")
            time.sleep(i*20)
        
    return 'Ссылка не работает'


# Function reading url from "avaible_sm.csv" and writing "avaible" into avaible.csv
# !May be separate reading and writing
def readwrite():
    i = 0  # Just counter

    # Create table 'avaible.csv'
    with open('avaible.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['id', 'url', 'avaible'])

    # Open file with all url
    with open('avaible_sm.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            for i in range(1, 4):
                try:
                    headers = random_headers()
                    html = requests.get(row['url'], headers=headers)
                    soup = BeautifulSoup(html.text, 'html.parser')
                    items = soup.find('div', class_='content')
                    return print('Working')
                except Exception:
                    print(f"Something went wrong. Repeat {i}")
                    time.sleep(i*20)

        # Check all product
        # for row in reader:
        #     avaible = get_content(row['url'])
        #     i+=1
        #     # Write avaible infomation into file "avaible.csv"
        #     with open('avaible.csv', 'a', encoding='utf-8', newline='') as file:
        #         writer = csv.writer(file, delimiter=';')
        #         writer.writerow([row['id'], row['url'], avaible])
        #     print(f'Проверенно: {i} позиций. Статус: {avaible}')
        #     time.sleep(random.randint(2,10))



if __name__ == "__main__":
    readwrite()

