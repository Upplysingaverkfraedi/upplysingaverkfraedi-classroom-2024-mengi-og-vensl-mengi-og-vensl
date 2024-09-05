import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

birthdays = [
    [9, 9, 2003],
    [27, 11, 2002],
    [30, 1, 2001],
]

def plot_relation(fylki, title):
    G = nx.DiGraph()

    # Bæta við hnúta
    G.add_nodes_from(range(fylki.shape[0]))

    # Bæta við örvum
    for i in range(fylki.shape[0]):
        for j in range(fylki.shape[1]):
            if fylki[i, j] == 1:
                G.add_edge(i, j)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
    plt.title(title)
    plt.show()

for i in range(len(birthdays)):
    # Búa til slembifræ/seed út frá dagsetningunni
    dd, mm, yyyy = birthdays[i]

    seed = int(f"{dd:02d}{mm:02d}{yyyy}")
    np.random.seed(seed)

    # Búa til 4x4 slembifylki með 0 eða 1
    fylki = np.random.randint(0, 2, size=(4, 4))

    # Endirskrifa dagssetninguna á formið "dd-mm-yyyy"
    formatted_date = f"{dd:02d}-{mm:02d}{yyyy}"

    # Prenta niðurstöður:
    print(f"Fylkið fyrir dagsetninguna {formatted_date} og seed {seed}:")
    print(fylki)
    print()

    # sjálfhverft ef stökin á aðalhornalínunni eru 1 (i=j)
    if np.all(np.diag(fylki) == 1):
        print("Fylkið er sjálfhverft")
    else:
        print("Fylkið er ekki sjálfhverft")

    # Samhverft ef fylkið er jafnt og fylkið transposed
    if np.array_equal(fylki, fylki.T):
        print("Fylkið er samhverft")
    else:
        print("Fylkið er ekki samhverft")

    # Andsamhverft ef fylkið er jafnt -fylkinu
    if np.array_equal(fylki, -fylki):
        print("Fylkið er andsamhverft")
    else:
        print("Fylkið er ekki andsamhverft")

    # Athuga gegnvirkni
    n = fylki.shape[0]  # Fjöldi raða/dálka í fylkinu
    er_gegnvirkt = True

    # Athuga gegnvirkni
    for i in range(n):
        for j in range(n):
            if fylki[i][j] == 1:
                for k in range(n):
                    if fylki[j][k] == 1 and fylki[i][k] != 1:
                        er_gegnvirkt = False
                        break
    if er_gegnvirkt:
        print("Fylkið er gegnvirkt")
    else:
        print("Fylkið er ekki gegnvirkt")

    # Teikna örvanet fyrir fylkin
    plot_relation(fylki, f"Relation Graph for {formatted_date}")