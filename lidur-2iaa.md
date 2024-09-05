### 2. Veldismengi (20 stig)

Látum P(A) vera veldismengið af menginu (A). Sýnið hvort að
$$ P(A) \subseteq P(P(A)) $$
sé alltaf það sama. Rökstyðjið af hverju eða af hverju ekki. (20 stig)

Skýrið ítarlega með röksemdum hvort mengið
$$ P(A) $$
sé eða sé ekki hlutmengi af
$$ P(P(A)) $$
Notið dæmi til að styðja röksemdir ykkar.

### Lausn:

Samkvæmt skilgreiningu á hlutmengjum þurfa öll stök í A að vera stök í B til þess að A geti verið talið hlutmengi af B:

$$
A \subseteq B \Leftrightarrow x \in A \rightarrow x \in B
$$

Sýnum fram á að $$ P(A) \subseteq P(P(A)) $$  getur reynst bæði satt og ósatt með tveimur dæmum:

## Dæmi 1:
Látum $$ A = \{a\} $$
Þá er $$ P(A) = \{ \emptyset, \{a\}\} $$
Þá er $$ P(P(A)) = \{\emptyset, \{\emptyset\}, \{\{a\}\}, \{\emptyset, \{a\}\}\} $$
En nú sjáum við að {a} er ekki stak í P(P(A)), en mengið {{a}} sem inniheldur {a} og tóma mengið eru  t.d. hlutmengi af P(P(A)). Í þessu tilfelli gildir því:
$$ P(A) \not\subseteq P(P(A)) $$

## Dæmi 2:
Látum nú $$ A = \emptyset $$
Þá er $$ P(A) = \{\emptyset, \{\emptyset\}\} $$
Og $$ P(P(A)) = \{\emptyset, \{\emptyset\}, \{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\} $$

Við sjáum að í þessu tilfelli eru öll stök P(A) líka í P(P(A)):
$$
\emptyset \in P(P(A)) \quad \text{og} \quad \{\emptyset\} \in P(P(A))
$$
Því gildir í þessu tilfelli:
$$ P(A) \subseteq P(P(A)) $$

## Ályktun

Við sáum að dæmi 1 og dæmi 2 gáfu mismunandi sannleiksgildi fyrir staðhæfinguna $$ P(A) \subseteq P(P(A)) $$
Því getum við ályktað að hún sé ekki alltaf sönn né ósönn. Í tilfellinu þar sem A er tóma mengið er hún sönn, en annars ekki.