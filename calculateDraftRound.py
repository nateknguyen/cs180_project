from flask import redirect, Flask, request, render_template
from decimal import Decimal
import playerName
import csv
import json

CALCULATED_DRAFT_ROUND_RATING = 'draftRoundRating.json'
#CALCULATED_NET_RATING_PLAYER = 'netRatingOfPlayer.json'


def calculateDraftRoundRating(season, draftRound):
 playerName.convertPlayerTableToJSON()
 players = playerName.getPlayerListFromJSON()
 sum = 0
 roundOneList = list()
 #draftNumber = list()
          
 for round in players:
  if round['season'] == season and round['draft_round'] == draftRound:
       roundOneList.append(round)

 with open(CALCULATED_DRAFT_ROUND_RATING, 'w') as jsonf:
        jsonString = json.dumps(roundOneList, indent=4)
        jsonf.write(jsonString)


 #test = roundOneList + roundTwoList + undraftedList
 #test = roundOneList
 #return draftNumber

#calculateDraftRoundRating('1998-99', '1')
 return roundOneList

def calculateAverageNetRating(playerList):
    sum = 0
    for player in playerList:
        if player['season'] != None:
            points = Decimal(player['pts']) * Decimal('0.5')
            rebounds = Decimal(player['reb']) * Decimal('0.3')
            assists = Decimal(player['ast']) * Decimal('0.2')
            netRating = (points + rebounds + assists)
            sum += netRating
            player['net_rating'] = str(netRating)
  
    result = "{:.2f}".format(sum / len(playerList))

    with open(CALCULATED_DRAFT_ROUND_RATING, 'w') as jsonf:
        jsonString = json.dumps(playerList, indent=4)
        jsonf.write(jsonString)
    
    return result