import requests as request
import csv
import os

def main():
    item_id = input('Item ID: ')

    if int(item_id) > 36700:
        print('Item ID out of range')
        return

    price = getPrice(item_id)
    name = getName(item_id)
    if price == -1:
        response = str(name) + ' is not available.'
    else:
        response = 'The cheapest ' + str(name) + ' costs: ' + str(price) + ' gil'
    print(response)

################################

def getName(itemID):
    f = open(os.path.join('items.csv'))
    items_file = csv.reader(f)

    for row in items_file:
        if row[0] == itemID:
            f.close()
            return row[1]
    f.close()
    return 'NotFound'

def getPrice(itemID):
    result = request.get('https://universalis.app/api/Lich/' + itemID)
    try:
        price = result.json()['listings'][1]['pricePerUnit']
    except:
        price = -1
        return int(price)

    return int(price)

if __name__ == "__main__":
    main()