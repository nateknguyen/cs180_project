from unittest import result
import playerName
import csv
import json
from decimal import Decimal

CALCULATED_NET_RATING_PLAYER = 'netRatingOfPlayer.json'

def calculateNetRating(name):
    players = playerName.getPlayerListFromJSON()
    resultList = list()
    for player in players:
        if player['player_name'] == name:
            if player['season'] != None:
                points = Decimal(player['pts']) * Decimal('0.5')
                rebounds = Decimal(player['reb']) * Decimal('0.3')
                assists = Decimal(player['ast']) * Decimal('0.2')
                netRating = (points + rebounds + assists)
                player['net_rating'] = str(netRating)
            resultList.append(player)    

    with open(playerName.FILE_NAME, 'w', newline='') as file:
        csvWriter = csv.DictWriter(file, fieldnames=playerName.columns)
        csvWriter.writeheader()
        for elem in players:
            csvWriter.writerow(elem)

    with open(playerName.PLAYERS_JSON_DATA, 'w') as jsonf:
        jsonString = json.dumps(players, indent=4)
        jsonf.write(jsonString)

    with open(CALCULATED_NET_RATING_PLAYER, 'w') as jsonf:
        jsonString = json.dumps(resultList, indent=4)
        jsonf.write(jsonString)

    return resultList
