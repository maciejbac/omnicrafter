import requests as request
import csv
import os

def main():

    answer = input('Would you like to search for an item with\n1. item ID\n2. Name\n')

    if answer == '1':
        item = input('Item ID: ')
        print(searchByID(item))

    elif answer == '2':
        item = input('Item Name: ')
        print(searchByName(item))

    else:
        print('Incorrect input')

    

###############################

def getCSraftingCost(item):
    print('yes')

def searchByName(item):
    item = getID(item)
    return searchByID(item)


def searchByID(input):
    item_id = input

    if int(item_id) > 36700:
        response = 'Item ID out of range'
        return response

    price = getPrice(item_id)
    name = getName(item_id)
    if price == -1:
        response = str(name) + ' is not available.'
    else:
        response = 'The cheapest ' + str(name) + ' costs: ' + str(price) + ' gil'
    return response

def getName(itemID):
    f = open(os.path.join('items.csv'))
    items_file = csv.reader(f)

    for row in items_file:
        if row[0] == itemID:
            f.close()
            return row[1]
    f.close()
    return 'NotFound'

def getID(itemName):
    f = open(os.path.join('items.csv'))
    items_file = csv.reader(f)

    for row in items_file:
        if str(row[1]).lower() == str(itemName).lower():
            f.close()
            return row[0]
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