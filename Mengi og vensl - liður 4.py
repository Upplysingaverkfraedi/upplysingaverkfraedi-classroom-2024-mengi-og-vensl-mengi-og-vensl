import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def athuga_vensli_og_teikna(dd, mm, yyyy):
    # Búa til slembifræ/seed út frá dagsetningunni
    seed = int(f"{dd:02}{mm:02}{yyyy}")
    np.random.seed(seed)

    # Búa til 4x4 slembifylki með 0 eða 1
    fylki = np.random.randint(0, 2, size=(4, 4))

    # Endirskrifa dagssetninguna á formið "dd-mm-yyyy"
    formatted_date = f"{dd:02}-{mm:02}-{yyyy}"

    # Prenta niðurstöður:
    print(f"Fylkið fyrir dagsetninguna {formatted_date} og seed {seed}:")
    print(fylki)
    print()

    # Athugar hvort fylkið sé sjálfhverft
    def er_sjalfhverft(fylki):
        return all(fylki[i][i] == 1 for i in range(len(fylki)))

    # Athugar hvort fylkið sé samhverft
    def er_samhverft(fylki):
        return np.array_equal(fylki, fylki.T)

    # Athugar hvort fylkið sé andsamhverft
    def er_andsamhverft(fylki):
        return all(fylki[i][j] != fylki[j][i] or fylki[i][j] == 0 for i in range(len(fylki)) for j in range(len(fylki)) if i != j)

    # Athugar hvort fylkið sé gegnvirkt
    def er_gegnvirkt(fylki):
        return all(fylki[i][k] == 1 for i in range(len(fylki)) for j in range(len(fylki)) for k in range(len(fylki)) if fylki[i][j] == 1 and fylki[j][k] == 1)

    # Skoða eiginleika venslanna
    print(f"Fylkið fyrir dagsetninguna {dd:02d}-{mm:02d}-{yyyy}:")
    print(fylki)
    print("\nEiginleikar venslanna:")
    print(f"Sjálfhverf: {er_sjalfhverft(fylki)}")
    print(f"Samhverf: {er_samhverft(fylki)}")
    print(f"Andsamhverf: {er_andsamhverft(fylki)}")
    print(f"Gegnvirk: {er_gegnvirkt(fylki)}")
    print("=" * 40)

    # Myndræn framsetning á venslunum með örvaneti
    G = nx.DiGraph()

    for i in range(4):
        for j in range(4):
            if fylki[i][j] == 1:
                G.add_edge(i+1, j+1)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', arrows=True)
    plt.title(f"Örvanet fyrir dagsetninguna {dd:02d}-{mm:02d}-{yyyy}")
    plt.show()

# Dagsetningar sem verða skoðaðar
dagsetningar = [
    (15, 10, 2002),  # 15. október 2002
    (27, 5, 2001),   # 27. maí 2001
    (14, 7, 2003)    # 14. júlí 2001
]

# Keyra fyrir hverja dagsetningu og teikna örvanet
for dd, mm, yyyy in dagsetningar:
    athuga_vensli_og_teikna(dd, mm, yyyy)



# Sjálfhverf: Sérhvert stak er venslað sjálfu sér (a ~ a) "(a, a) ∈ R for every element a ∈ A."
# Samhverf:  Fyrir öll stök a og b í S gildir (a ~ b <=> b ~ a)
# Andsamhverf: Má aðeins ganga í eina átt (ekki báðar áttir)
# Gegnvirk: Fyrir öll a, b og c í X að ef a er venslað við b er venslað við c, þá er a og c tengt. (a=b og b=c --> a=c)

#Dagsetningar: 
   # (15, 10, 2002),  # Dagsetning 1 Alda 
    # (14, 7, 2003),  # Dagsetning 2 Benni 
    # (27, 5, 2001)     # Dagsetning 3 Elísabet

    
