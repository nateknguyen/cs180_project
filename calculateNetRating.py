import playerDataStore
from decimal import Decimal

CALCULATED_NET_RATING_PLAYER = 'netRatingOfPlayer.json'

def calculateNetRating(jsonFileToRead):
    players = playerDataStore.readDataFromJSON(jsonFileToRead)
    resultList = list()

    for player in players:
        points = Decimal(player['pts']) * Decimal('0.5')
        rebounds = Decimal(player['reb']) * Decimal('0.3')
        assists = Decimal(player['ast']) * Decimal('0.2')
        netRating = (points + rebounds + assists)
        player['net_rating'] = str(netRating)
        resultList.append(player)

    playerDataStore.writeDataToJSON(jsonFileToRead, resultList)

    return resultList

def getMaxNetRating(playerList):
    max = Decimal(playerList[0]['net_rating'])
    for player in playerList:
        if max < Decimal(player['net_rating']):
            max = Decimal(player['net_rating'])
    
    return max

def getMinNetRating(playerList):
    min = Decimal(playerList[0]['net_rating'])
    for player in playerList:
        if min > Decimal(player['net_rating']):
            min = Decimal(player['net_rating'])

    return min

def calculateAverageNetRating(playerList):
    sum = 0
    for player in playerList:
        sum += Decimal(player['net_rating'])

    result = "{:.2f}".format(sum / len(playerList))

    return result