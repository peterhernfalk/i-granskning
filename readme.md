# I-granskning av tjänstedomäner

## Beskrivning:
Granskningsprocedur som läser in Infospec och TKB från Bitbucket-repo.
Dokumenten läses in i varsin instans av typen DOCX Document-klass. 
Granskningsflödet exekveras i sekvens per dokument genom anrop från app.py 
Granskningsfunktioner har i första hand utvecklats för att kunna användas av alla granskade dokument. 
I de fall där kraven är specifika för ett visst dokument så har granskningsfunktioner utvecklats för just dessa krav.

All kod är skriven i Python, som använder några bibliotek.
Koden är skriven i form av funktioner som anropas i ett flöde per dokument.

Koden förenklas och renodlas inför slutleverans. 
Det har påbörjats ett arbete att göra funktionerna mer självständiga
ur ett informationsförsörjningsperspektiv, med ett minskat beroende till globala variabler

### Runtime-stöd:
Filerna requirements.txt och runtime.txt används av Heroku vid deploy 
för att installera eller uppdatera Python-version och beroenden.


## Målbild för kodstruktur:
- Renodlad, välstrukturerad kod (separation of concerns)
- Funktionell stil i form av inparametrar till funktioner med data som används av funktionerna
- Generaliserade funktioner (återanvändning) för at undvika kopiering av kod
- Struktur
  - App med endpoint och html-svar på anrop
  - Granskningsprocedur per dokument (anropas av app)
  - URL-byggande
  - Dokumenthantering och användning av dokumentinnehåll
  - Html-generering
  - Globala variabler
### Python-filer som används i förbättrad struktur:
```
- app.py
  - Exponerar REST-endpoint: ('/granskningsinfo')
  - Läser in GET-parametrar från URL-strängen
  - AB-dokumentet
    - Anropar funktion i granskning_AB.py för att förbereda granskning av infospec
    - Anropar funktion i granskning_AB.py för att genomföra granskning av Infospec
  - Infospec
    - Anropar funktion i granskning_IS.py för att förbereda granskning av infospec
    - Anropar funktion i granskning_IS.py för att genomföra granskning av Infospec
  - TKB
    - Anropar funktion i granskning_TKB.py för att förbereda granskning av TKB
    - Anropar funktion i granskning_TKB.py för att genomföra granskning av TKB
 
 - Document_management.py
    - Funktioner för att beräkna URL till angivet dokument
    
- DOCX_display_document_contents.py
    - Funktioner som används vid granskning av docx-dokument

- globals.py
    - Globala variabler och konstanter samt en funktion för att initiera dem

- granskning_AB.py
    - Funktion som förbereder granskning av AB-dokumentet
    - Funktioner som genomför granskning av AB-dokumentet
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen
        
- granskning_IS.py
    - Funktion som förbereder granskning av Infospec
    - Funktioner som genomför granskning av Infospec
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen

- granskning_TKB.py
    - Funktion som förbereder granskning av TKB
    - Funktioner som genomför granskning av TKB
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen

- html_dashboard.py
  - Funktioner för att bygga den dashboard i html-format som lämnas ut som svar på GET-anropet
  - Returnerad html innehåller:
    - All layout, inklusive css
    - Navigeringslänkar i lista till vänster om huvudinnehållet
    - Två boxar med summeringsinformation
    - Detaljboxar per granskat dokument
  - 2do: lägg till inparametrar till vissa funktioner 

- repo.py
    - Innehåller funktionen REPO_get_domain_docs_link
    
- uilities.py
    - Några funktioner som används både vid granskning av Infospec och TKB

```
### Utredning innan utveckling:
- Listningen nedan visar hur många tabeller det faktiskt finns per avsnitt per dokument (för närvarande baserat på Intygsdomänen).
  - Slutsatsen hittills är att de allra flesta avsnitt inte har mer än en tabell
- AB
  - Saknar avsnittsrubrik (avvikelser kan förekomma i vissa domäner)
    - Tabell 1: revisionshistorik inom projektet
    - Tabell 2: referenser
  - Ingår i avsnitt
    - 1.2: Begrepp
    - 2.x: Arkitekturellt beslut
- Infospec
  - Saknar avsnittsrubrik (avvikelser kan förekomma i vissa domäner)
    - Tabell 1: revisionshistorik
    - Tabell 2: referenser
  - Ingår i avsnitt
    - 2: Informationssäkerhet
      - Tabell: beskrivning av informationen
      - Tabell: lagrum
      - Tabell: informationsflöde
      - Tabell: spårbarhet, tillgänglighet och arkivering
      - Tabell: krav på den som konsumerar informationen
    - 3: Referensmodellsförteckning (RIM)
    - 4: Processmodell
      - 4.1, tabell: Beskrivning av processmodellen
    - 5: Arbetsflöde
      - 5.1.1, tabell: Aktörer
      - 5.1.2, tabell: Användningsfall
    - 6: Begreppsmodell och beskrivning
      - 6.2, tabell: Beskrivning av begrepp
    - 7: Informationsmodell och beskrivning
      - Inga tabeller
    - 8: Klasser och attribut
      - 8.x, tabell: klass
    - 9: Datatyper i informationsmdoellen
      - Tabell
    - 10: Multipliciteter i informationsmodellen
      - Tabell
    - 11: Identifierare och kodverk
      - Tabell
- TKB
  - Saknar avsnittsrubrik (avvikelser kan förekomma i vissa domäner)
    - Tabell 1: revisionshistorik
    - Tabell 2: referenser
  - Ingår i avsnitt
    - 2: Versionsinfomation
      - 2.1.3: Förändrade tjänstekontrakt
        - Tabell med kompatibilitetsinformation
    - 3: Tjänstedomänens arkitektur
      - 3.7: flöden
        - Tabell
    - 4: Tjänstedomänens krav och regler
      - 4.2.1: SLA krav
        - Tabell
    - 6: Tjänstekontrakt
      - 6.x tjänstekontrakt xyz
        - 6.x.2: Fältregler
          - Tabell med begäran och svar
    - 7: Gemensamma fälttyper (kan även heta Gemensamma datatyper)
      - Tabeller kan förekomma direkt eller i undernivåer



## Driftsättning, konfiguration, beroenden:
- Push till GitHub-repo
  - Från lokalt repo
- Deploy till Heroku-app
  - Deploy sker med Herokus CLI 
  - runtime.txt används av Heroku för att se till att önskat Python-version är installerat i appen
  - requirements.txt används av Heroku för att se till att angivna versioner av dependencies är installerade i appen

## Information riktad till utvecklare:
Dokumenten som granskas laddas ner till virtuella dokumentinstanser (DOCX Document), som är de som granskas.
### Komplettera med ytterligare granskningspukt:
Både granskningsflöde och dokumentspecifika funktioner finns i 
respektive dokuments granskningsfil (granskning_*.py). 
Funktioner som används vid granskning av flera dokument finns i gemensam pyhon-fil. 
Exempel på det är DOCX_display_document_contents.py

- Lägg till kod i granskning_*.py (granskningsfilen för berört dokument)
  - Presentation av granskningskrav
  - Anrop till funktion som genomför granskningen
    - Använd befintlig funktion eller lägg till en ny funktion i lämplig python-fil
  - Presentation av granskningens resultat
- Ifall granskningskrav som är gemensamt för flera dokument ska läggas till:
  - Skapa funktionen i lämplig gemensam python-fil
  - Lägg till anrop till funktionen i de granskningsfiler som ska använda samma granskningskontroll
- Uppdatera sammanfattningsruta i html_dashboard.py om resultat av den nya granskningspunkten ska visas i summeringsruta

### Listning av dokumentinnehåll under en viss rubrik:
- Introduktion
  - Funktionen DOCX_display_paragraph_text_and_tables används för att visa innehåll i sökt paragraf
- Lösning
  - Parametrar avgör vilket paragrafinnehåll som ska visas
  - Funktionen returnerar True eller False som anger om sökt paragraf hittades
- Användning
  - Funktionen används av ett flertal IS-, TKB- och AB-granskningspunkter

### Tabellnummer för tabell under en viss rubrik
- Introduktion
  - Instanser av Document innehåller attributet tables som håller reda på alla tabeller som finns i dokumentet
  - document.tables[tabellnummer] refererar till en viss tabell i dokumentet, men utan koppling till var i dokumentet den finns
- Lösning
  - Dictionaryt paragraph_title_tableno_dict sparar tabellnummer med rubrik som nyckel
  - Funktionen DOCX_get_tableno_for_paragraph_title används för att få det tabellnummer som hör till en viss rubrik
  - I vissa fall innehåller dokumentet flera likadana rubriker. I de fallen läggs tabellnummer till i nyckeln för att 
  skapa unika nycklar så att alla förekomster lagras i dictionaryt
- Användning
  - Dictionaryt används av implementation av vissa granskningskrav i Infospec, TKB och AB-dokumentet

### Kontroll av förekomst av tomma tabellceller
- Introduktion
  - Funktionen DOCX_empty_table_cells_exists används för att kontrollera om angiven tabell innehåller tomma celler
  - Det är ganska många kodrader, vilket gör funktionen onödigt komplex att förvalta och vidareutveckla
  - Förenkling av koden ska ske innan överlämning till förvaltning
- Lösning
- Användning