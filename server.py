from flask import redirect, Flask, request, render_template
import playerName
import playerInsertion
import calculateNetRating
import playerUpdate
import playerDelete
import json

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

    name = request.args.get("name")
    season = request.args.get("season")
    pinput = request.args.get("pinput")
    TAinput = request.args.get("TAinput")

    playerToSearch = playerName.searchPlayerByName(players, name)
    print("playerToSearch:" , playerToSearch)
    playerToSearch = playerName.searchPlayerBySeason(playerToSearch, season)

    print("player_name: ", name)
    print("season: " , season)

    print("pinput: ", pinput)
    print("TAinput: " , TAinput)

    searchType = 'Update by Name: ' +name


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

if __name__ == "__main__":
    app.run(debug=True)