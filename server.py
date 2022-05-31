from flask import redirect, Flask, request, render_template
from matplotlib.pyplot import scatter
import playerDataStore
import playerSearch
import playerInsertion
import playerDelete
import playerUpdate
import calculateNetRating
import calculateDraftRound
import generateGraph

playerDataStore.initializePlayerTableToJSON()
players = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', playerList=players)

@app.route('/searchByName/')
def searchByName():
    players = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    name = request.args.get("name")
    playerToSearch = playerSearch.searchPlayerByName(players, name)
    searchType = 'Search by Name: '+ name

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

@app.route('/searchByDraftRound/')
def searchByDraftYear():
    players = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    draftRound = request.args.get("draftRound")
    playerToSearch = playerSearch.searchPlayerByDraftRound(players, draftRound)
    searchType = 'Search by Draft Round: '+draftRound

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

@app.route('/searchBySeason/')
def searchBySeason():
    players = playerDataStore.readDataFromJSON(playerDataStore.PLAYERS_JSON_DATA)
    season = request.args.get("season")
    playerToSearch = playerSearch.searchPlayerBySeason(players, season)
    searchType = 'Search by Season: '+season

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

#app route for add player
@app.route('/addPlayer/')
def addPlayer():
    playerData = dict.fromkeys(['', 'player_name', 'age', 'draft_round', 'draft_number', 'pts', 'reb', 'ast', 'season'])
    name = request.args.get("name")
    season = request.args.get("season")
    playerData['player_name'] = name
    playerData['season'] = season
    playerInsertion.insertPlayer(playerData)
    newEntry = [playerInsertion.getNewestPlayer()]
    return render_template('insertion.html', name = name, playerData = newEntry)

#app route for calculate net rating
@app.route('/netRating/')
def netRating():
    global players
    name = request.args.get("name")
    playerSearch.searchPlayerByName(players, name)
    playersCalculatedNetRating = calculateNetRating.calculateNetRatingOnePlayer('searchedPlayer.json')
    averageOfPlayer = calculateNetRating.calculateAverageNetRating()
    netRatingHeader = 'Net rating of ' + name

    return render_template('netRating.html', playerName=netRatingHeader,playerList=playersCalculatedNetRating, average=averageOfPlayer)


#app route for updating player
@app.route('/updatePlayer/')
def updatePlayer():
    global players

    #Search for Player by name+season
    pname = request.args.get("name")
    pseason = request.args.get("season")
    ageInput = request.args.get("ageinput")
    droundinput = request.args.get("droundinput")
    dnumberInput = request.args.get("dnumberInput")
    ptsinput = request.args.get("ptsinput")
    rebinput = request.args.get("rebinput")
    astinput = request.args.get("astinput")

    players = playerUpdate.updatePlayer(pname, pseason, droundinput, dnumberInput, ageInput, ptsinput, rebinput, astinput)
    result = playerSearch.searchPlayerByName(players, pname)

    searchType = "Update by Name: " +pname

    return render_template('update.html', playerList=result, playerName=searchType)

#app route for delete player
@app.route('/deletePlayer/')
def deletePlayer():
    global players

    pname = request.args.get("name")
    pseason = request.args.get("season")

    players = playerDelete.deletePlayer(pname, pseason)
    result = playerSearch.searchPlayerByName(players, pname)

    return render_template('delete.html', playerList=result, name=pname)

@app.route('/draftRating/')
def draftRating():
    global players
    season = request.args.get("season")
    round = request.args.get("round")
   
    playersToCalculate = calculateDraftRound.readPlayersDraftRoundRating(season, round)

    average = calculateNetRating.calculateAverageNetRating()
    draftRatingHeader = 'Season ' + season + ' Draft Round: ' + round 

    return render_template('draftRating.html', playerName=draftRatingHeader,playerList=playersToCalculate,averageNetRating=average)

@app.route('/playerGraph/')
def playerGraph():
    dataList = playerDataStore.readDataFromJSON('searchedPlayer.json')

    graph = generateGraph.generateGraph(dataList)
    max = calculateNetRating.getMaxNetRating(dataList)
    min = calculateNetRating.getMinNetRating(dataList)

    title = 'Graph of ' + dataList[0]['player_name']
    return render_template('playerGraph.html', title=title, barGraph=graph, maxNetRating=max, minNetRating=min)


@app.route('/draftGraph/')
def draftGraph():
    dataList = playerDataStore.readDataFromJSON('draftRoundRating.json')

    graph = generateGraph.generateScatter(dataList)
    max = calculateNetRating.getMaxNetRating(dataList)
    min = calculateNetRating.getMinNetRating(dataList)

    title = 'Graph of the Player Table' 
    return render_template('graphForDraft.html', title=title, scatter=graph, maxNetRating=max, minNetRating=min)

if __name__ == "__main__":
    app.run(debug=True)