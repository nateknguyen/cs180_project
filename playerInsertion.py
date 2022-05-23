import playerDataStore

#inserts player data to csv
def insertPlayer(newPlayerData):
    playerData = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    playerData.append(newPlayerData)

    playerDataStore.writeDataToJSON(playerDataStore.PLAYERS_JSON_DATA, playerData)

#gets last entry in the csv
def getNewestPlayer():
    playerData = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    return playerData[-1]    



