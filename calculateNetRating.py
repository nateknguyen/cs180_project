import playerDataStore
from decimal import Decimal
import json

CALCULATED_NET_RATING_PLAYER = 'netRatingOfPlayer.json'

def calculateNetRatingOnePlayer(jsonFileToRead):
    players = playerDataStore.readDataFromJSON(jsonFileToRead)
    resultList = list()
    sum = 0
    for player in players:
        points = Decimal(player['pts']) * Decimal('0.5')
        rebounds = Decimal(player['reb']) * Decimal('0.3')
        assists = Decimal(player['ast']) * Decimal('0.2')
        netRating = (points + rebounds + assists)
        sum += netRating
        player['net_rating'] = str(netRating)
        resultList.append(player)

    with open('sumData.json', 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)

    if len(players) != Decimal(data['tot']) or players[0]['player_name'] != data['player_name']:
        sumData = {'player_name':players[0]['player_name'], 'sum':str(sum), 'tot':str(len(players))}
        playerDataStore.writeDataToJSON('sumData.json', sumData)
    
    playerDataStore.writeDataToJSON(jsonFileToRead, resultList)

    return resultList

def calculateNetRatingDraftRound(jsonFileToRead):
    players = playerDataStore.readDataFromJSON(jsonFileToRead)
    resultList = list()
    sum = 0
    for player in players:
        points = Decimal(player['pts']) * Decimal('0.5')
        rebounds = Decimal(player['reb']) * Decimal('0.3')
        assists = Decimal(player['ast']) * Decimal('0.2')
        netRating = (points + rebounds + assists)
        sum += netRating
        player['net_rating'] = str(netRating)
        resultList.append(player)

    sumData = {'draft_round':players[0]['draft_round'], 'sum':str(sum), 'tot':str(len(players))}
    
    playerDataStore.writeDataToJSON('sumData.json', sumData)

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

def calculateAverageNetRating():
    with open('sumData.json', 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
    
    sum = Decimal(data['sum'])
    tot = Decimal(data['tot'])

    average = sum / tot
#store sum 
# on update average check in json file sum, tot  sum += new player data  net rating
    result = "{:.2f}".format(average)

    return result