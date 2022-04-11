from flask import redirect, Flask, request
import playerName

app = Flask(__name__)

@app.route('/')
def index():
    return f'''<!DOCTYPE html>
    <html>
        <body>
            {playerName.getPlayerTable()}
        </body>
    </html>
    '''

app.run(debug=True)