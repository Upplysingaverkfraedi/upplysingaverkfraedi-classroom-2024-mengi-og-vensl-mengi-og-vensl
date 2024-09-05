import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def slembiseed (dd, mm, yyyy):
    # Búa til slembifræ/seed út frá dagsetningunni
    seed = int(f"{dd:02d}{mm:02d}{yyyy}")
    np.random.seed(seed)

    # Búa til 4x4 slembifylki með 0 eða 1
    fylki = np.random.randint(0, 2, size=(4,4))

    # Endurskrifa dagssetninguna á formið "dd-mm-yyyy"
    formatted_date = f"{dd:02d}-{mm:02d}-{yyyy}"

    # Prenta niðurstöður:
    print(f"Fylkið fyrir dagsetninguna {formatted_date} og seed {seed}:")
    print(fylki)
    print()

    # Skoða eiginleika venslanna
    # AFH sjalfhverft, fylki er sjálfhverft ef öll gildin á hornalínunni eru þau sömu.
    sjalfhverf = np.all(np.diag(fylki))
    # AFH Samhverft, fylki er samhverft ef það er jafngilt byltingu sinni, þ.e.a.s. breytist ekki við byltingu, A^T = A.
    samhverf = np.all(fylki == fylki.T)
    # AFH Andsamhverft, fylki er andsamhverft ef andhverfa fylkisins er jöfn byltingunni, A^T = -A.
    andsamhverft = np.all((fylki & fylki.T) == np.diag(fylki))
    # AFH Gegnvirk, mengi X er sagt gegnvirk ef a er venslað við b og b er venslað við c, þá er a venslað við c. a = b og b = c => a = c
    gegnvirk = np.all((np.dot(fylki, fylki) > 0) <= (fylki > 0))
    print(f"\nEiginleikar venslanna:")
    print(f"Sjálfhverf: {sjalfhverf}")
    print(f"Samhverf: {samhverf}")
    print(f"Andsamhverf: {andsamhverft}")
    print(f"Gegnvirk: {gegnvirk}")

    # Teikna örvanet
    G = nx.DiGraph()
    for i in range(4):
        for j in range(4):
            if fylki[i,j] == 1:
                G.add_edge(i+1, j+1)
    plt.figure(figsize=(5,5))
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, arrows=True)
    plt.title(f"Örvanet fyrir dagsetninguna {formatted_date}")
    plt.show()


slembiseed(25,2, 2004)
slembiseed(13,7,1999)
slembiseed(7,6,2003)
