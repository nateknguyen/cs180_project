import json
import playerDataStore


FILE_NAME = "all_seasonsTest.csv"
PLAYERS_JSON_DATA = "players.json"
columns = ['', 'player_name', 'team_abbreviation', 'age', 'player_height', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']
obj = json.load(open(PLAYERS_JSON_DATA))


def deletePlayer(name, season):
    playerList = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    
    for index in range(len(playerList)):
        if playerList[index]['player_name'] == name and playerList[index]['season'] == season:
            playerList.pop(index)
            break

    playerDataStore.writeDataToJSON(playerDataStore.PLAYERS_JSON_DATA, playerList)

    return playerList

