import csv
import json

FILE_NAME = "all_seasonsTest.csv"
PLAYERS_JSON_DATA = "players.json"

def initializePlayerTableToJSON():
    jsonArray = []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
       csvReader = csv.DictReader(f)

       for row in csvReader:
           trimData = {'player_name':row['player_name'], 'age':row['age'], 'draft_round':row['draft_round'], 'draft_number':row['draft_number'], 'pts':row['pts'], 'reb':row['reb'], 'ast':row['ast'], 'season':row['season']}
           jsonArray.append(trimData)

    writeDataToJSON(PLAYERS_JSON_DATA, jsonArray)

def readDataFromJSON(fileName):
    with open(fileName, 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
    
    dataList = list(data)

    return dataList

def writeDataToJSON(fileName, DateToWrite):    
    with open(fileName, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(DateToWrite, indent=4)
        jsonf.write(jsonString)
