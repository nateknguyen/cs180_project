import csv
import playerName

#inserts player data to csv
def insertPlayer(newPlayerData):
    playerData = playerName.getPlayerTable()
    data = [len(playerData)] + newPlayerData
    with open(playerName.FILE_NAME, 'a', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
    return newPlayerData

#gets last entry in the csv
def getNewestPlayer():
    playerData = playerName.getPlayerTable()
    return playerData[-1]    
