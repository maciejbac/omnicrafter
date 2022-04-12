import requests as request
import csv
import os
from django.conf import settings

def getName(itemID):
    f = open(os.path.join(settings.BASE_DIR, 'files/items.csv'))
    items_file = csv.reader(f)

    for row in items_file:
        if row[0] == itemID:
            f.close()
            return row[1]
    f.close()

def getPrice(itemID):

    result = request.get('https://universalis.app/api/Lich/' + itemID)

    try:
        price = result.json()['listings'][1]['pricePerUnit']
    except:
        price = 'Not available'
        return price

    return str(price) + 'gil'
