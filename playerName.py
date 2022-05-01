import csv
import json

FILE_NAME = "all_seasonsTest.csv"
PLAYERS_JSON_DATA = "players.json"

def convertPlayerTableToJSON():
    jsonArray = []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
       csvReader = csv.DictReader(f)

       for row in csvReader:
           jsonArray.append(row)

    with open(PLAYERS_JSON_DATA, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def getPlayerListFromJSON():
    with open(PLAYERS_JSON_DATA, 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
    
    dataList = list(data)

    return dataList

def searchPlayerByName(playerList, playerName):
    playerData = getPlayerListFromJSON()
    searchData = list()

    for player in playerData:
        if player['player_name'] == playerName:
            searchData.append(player)
    
    return searchData

def searchPlayerByDraftYear(playerList, playerDraftYear):
    playerData = getPlayerListFromJSON()
    searchData = list()

    for player in playerData:
        if player['draft_year'] == playerDraftYear:
            searchData.append(player)

    return searchData

def searchPlayerBySeason(playerList, playerSeason):
    playerData = getPlayerListFromJSON()
    searchData = list()

    for player in playerData:
        if player['season'] == playerSeason:
            searchData.append(player)
    
    return searchData