[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eaw_5ILO)
# Mengi og vensl

## Leiðbeiningar

- **Öll svör verða að vera rökstudd með skýrri röksemdafærslu.** Ekki verður veitt stig fyrir svör
  án rökstuðnings.
- **Tryggið skýrleika og skipulag í uppsetningu.** Þið megið nota verkfæri eins og iPad fyrir
  útreikninga þar sem það á við. Hlaðið svo upp PDF útgáfu af lausninni ykkar.
- Þetta er hópverkefni, sem fer fram hér. **Notið PR til að fara yfir lausnir hvers annars.**
  Mikilvægt er að allir séu virkir þátttakendur.
- **Óskýr uppsetning hefur áhrif á stigagjöf verkefnisins.**
- Gangi ykkur vel!

Verkefnið byggir á virku samstarfi í gegnum GitHub þar sem notkun á branches, commitum, og pull
requestum er mikilvæg. Branches ættu að vera vel skipulagðar með skýrum og rökréttum nöfnum sem
endurspegla þemu eða virkni sem unnið er að. Commit skilaboð skulu vera skýr og lýsa þeim
breytingum sem gerðar eru, þar sem samhengi á milli breyttra skráa er augljóst. Mikilvægt er að
README skjalið sé uppfært reglulega og innihaldi skýrar leiðbeiningar um uppsetningu, notkun, og
breytingar á verkefninu.

Samvinna í teyminu er lykilatriði þar sem allir liðsmenn taka virkan þátt í þróun verkefnisins. Það
skal tryggja jafna dreifingu á commitum, branches, og pull requestum meðal liðsmanna. Ákvarðanir
skulu teknar í sameiningu, með virku samráði í gegnum code reviews og viðbrögð við breytingum. Það
er mikilvægt að hver og einn liðsmanna leggi sitt af mörkum í samræmi við sína styrkleika og að
þátttaka sé jöfn og vel skipulögð. Þetta stuðlar að sterkri teymisvinnu þar sem allir taka ábyrgð á
árangri verkefnisins.

Heildarstigagjöf fyrir GitHub notkun og samvinnu/virkni byggir á því hversu vel verkefnið uppfyllir
þessi skilyrði, með 5 stig fyrir GitHub notkun og 5 stig fyrir samvinnu og virkni í teyminu.

## 1. Mengjafræði (20 stig)

við gerðum lausn á lið 1 þar sem ég nýti mér umritunarreglur í mengjafræði til að leiða út tvær sannanir.
Lausnin er útfærð í markdown skjali (.md) með md.stærðfræðitáknum.

## 2. Veldismengi (20 stig)

Fylgdu þessum skrefum til að setja upp og keyra kóðann á réttan hátt.

1. **Búa til nýtt Virtual Environment**:
   - Opnaðu forritunarumhverfið
   - Keyrðu eftirfarandi skipun til að búa til nýtt virtual environment:
     ```bash
     python -m venv venv
     ```
   - Þetta býr til nýtt environment í möppu sem kallast `venv`.

2. **Virkið Virtual Environment**:
   - Til að virkja environmentið, keyrðu eftirfarandi skipun:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - Þegar environmentið er virkt ættir þú að sjá nafnið `venv` fyrir framan skipanalínuna í terminalnum.

## Skref 2: Setja upp nauðsynlega pakka
- Þó að engir sérstakir pakkar séu nauðsynlegir fyrir þennan kóða, þá skaltu alltaf ganga úr skugga um að allar dependency séu uppfærðar með:
  ```bash
  pip install --upgrade pip
  ```

## Skref 3: Keyra kóðann
1. **Veldu rétt Interpreter**:
   - Opnaðu Command Palette með `Ctrl+Shift+P` (eða `Cmd+Shift+P` á macOS).
   - Sláðu inn `Python: Select Interpreter` og veldu environmentið sem heitir `venv`.

2. **Keyra kóðann**:
   - Keyrðu skrána með því að nota:
     ```bash
     python power_set_solution.py
     ```
   - Úttakið mun birtast í terminalnum neðst í VS Code.

## 3. Vensl (25 stig)

Við útfærðum svar við lið 3 í mengi og vensl verkefninu með markdown file.


## 4. Vensl á heiltölum (25 stig)

# Venslamatris Framleiðandi

Þetta Python forrit býr til venslamatris fyrir tiltekna dagsetningu og athugar eiginleika þess (sjálfhverft, 
samhverft, andsamhverft, og gegnvirkt). Það sýnir einnig venslin myndrænt með `matplotlib`.

## Forkröfur

Gakktu úr skugga um að þú hafir eftirfarandi uppsett:

- Python 3.x
- `numpy`
- `matplotlib`

## Leiðbeiningar til að keyra kóðann í nýju Python umhverfi

### 1. Setja upp Python umhverfi

Þú getur sett upp nýtt Python umhverfi með verkfærum eins og `virtualenv` eða `conda`. Hér eru skrefin fyrir bæði:

#### Notkun `virtualenv` (mælt með):

1. Settu upp `virtualenv` ef þú hefur ekki gert það áður:
   ```bash

   pip install virtualenv
	2	Búðu til nýtt sýndarumhverfi: bash
	3	 virtualenv venv
	4	  
	5	Virkjaðu umhverfið:
	◦	Á macOS/Linux: bash  source venv/bin/activate
	◦	  
	◦	Á Windows: bash
	◦	 .\venv\Scripts\activate
	◦	  
Notkun conda:
	1	Búðu til nýtt umhverfi: bash  conda create --name relation-matrix-env python=3.x
	2	  
	3	Virkjaðu umhverfið: bash  conda activate relation-matrix-env
	4	  


2. Setja upp nauðsynlegar pakkar
Þegar umhverfið er virkjað, settu upp nauðsynlegar pakkar (numpy og matplotlib):
bash

pip install numpy matplotlib

3. Keyra forritið
Vistaðu forritið í skrá, til dæmis relation_matrix.py.
Keyrðu síðan forritið:
bash
python relation_matrix.py
Forritið mun biðja þig um að slá inn dagsetningu (dag, mánuð og ár) og byggt á þeirri dagsetningu mun það búa til venslamatris, greina eiginleika þess og sýna venslin myndrænt.
Dæmi um notkun
Þegar þú ert beðinn, sláðu inn dagsetningu, mánuð og ár fæðingar, og forritið mun skila:
	•	Fylki fyrir uppgefna dagsetningu.
	•	Greiningu á eiginleikum fylkisins:
	◦	Sjálfhverft
	◦	Samhverft
	◦	Andsamhverft
	◦	Gegnvirkt
	•	Myndræna framsetningu á venslinu.

Dæmi um úttak
bash
Sláðu inn dagsetningu fæðingardags (1-31): 15
Sláðu inn mánuð fæðingardags (1-12): 8
Sláðu inn ár fæðingardags (t.d., 1990): 1990

Fylkið fyrir dagsetninguna 15-08-1990 og seed 15081990:
[[1 0 1 0]
 [1 1 0 0]
 [1 0 1 0]
 [0 0 0 1]]

Sjálfhverft (Reflexive): True
Samhverft (Symmetric): False
Andsamhverft (Antisymmetric): False
Gegnvirkt (Transitive): True
Myndræna framsetningin mun birtast í glugga með matplotlib.


