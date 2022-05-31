from decimal import Decimal
import calculateNetRating
import playerDataStore
import playerSearch
import json

CALCULATED_DRAFT_ROUND_RATING = 'draftRoundRating.json'
#CALCULATED_NET_RATING_PLAYER = 'netRatingOfPlayer.json'


def readPlayersDraftRoundRating(season, draftRound):
    playerList = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    result = list()
    for player in playerList:
        if player['draft_round'] == draftRound and player['season'] == season:
            trimData = {'player_name':player['player_name'], 'age':player['age'], 'draft_number':player['draft_number'], 'draft_round':player['draft_round'], 'pts':player['pts'], 'reb':player['reb'], 'ast':player['ast'], 'net_rating':'N/A'}
            result.append(trimData)

    playerDataStore.writeDataToJSON(CALCULATED_DRAFT_ROUND_RATING, result)

    result = calculateNetRating.calculateNetRatingDraftRound(CALCULATED_DRAFT_ROUND_RATING)

    return result

