**Liður 1**

Látum $A$ og $B$ vera hlutmengi alsherjarmengisins $U$. Notið skilgreiningar á mengjahugtökum og þekktar umritunarreglur til að sýna að:

**a. Sýnið að sniðmengi $A ∩ B$ má skrifa sem:
$A ∩ B = A \ (A \ B)$**

**b. Sýnið að sammengi $(A ∪ B)$ má skrifa með hjálp mismunamengja: 
$A ∪ B = (A \ B) ∪ B$**

Sýnið útreikningana og notið skilgreiningar á sammengi(∪), sniðmengi(∩), og mismengi(\), og stærðfræðilega rökfærslu.

**Lausn:**

**a. Sýnið að sniðmengi $A ∩ B$ má skrifa sem:
$A ∩ B = A \ (A \ B)$**

Sniðmengið $A ∩ B$ er skilgreint sem mengi allra staka sem eru bæði í $A$ og í $B$.

Skilgreinum $A∖B$ sem mengi allra staka sem eru í $A$ en ekki í $B$. Þá er $A∖(A∖B)$ mengi allra staka sem eru í $A$ en ekki í $A∖B$.

Nú, til að sanna að $A ∩ B = A\(A\B)$, verðum við að sýna að hvort stak í $A ∩ B$ er líka í $A\(A\B)$ og öfugt. 

1. Sýnum að $A ∩ B ⊆ A\(A\B)$

Tökum $x ∈ A ∩ B$. Þá er $x ∈ A$ og $x ∈ B$.

Ef $x ∈ B$, þá er $x ∉ A\B$ því $A\B$ inniheldur aðeins þau stök í $A$ sem eru ekki í $B$.

Þar sem $x ∈ A$ og $x ∉ A \ B$, höfum við $x ∈ A\(A\B)$.

Þannig að $x ∈ A\(A\B)$.

2. Sýnum $A\(A\B) ⊆ A ∪ B$.

Tökum $x ∈ A\(A\B)$. Þá er $x ∈ A$ og $x ∉ A\B$.

Ef $x ∉ A\B$, þá er $x ∈ B$ því $x$ getur ekki verið í $A$ án þess að vera í $B$.

Þar sem $x ∈ A$ og $x ∈ B$, höfum við $x ∈ A ∩ B$.

Þannig, $x ∈ A ∩ B$.

Niðurstaðan úr báðum sönnunum er að:

$A ∩ B = A\(A\B)$.

**b. Sýnið að sammengi $A ∪ B$ mæa skrifa með hjálp mismunamengja:
$A ∪ B = (A \ B) ∪ B$.**

Sammengi A ∪ B er mengi allra staka sem eru annaðhvort í $A,B$, eða í báðum.

1. Sýnum að $A ∪ B ⊆ (A\B) ∪ B$:

Tökum $x ∈ A ∪ B$. Þá er $x ∈ A$ eða $x ∈ B$.

Ef $x ∈ B$, þá er $x ∈ (A\B) ∪ B$.

Ef $x ∈ A$ en $x ∉ B$, þá er $x ∈ A\B$, svo $x ∈ (A\B) ∪ B$.

Með því sögðu er $x$ í baðum tilfellum $x ∈ (A\B) ∪ B$.

2. Sýnum að $(A\B) ∪ B ⊆ A ∪ B$:

Tökum $x ∈ (A\B) ∪ B$. Þá er $x ∈ A\B$ eða $x ∈ B$.

Ef $x ∈ A\B$, þá er $x ∈ A$ og $x ∉ B$. En þá er $x ∈ A ∪ B$.

Ef $x ∈ B$, þá er $x ∈ A ∪ B$.

Í báðum tilfellum er $x ∈ A ∪ B$.

Niðurstaðan úr 1. og 2. gefur okkur að:  

$A ∪ B = (A\B) ∪ B$.







