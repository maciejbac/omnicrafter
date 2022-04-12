import requests as request
import csv
import os

def main():

    answer = input('Would you like to search for an item with\n1. item ID\n2. Name\n3. Recipe\nAnswer: ')

    if answer == '1':
        item = input('Item ID: ')
        print(searchByID(item))

    elif answer == '2':
        item = input('Item Name: ')
        print(searchByName(item))

    elif answer == '3':
        answer = input('1. Pumpkin Potage\n2. Chilled Popoto Soup\nAnswer: ')
        if answer == '1':
            item = 'Pumpkin Potage'
        elif answer == '2':
            item = 'Chilled Popoto Soup'
        getCraftingCost(item)

    else:
        print('Incorrect input')

###############################

def getCraftingCost(item):
    value = getPrice(getID(item))
    print('The cheapest ' + item + ' costs: ' + str(value) + ' gil')

    matsArray = searchMats(item)
    itemYield = int(matsArray[0])
    matsArray.pop(0)

    cost = 0
    for material in matsArray:
        materialID = getID(material)
        materialPrice = getPrice(materialID)
        cost = cost + materialPrice

    value = value * itemYield
    profit = value - cost

    print('Total price to craft ' + str(itemYield) + ' ' + item + ' is: ' + str(int(cost)) + ' gil')
    print('Total sale price of ' + str(itemYield) + ' ' + item + ' is: ' + str(int(value)) + ' gil')
    print('Profit per craft: ' + str(int(profit)) + ' gil')




def searchMats(item):
    f = open(os.path.join('recipes.csv'))
    items_file = csv.reader(f)

    for row in items_file:
        if str(row[0]).lower() == str(item).lower():
            f.close()
            itemArray = []
            for entry in row:
                itemArray.append(entry)
            itemArray.pop(0)
            return itemArray
    f.close()
    return 'NotFound'

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