import pandas

def getPlayerTable():
    players = pandas.read_csv("all_seasons.csv", sep=",")

    dataSet = list()
    for data in players.iloc:
        dataSet.append(data.to_dict())

    return dataSet
