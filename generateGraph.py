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

    result = mpld3.fig_to_html(graph, figid="AGE_VS_PERFORMANCE")

    return result