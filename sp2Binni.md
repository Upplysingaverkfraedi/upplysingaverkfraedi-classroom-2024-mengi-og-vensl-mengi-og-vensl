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