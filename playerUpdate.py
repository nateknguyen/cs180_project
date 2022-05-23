import playerDataStore
import json
from decimal import Decimal

#update player data to csv
def updatePlayer(name, season, draftRound, dnumberInput, age, pts, reb, ast):
    playerList = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    netRating = Decimal()
    for player in playerList:
        if player['player_name'] == name and player['season'] == season:
            player['draft_round'] = str(draftRound)
            player['draft_number'] = str(dnumberInput)
            player['age'] = str(age)
            player['pts'] = str(pts)
            player['reb'] = str(reb)
            player['ast'] = str(ast)
            points = Decimal(player['pts']) * Decimal('0.5')
            rebounds = Decimal(player['reb']) * Decimal('0.3')
            assists = Decimal(player['ast']) * Decimal('0.2')
            netRating = (points + rebounds + assists)

    with open('sumData.json', 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)

    sum = Decimal(data['sum'])
    tot = Decimal(data['tot'])

    if data['player_name'] == playerList[0]['player_name']:
        sum += netRating
        tot += 1

    data['sum'] = str(sum)
    data['tot'] = str(tot)

    playerDataStore.writeDataToJSON('sumData.json', data)

    playerDataStore.writeDataToJSON(playerDataStore.PLAYERS_JSON_DATA, playerList)

    return playerList
