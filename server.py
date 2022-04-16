from flask import redirect, Flask, request, render_template
import playerName

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', playerList=playerName.getPlayerTable())

if __name__ == "__main__":
    app.run(debug=True)