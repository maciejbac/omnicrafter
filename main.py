import os, csv
import requests as request

def main():

    answer = input('Would you like to search for an item with\n1. Recipe\n2. Name\n3. Item ID\n4. All profitable recipes\nAnswer: ')

    if answer == '1':
        print('Recipes:')

        f = open(os.path.join('recipes.csv'))
        items_file = csv.reader(f)

        itemArray = []
        for row in items_file:
                itemArray.append(row)
        f.close()

        itemCount = 1
        for item in itemArray:
            print(str(itemCount) + '. ' + item[0])
            itemCount = itemCount + 1

        answer = int(input(''))
        workingItem = itemArray[answer-1][0]
        itemYield, cost, value, profit = getCraftingCost(workingItem)
        print(workingItem)
        print('Total price to craft ' + str(itemYield) + ' ' + workingItem + ' is: ' + str(int(cost)) + ' gil')
        print('Total sale price of ' + str(itemYield) + ' ' + workingItem + ' is: ' + str(int(value)) + ' gil')
        print('Profit per craft: ' + str(int(profit)) + ' gil')

    elif answer == '2':
        item = input('Item Name: ')
        print(searchByName(item))


    elif answer == '3':
        item = input('Item ID: ')
        print(searchByID(item))

    elif answer == '4':
        f = open(os.path.join('recipes.csv'))
        items_file = csv.reader(f)

        itemArray = []
        for row in items_file:
                itemArray.append(row)
        f.close()

        for i in range(0, len(itemArray)):
            i = int(i)
            workingItem = itemArray[i][0]
            itemYield, cost, value, profit = getCraftingCost(workingItem)
            if(profit > 0):
                print(workingItem)
                print('Profit per craft: ' + str(int(profit)) + ' gil')
                print('')

    else:
        print('Incorrect input')

def getCraftingCost(item):
    value = getPrice(getID(item))

    matsArray = searchMats(item)
    itemYield = int(matsArray.pop(0))

    # reset cost vaule
    cost = 0

    for material in matsArray:
        materialID = getID(material)
        materialPrice = getPrice(materialID)
        cost = cost + materialPrice

    value = value * itemYield
    profit = value - cost

    return itemYield, cost, value, profit



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
    return 'Not Found'

def getPrice(itemID):
    result = request.get('https://universalis.app/api/Lich/' + itemID)
    try:
        price = result.json()['listings'][1]['pricePerUnit']
    except:
        price = -1

    return int(price)

def getCrystals():
    crystalStack = []
    
if __name__ == "__main__":
    main()
