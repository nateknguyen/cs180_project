import pandas

FILE_NAME = "all_seasonsTest.csv"

def getPlayerTable():
    players = pandas.read_csv(FILE_NAME, sep=",")

    dataSet = list()
    for data in players.iloc:
        data.pop('Unnamed: 0')
        dataSet.append(data.to_dict())

    return dataSet

def searchPlayerByName(playerList, playerName):
    playerData = getPlayerTable()
    searchData = list()

    for player in playerData:
        if player['player_name'] == playerName:
            searchData.append(player)
    
    return searchData

def searchPlayerByDraftYear(playerList, playerDraftYear):
    playerData = getPlayerTable()
    searchData = list()

    for player in playerData:
        if player['draft_year'] == playerDraftYear:
            searchData.append(player)

    return searchData

def searchPlayerBySeason(playerList, playerSeason):
    playerData = getPlayerTable()
    searchData = list()

    for player in playerData:
        if player['season'] == playerSeason:
            searchData.append(player)
    
    return searchData