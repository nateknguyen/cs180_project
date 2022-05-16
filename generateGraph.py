import mpld3
import matplotlib.pyplot as plt
from decimal import Decimal

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