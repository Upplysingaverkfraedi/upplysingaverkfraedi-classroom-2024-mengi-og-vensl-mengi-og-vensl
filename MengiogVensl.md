
# Mengi og Vensl

## **Mengjafræði**
##### a. Sýnið að sniðmengi A $\cap$ = A \ (A \ B)

Fyrst í þessu skal útskýra hvað (A $\cap$ B) þýðir. 
(A $\cap$ B) merkir það sem bæði er í A og B = (A $\cap$ B).

Það seinna til að útskýra er að (A \ B) samanstendur af öllum þáttum sem eru í A en ekki í B. Það þýðir að A \ (A \ B) er það sem er bæði í A og B því fyrst er tekið B út (A \ B) og svo er tekið A úr (A \ B) sem endar sem (A $\cap$ B).

t.d
Ef A = {1,2,3,4,5} og B = {5,6,7,8,9}
Þá er fyrst reiknað (A \ B) sem verður = {1,2,3,4}.
Svo er A \ "(A \ B)" sem er það sem er í A en ekki í (A \ B), sem er
= {5}.

##### b. Sýnið að sammengi A $\cup$ B = (A \ B) $\cup$ B

Fyrst samstendur (A $\cup$ B) af öllum hlutum sem eru í A og B, líka á milli A og B.

Það seinna til að útskýra er að (A \ B) samanstendur af öllum þáttum sem eru í A en ekki í B. Það þýðir að þegar (A \ B) sameinast við B í (A \ B) $\cup$ B, þá er það orðið einangrað A og allt B set saman og verður það sama og A $\cup$ B.

t.d

Ef A = {1,2,3,4} og B = {5,6,7,8,9}
Þá er fyrst reiknað (A \ B) sem verður = {1,2,3,4}.
Svo er bætt því við $\cup$ B, út út úr við sameinast mengin og loka svarið 
er = {1,2,3,4,5,6,7,8,9} sem er það sama og (A $\cup$ B).

## **Spurning 2: Veldismengi**

Látum P(A) vera veldismengið af menginu $A$. Sýnið hvort að $P(A) \subseteq P(P(A))$ sé alltaf það sama. Rökstyðjið af hverju eða af hverju ekki. (20 stig)
Skýrið ítarlega með röksemdum hvort mengið $P(A)$ sé eða sé ekki hlutmengi af $P(P(A))$. Notið dæmi til að styðja röksemdir ykkar.


## **LAUSN**

Til að álykta hvort $P(A) \subseteq P(P(A))$ sé alltaf rétt þurfum skulum við byrja að á að skoða skilgreiningar.

##### **SKILGREINING**
Byrjum á að skilgreina $P(A)$. Við vitum að veldismengi $A$ er táknað $P(A)$. Það lýsir mengi af öllum undirmengjum $A$. $\newline$ Höfum þá formlega uppsetningu á því $P(A) = \{ \, B \mid B \subseteq A \, \}$ skv. netbók.

Skilgreinum þá næst $P(P(A))$ sem merkir þá mengið af öllum undirmengjum $P(A)$. $\newline$ Höfum þá formlega uppsetningu á því $P(P(A)) = \{ C \mid C \subseteq P(P(A)) \}$ skv. netbók. Það þýðir að $P(P(A))$ inniheldur allar mögulegar samsetningar af undirmengjum $P(A)$.


Látum $A = \{1\}$. Þá er:

$P(A) = \{\emptyset, \{1\}\}$

$P(P(A)) = \{\emptyset, \{\emptyset\}, \{\{1\}\}, \{\emptyset, \{1\}\}\}$

Til að svara spurningunni hvort mengið $P(A)$ sé eða sé ekki hlutmengi af $P(P(A))$:

Til þess að $P(A) \subseteq P(P(A))$ sé satt, þyrftu öll stök í $P(A)$ að vera hlutmengi í $P(P(A))$. Hins vegar eru stök í $P(A)$ hlutmengi af $A$, en ekki sjálfkrafa hlutmengi af $P(A)$. Þess vegna eru stök í $P(A)$ ekki sjálfkrafa í $P(P(A))$.

Skoðum dæmi þar sem $A = \{1\}$. Þá er:

$P(A) = \{\emptyset, \{1\}\}.$

Frumengi allra hlutmengja af $P(A)$, sem táknað er $P(P(A))$, verður safn allra hlutmengja af $P(A)$:

$P(P(A)) = \{\emptyset, \{\emptyset\}, \{\{1\}\}, P(A)\}.$

Athugum að $P(P(A))$ inniheldur $\{\{1\}\}$, þar sem það er hlutmengi af $P(A)$, en það inniheldur **ekki** $\{1\}$, þar sem $\{1\} \notin P(P(A))$. Þetta þýðir að $\{1\}$ er ekki hlutmengi í $P(P(A))$.

### Niðurstaða:
$P(A) \subseteq P(P(A))$ er **ekki satt**. Hvert hlutmengi af $A$ er stak í $P(A)$, en í $P(P(A))$ verða þessi hlutmengi sjálf að stökum í safni. Af þessari ástæðu er $P(A) \subseteq P(P(A))$ ósatt.

## 3. Vensl 

**Sýnið og skýrið eftirfarandi:**

a. **Dæmi um vensl á mengi sem eru bæði samhverf og andsamhverf.** 

b. **Munur á milli falla og vensla.**

Skýrið ítarlega hvað gerir vensl samhverf og andsamhverf og nefnið dæmi. Skýrið einnig muninn á
falli og vensli og gefið gott sýnidæmi um muninn.

## Lausn 

#### a. **Dæmi um vensl á mengi sem eru bæði samhverf og andsamhverf.**

Skilgreinum samhverf og andsamhverf vensl

**Samhverf vensl**:
Vensl $R$ á mengi $A$ er sögð samhverf ef fyrir öll $x, y \in A$ gildir:
- Ef $xRy$, þá $yRx$

**Andsamhverf vensl**:
Vensl $R$ á mengi $A$ eru sögð andsamhverf ef öll $x,y \in A$ gildir:
- Ef $xRy$ og $yRx$, þá er $x = y$

**Dæmi um vensl sem eru bæði samhver og andsamhverf**

Hugsum okkur megið $A = \{1\}$ og venslin $R$ skilgreind á þvi megni þannig að $R = \{(1,1)\}$

- **Samhverf**: Fyrir öll $x,y \in A$ þar sem $xRy$, þá $yRx$. í Þessu tilfelli höfum við aðeins eina pörun, $(1,1)$. Ef $1R1$, þá $1R1$, sem uppfyllir skilyrði samhverfu.
- **Andsamhverfa**: Ef $xRy$ og $yRx$ gildir, þá er $x = y$. Í þessu tilfelli er aðeisn ein pörun $(1,1)$, og hér er $x = y = 1$ sem uppfyllir skilyrði andsamhverfu.

Þetta dæmi sýnir að venslin $R = \{(1,1)\}$ eru bæði samhverf og andsamhverf.

#### b. **Munur á milli falla og vensla.**

- **Fall**: Fall $f$ frá mengi $A$ í mengi $B$ er sérstök tegund vensla þar sem hvert stak í $A$ hefur nákvæmnlega eitt svarandi stak í $B$. Með öðrum orðum, fyrir hvert $x \in A$ er til eitt og aðeins eitt $y \in B$ þannig að $f(x) = y$ 
- **Vensl**: Vensl á milli tveggja mengja $A$ og $B$ er einhverskona safn af pörum $(x,y)$ þar sem $x \in A$ og $y \in B$. Þetta safn af pörum þarf ekki að uppfylla nein skilyrði varðandi fjölda eða einstök venls milli staka.
  
**Dæmi til að skýra muninn:**

- **Fall:** Hugsum okkur fallið $f : \mathbb{R} \rightarrow \mathbb{R}$ skilgreint með $f(x) = x^2$. Hér er hverju $x$ úr mengi $\mathbb{R}$ svarað með nákvæmnlega einu staki $y = x^2$ í $\mathbb{R}$
- ***Vensl:* Hugsum okkur að venlin $R$ á milli $\mathbb{R}$ þar sem $xRy$ ef $x \le y$. Hér getur eitt stak $x$ í $\mathbb{R}$ haft mögulega svarendur $y$ í $\mathbb{R}$.

**Munurinn:** Munurinn á falli og venslu felst í því að fall tryggir að hvert stak í menginu $A$ hefur aðeins eitt svarandi stak í $B$, en vensl getur verið miklu almennara, þar sem eitt stak $A$ getur haft engin, eitt eða fleir svarandi stök í $B$

## 4. Vensl á heiltölum 

**Búið til vensl á mengi heiltalnanna $A = \{1, 2, 3, 4\}$ með fylki í `Python` eða `R` samkvæmt
eftirfarandi leiðbeiningum:**

1. Notið afmælisdagana ykkar til að setja slembifræ (e. random seed).
2. Búið til $4 \times 4$ fylki með slembibreyttum gildum sem eru 0 eða 1.
3. Forritið virkni sem skoðar eiginleika venslanna: athugið hvort þau
   séu sjálfhverf, samhverf, andsamhverf, og gegnvirk.
4. Sannreynið niðurstöður forritsins með því að skoða venslin myndrænt með örvaneti.

Athugið, þið þurfið að uppfæra `README` skjalið til að útskýra hvernig eigi að keyra kóðann ykkar
(og hvaða pakka þarf að setja upp, ef við á). Þar sem þið eruð að endurtaka þetta fyrir allar
afmælisdaga hópmeðlima þá er ráðlagt að setja upp fall sem tekur inn dagsetninguna og skilar
niðurstöðum.

### Python Kóði

```python
# Búa til slembifræ/seed út frá dagsetningunni
seed = int(f"{dd:02d}{mm:02d}{yyyy}")
np.random.seed(seed)

# Búa til 4x4 slembifylki með 0 eða 1
fylki = np.random.randint(0, 2, size=(4, 4))

# Endirskrifa dagssetninguna á formið "dd-mm-yyyy"
formatted_date = f"{dd:02d}-{mm:02d}-{yyyy}"

# Prenta niðurstöður:
print(f"Fylkið fyrir dagsetninguna {formatted_date} og seed {seed}:")
print(fylki)
print()
```

## **Lausn**
Byrjum á því að búa til fall sem að skoðar eiginleika venslanna: athugið hvort það séu sjálfhverf, samhverf, andsamhverf, og gegnvirk.

**Sjálfhverf:** Vensl eru samhverf er fyrir öll $i$, þá er $R(i,i) = 1$ (þ.e. allir í fylkinu hafa vensl við sjálfan sig)

**Samhverf:** Vensli eru samhverf ef fyrir öll $i,j$ þá gildir að $R(i,j) = R(j,i)$

**Andsamhverf:** Vensli eru andsamhverf ef fyrir öll $i,j$, ef $R(i,j) = 1$ og $i \neq j$ þá er $R(j,i) = 0$.

**Gegnvirk:** Vensl eru gegnvirk ef $R(i,j) = 1$ og $R(j,k) = 1$ þýðir að (R(i,k) = 1)

```python
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
```
Næst búum við til fall sem að tekur saman niðurstöður með því að skoða venslin myndrænt með örvaneti.

```Python
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
```

Búum til fall sem að tekur inn afmælisdag sem slembifræ til þess að búa 4x4 fylki með slembi gildum sem eru 0 eða 1. látum það síðan kalla á hin föllin fyrir ofan til þess að athuga eiginleika þess og teiknar upp niðurstöður.
```python
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
```

Kóðinn er í skjali sem heitir "sp4Python.py". Forritið tekur inn afmælisdag í inntak og skilar fylkinu, eiginleikum þess og örvaneti.

```python
day, month, year = input("Sláðu inn dag, mánuð og ár með bilum (engir punktar): ").split()
dagur = int(day)
man = int(month)
ar = int(year)

bua_til_fylki(dagur, man, ar)
```