import pandas

def getPlayerTable():
    players = pandas.read_csv("all_seasons.csv", sep=",")

    datas = players[ ["player_name", "team_abbreviation", "age"] ]
    datas.dropna(how="any")
    html = datas.to_html()

    return html


