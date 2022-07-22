# Scraping Santehmoll
# Main Block

import csv



# Function reading url from "avaible_sm.csv" and writing "avaible" into avaible.csv
# !May be separate reading and writing
def readwrite():
    i = 0  # Just counter

    # Create table for data sсraping
    # with open('avaible.csv', 'a', newline='') as file:
    #     writer = csv.writer(file, delimiter=';')
    #     writer.writerow(['id', 'url', 'avaible'])

    # Open file with all url
    with open('avaible_sm.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            print(row)




if __name__ == "__main__":
    readwrite()

