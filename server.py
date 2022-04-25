from operator import methodcaller
import string
from flask import redirect, Flask, request, render_template
import playerName
import playerInsertion
import playerUpdate

players = playerName.getPlayerTable()
playerToSearch = list()
check = list()

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
    playerData = [0] * 21 #create a player entry of 20 elements for each column
    name = request.args.get("name")
    playerData[0] = name 
    player = playerInsertion.insertPlayer(playerData)
    newEntry = [playerInsertion.getNewestPlayer()]
    return render_template('insertion.html', name = name, playerData = newEntry)

#app route for update player
@app.route('/updatePlayer/')
def updatePlayer():
    global playerToSearch
    
    name = request.args.get("name")
    season = request.args.get("season")

    playerToSearch = playerName.searchPlayerByName(players, name)
    print("playerToSearch:" , playerToSearch)
    playerToSearch = playerName.searchPlayerBySeason(playerToSearch, season)
    
    print("name: ", name)
    print("season: " , season)

    searchType = 'Update by Name: '+name

    return render_template('update.html', playerList=playerToSearch, playerName=searchType)

if __name__ == "__main__":
    app.run(debug=True)

