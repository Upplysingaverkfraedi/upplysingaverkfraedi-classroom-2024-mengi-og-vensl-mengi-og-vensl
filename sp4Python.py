import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def sjalfhverft(fylki):
    # Athugar hvort fylkið sé sjálfhverft
    for i in range(len(fylki)):
        if fylki[i][i] != 1:
            return False
    return True

def samhverf(fylki):
    # Athugar hvort fylkið sé samhverft
    for i in range(len(fylki)):
        for j in range(len(fylki)):
            if fylki[i][j] != fylki[j][i]:
                return False
    return True

def adsamhverft(fylki):
    # Athugar hvort fylkið sé andsamhverft
    for i in range(len(fylki)):
        for j in range(len(fylki)):
            if i != j and fylki[i][j] == 1 and fylki[j][i] == 1:
                return False
    return True

def gegnvirkt(fylki):
    # Athugar hvort fylkið sé gegnvirkt
    n = len(fylki)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if fylki[i][j] == 1 and fylki[j][k] == 1 and fylki[i][k] != 1:
                    return False
    return True


def eiginleikar(fylki):
    # Skilar öllum eiginleikum fylkis
    return sjalfhverft(fylki), samhverf(fylki), adsamhverft(fylki), gegnvirkt(fylki)

def graf(matrix):
    # Búum til tóm directed graph (örvanet)
    G = nx.DiGraph()
    
    # Mengi hnútanna er {1, 2, 3, 4}
    nodes = range(1, len(matrix) + 1)
    
    # Bætum hnútum við netið
    G.add_nodes_from(nodes)
    
    # Bætum örvum við eftir því hvort fylkið hefur vensl
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                G.add_edge(i + 1, j + 1)  # Bætum við ör frá i+1 til j+1
    
    # Teiknum netið
    pos = nx.circular_layout(G)  # Hnútarnir verða á hring fyrir betri útlit
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold', arrowsize=20)
    plt.title("Vensl örvanet")
    plt.show()

def bua_til_fylki(dagur, manudur, ar):
    seed = int(f"{dagur:02d}{manudur:02d}{ar}")
    np.random.seed(seed)
    
    # Búa til 4x4 slembifylki með 0 eða 1
    fylki = np.random.randint(0, 2, size=(4, 4))
    
    print(f"Fylkið fyrir dagsetninguna {dagur:02d}-{manudur:02d}-{ar} með seed {seed}:")
    print(fylki)
    print()
    
    #skoðar eiginleika fylkisins
    eiginleikar(fylki)
    print("Sjálfhverf:", sjalfhverft(fylki))
    print("Samhverf:", samhverf(fylki))
    print("Andsamhverf:", adsamhverft(fylki))
    print("Gegnvirk:", gegnvirkt(fylki))
    # Teiknum vensl örvanet
    graf(fylki)
    
day, month, year = input("Sláðu inn dag, mánuð og ár með bilum (engir punktar): ").split()
dagur = int(day)
man = int(month)
ar = int(year)

bua_til_fylki(dagur, man, ar)