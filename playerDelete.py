import csv
import json
import playerName


FILE_NAME = "all_seasonsTest.csv"
PLAYERS_JSON_DATA = "players.json"
columns = ['', 'player_name', 'team_abbreviation', 'age', 'player_height', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']



def deletePlayer(playerList, playerSeason, playerName):
    playerData = playerName.getPlayerListFromJSON()
    searchData = list()
    

    for player in playerData:
        if (player['player_name'] == playerName and player['season'] == playerSeason):
            searchData.remove(player)
    
    return searchData