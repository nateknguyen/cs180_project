from flask import redirect, Flask, request, render_template
import playerName
import playerInsertion
import calculateNetRating

playerName.convertPlayerTableToJSON()

players = playerName.getPlayerListFromJSON()
playerToSearch = list()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('homePage.html', playerList=players)

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

if __name__ == "__main__":
    app.run(debug=True)