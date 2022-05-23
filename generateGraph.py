import mpld3
import matplotlib.pyplot as plt
from decimal import Decimal
import matplotlib
matplotlib.use("agg")

def generateGraph(players):
    x = list()
    y = list()
    for player in players:
        x.append(Decimal(player['age']))
        y.append(Decimal(player['net_rating']))

    graph = plt.figure()
    plt.bar(x,y)
    plt.xlabel("Age", labelpad=7, fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size':15})
    plt.ylabel("Net Rating", labelpad=15, fontdict={'family': 'serif', 'color': 'r', 'weight': 'bold', 'size':15})

    result = mpld3.fig_to_html(graph, figid="AGE_VS_PERFORMANCE")

    return result

def generateScatter(players):
    x = list()
    y = list()
    for player in players:
        x.append(Decimal(player['draft_number']))
        y.append(Decimal(player['net_rating']))

    graph = plt.figure()
    plt.scatter(x,y)
    plt.xlabel("Draft Number", labelpad=7, fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size':15})
    plt.ylabel("Net Rating", labelpad=15, fontdict={'family': 'serif', 'color': 'r', 'weight': 'bold', 'size':15})

    result = mpld3.fig_to_html(graph, figid="DRAFT_ROUND_GRAPH")

    return result


