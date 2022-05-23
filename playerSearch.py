import playerDataStore

SEARCHED_PLAYER_DATA = 'searchedPlayer.json'

def searchPlayerByName(playerList, playerName):
    dataToStore = list()
    playerSearch = list()

    for player in playerList:
        if player['player_name'] == playerName:
            trimData = {'player_name':player['player_name'], 'age':player['age'], 'pts':player['pts'], 'reb':player['reb'], 'ast':player['ast'], 'net_rating':'N/A'}
            dataToStore.append(trimData)
            playerSearch.append(player)

    playerDataStore.writeDataToJSON(SEARCHED_PLAYER_DATA, dataToStore)

    return playerSearch

def searchPlayerByDraftRound(playerList, playerDraftRound):
    dataToStore = list()
    playerSearch = list()

    for player in playerList:
        if player['draft_round'] == playerDraftRound:
            trimData = {'player_name':player['player_name'], 'age':player['age'], 'pts':player['pts'], 'reb':player['reb'], 'ast':player['ast'], 'net_rating':'N/A'}
            dataToStore.append(trimData)
            playerSearch.append(player)

    playerDataStore.writeDataToJSON(SEARCHED_PLAYER_DATA, dataToStore)

    return playerSearch

def searchPlayerBySeason(playerList, playerSeason):
    dataToStore = list()
    playerSearch = list()

    for player in playerList:
        if player['season'] == playerSeason:
            trimData = {'player_name':player['player_name'], 'age':player['age'], 'pts':player['pts'], 'reb':player['reb'], 'ast':player['ast'], 'net_rating':'N/A'}
            dataToStore.append(trimData)
            playerSearch.append(player)

    playerDataStore.writeDataToJSON(SEARCHED_PLAYER_DATA, dataToStore)
    
    return playerSearch