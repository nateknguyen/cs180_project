import csv
import playerName
import json


#inserts player data to csv
def insertPlayer(newPlayerData):
    playerData = playerName.getPlayerListFromJSON()
    playerData.append(newPlayerData)

    with open(playerName.FILE_NAME, 'w', newline='') as file:
        csvWriter = csv.DictWriter(file, fieldnames=playerName.columns)
        csvWriter.writeheader()
        for elem in playerData:
            csvWriter.writerow(elem)

    with open(playerName.PLAYERS_JSON_DATA, 'w') as jsonf:
        jsonString = json.dumps(playerData, indent=4)
        jsonf.write(jsonString)


    

    
#gets last entry in the csv
def getNewestPlayer():
    playerData = playerName.getPlayerListFromJSON()
    return playerData[-1]    



