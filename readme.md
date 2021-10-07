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
  - Ej skapat än
    - Anropar funktion i granskning_AB.py för att förbereda granskning av infospec
    - Anropar funktion i granskning_AB.py för att genomföra granskning av Infospec
  - Anropar funktion i granskning_IS.py för att förbereda granskning av infospec
  - Anropar funktion i granskning_IS.py för att genomföra granskning av Infospec
  - Anropar funktion i granskning_TKB.py för att förbereda granskning av TKB
  - Anropar funktion i granskning_TKB.py för att genomföra granskning av TKB
 
 - Document_management.py
    - Funktioner för att beräkna URL till angivet dokument
    
- DOCX_display_document_contents.py
    - Funktioner som används vid granskning av docx-dokument

- globals.py
    - Globala variabler och konstanter samt en funktion för att initiera dem

- granskning_AB.py (ej skapad än)
    - Funktioner som förbereder granskning av AB-dokumentet
    - Funktioner som genomför granskning av AB-dokumentet
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen
        
- granskning_IS.py
    - Funktioner som förbereder granskning av Infospec
    - Funktioner som genomför granskning av Infospec
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen

- granskning_TKB.py
    - Funktioner som förbereder granskning av TKB
    - Funktioner som genomför granskning av TKB
      - För varje granskningspunkt
        - Presenterar granskningskrav och ev. granskningsstöd
        - Anropar funktion som genomför granskning (eller listning av granskningsstöd)
          - Beroende på granskningspunkt så är det olika funktioner som anropas 
        - Presenterar resultat av granskningen

- html_dashboard.py
  - Funktioner för att bygga den dashboard i html-format som lämnas ut som svar på GET-anropet
  - 2do: lägg till inparametrar till vissa funktioner 

- repo.py
    - Innehåller funktionen REPO_get_domain_docs_link
    
- uilities.py
    - Några funktioner som används både vid granskning av Infospec och TKB

```


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
- Använd funktionen DOCX_display_paragraph_text_and_tables