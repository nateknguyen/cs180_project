import playerDataStore


#update player data to csv
def updatePlayer(name, season, draftRound, age, pts, reb, ast):
    playerList = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)

    for player in playerList:
        if player['player_name'] == name and player['season'] == season:
            player['draft_round'] = draftRound
            player['age'] = age
            player['pts'] = pts
            player['reb'] = reb
            player['ast'] = ast

    playerDataStore.writeDataToJSON(playerDataStore.PLAYERS_JSON_DATA, playerList)

    return playerList
