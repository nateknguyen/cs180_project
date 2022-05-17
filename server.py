from flask import redirect, Flask, request, render_template
from matplotlib.pyplot import scatter
import playerName
import playerInsertion
import calculateNetRating
import playerUpdate
import playerDelete
import json
import calculateDraftRound
import generateGraph

playerName.convertPlayerTableToJSON()

players = playerName.getPlayerListFromJSON()
playerToSearch = list()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', playerList=players)

@app.route('/searchByName/')
def searchByName():
    global playerToSearch
    name = request.args.get("name")
    playerToSearch = playerName.searchPlayerByName(players, name)
    searchType = 'Search by Name: '+name

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

@app.route('/searchByDraftYear/')
def searchByDraftYear():
    global playerToSearch
    draftYear = request.args.get("draftYear")
    playerToSearch = playerName.searchPlayerByDraftYear(players, draftYear)
    searchType = 'Search by Draft Year: '+draftYear

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

@app.route('/searchBySeason/')
def searchBySeason():
    global playerToSearch
    season = request.args.get("season")
    playerToSearch = playerName.searchPlayerBySeason(players, season)
    searchType = 'Search by Season: '+season

    return render_template('search.html', playerList=playerToSearch, playerName=searchType)

#app route for add player
@app.route('/addPlayer/')
def addPlayer():
    playerData = dict.fromkeys(['', 'player_name', 'team_abbreviation', 'age', 'player_height', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season'])
    name = request.args.get("name")
    playerData['player_name'] = name
    playerInsertion.insertPlayer(playerData)
    newEntry = [playerInsertion.getNewestPlayer()]
    return render_template('insertion.html', name = name, playerData = newEntry)

#app route for calculate net rating
@app.route('/netRating/')
def netRating():
    name = request.args.get("name")
    playersCalculatedNetRating = calculateNetRating.calculateNetRating(name)
    netRatingHeader = 'Net rating of ' + name

    return render_template('netRating.html', playerName=netRatingHeader,playerList=playersCalculatedNetRating)


#app route for updating player
@app.route('/updatePlayer/')
def updatePlayer():
    global playerToSearch



    #Search for Player by name+season
    pname = request.args.get("name")
    pseason = request.args.get("season")
    playerToSearch = playerName.searchPlayerByName(players, pname)
    playerToSearch = playerName.searchPlayerBySeason(playerToSearch, pseason)


    #if person exists within list, get rest of inputs and write new ones
    if (len(playerToSearch) != 0):
        obj = json.load(open("players.json"))

        tainput = request.args.get("tainput")
        ageinput = request.args.get("ageinput")
        heightinput = request.args.get("heightinput")
        weightinput = request.args.get("weightinput")
        collegeinput = request.args.get("collegeinput")
        countryinput = request.args.get("countryinput")
        dyearinput = request.args.get("dyearinput")
        droundinput = request.args.get("droundinput")
        dnuminput = request.args.get("dnuminput")
        GPinput = request.args.get("GPinput")
        ptsinput = request.args.get("ptsinput")
        rebinput = request.args.get("rebinput")
        astinput = request.args.get("astinput")
        ORPinput = request.args.get("ORPinput")
        UPinput = request.args.get("UPinput")
        TSPinput = request.args.get("TSPinput")
        APinput = request.args.get("APinput")
        DRPinput = request.args.get("DRPinput")
        

        #rewriting
        for i in range(len(obj)):
            if obj[i]["player_name"] == pname and obj[i]["season"] == pseason:
                obj[i]["age"] = ageinput
                obj[i]["ast"] = astinput
                obj[i]["ast_pct"] = APinput
                obj[i]["college"] = collegeinput
                obj[i]["country"] = countryinput
                obj[i]["draft_number"] = dnuminput
                obj[i]["draft_round"] = droundinput
                obj[i]["draft_year"] = dyearinput
                obj[i]["dreb_pct"] = DRPinput
                obj[i]["gp"] = GPinput
                obj[i]["oreb_pct"] = ORPinput
                obj[i]["player_height"] = heightinput
                obj[i]["player_weight"] = weightinput
                obj[i]["pts"] = ptsinput
                obj[i]["reb"] = rebinput
                obj[i]["team_abbreviation"] = tainput
                obj[i]["ts_pct"] = TSPinput
                obj[i]["usg_pct"] = UPinput
                obj[i]["oreb_pct"] = ORPinput

                open("players.json", "w").write(
            json.dumps(obj, sort_keys=True, indent = 4, separators=(',',': '))
        )


    playerToSearch = playerName.searchPlayerByName(players, pname)
    playerToSearch = playerName.searchPlayerBySeason(playerToSearch, pseason)

    searchType = "Update by Name: " +pname

    return render_template('update.html', playerList=playerToSearch, playerName=searchType)

#app route for delete player
@app.route('/deletePlayer/')
def deletePlayer():
    global playerToSearch

    pname = request.args.get("name")
    pseason = request.args.get("season")
    

    playerToSearch = playerName.searchPlayerByName(players, pname)
    playerToSearch = playerName.searchPlayerBySeason(playerToSearch, pseason)


    if (len(playerToSearch) != 0):
        obj = json.load(open("players.json"))
        
        for i in range(len(obj)):
            if obj[i]["player_name"] == pname and obj[i]["season"] == pseason:
                obj.pop(i)
                break

        open("players.json", "w").write(
            json.dumps(obj, sort_keys=True, indent = 4, separators=(',',': '))
        )

    return render_template('delete.html')

@app.route('/draftRating/')
def draftRating():
    season = request.args.get("season")
    round = request.args.get("round")
    draftRoundRating = calculateDraftRound.calculateDraftRoundRating(season,round)
    average = calculateDraftRound.calculateAverageNetRating(draftRoundRating)
    draftRatingHeader = 'Season ' + season + ' Draft Round: ' + round 

    return render_template('draftRating.html', playerName=draftRatingHeader,playerList=draftRoundRating,averageNetRating=average)

@app.route('/playerGraph/')
def playerGraph():
    with open('netRatingOfPlayer.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    dataList = list(data)

    graph = generateGraph.generateGraph(dataList)
    max = calculateNetRating.getMaxNetRating(dataList)
    min = calculateNetRating.getMinNetRating(dataList)

    title = 'Graph of ' + dataList[0]['player_name']
    return render_template('playerGraph.html', title=title, barGraph=graph, maxNetRating=max, minNetRating=min)


@app.route('/draftGraph/')
def draftGraph():
    with open('draftRoundRating.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    dataList = list(data)

    graph = generateGraph.generateScatter(dataList)
    max = calculateNetRating.getMaxNetRating(dataList)
    min = calculateNetRating.getMinNetRating(dataList)

    title = 'Graph of ' + dataList[0]['season'] + ' season and draft round ' + dataList[0]['draft_round']
    return render_template('graphForDraft.html', title=title, scatter=graph, maxNetRating=max, minNetRating=min)

if __name__ == "__main__":
    app.run(debug=True)