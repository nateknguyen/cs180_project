import csv
import playerName
import json


#update player data to csv
def updatePlayer(playerList):
    playerData = playerName.getPlayerListFromJSON()
    searchData = list()


    for player in playerData:
        if player['player_name'] == playerName:
            searchData.append(player)
    
    return searchData
