# I-granskning av tjänstedomäner

## Beskrivning:
Granskningsprocedur som läser in Infospec och TKB från Bitbucket-repo.
Dokumenten läses in i varsin instans av typen DOCX Document-klass. 
Granskningsflödet exekveras i sekvens per dokument. 

All kod är skriven i Python, som använder några bibliotek.
Koden är skriven i form av funktioner som anropas i ett flöde per dokument. 
Koden bör förenklas och renodlas innan slutleverans. 
I samband med det kan antagligen någon eller några Pythonfiler arbetas bort.
Det har påbörjats ett arbete att göra funktionerna mer självständiga
ur ett informationsförsörjningsperspektiv, utan beroende till globala variabler

Vid refaktorering skulle det kunna skapas en klass per dokument, 
innehållande de metoder som idag finns som funktioner i Python-filer.

### Runtime-stöd:
Filerna requirements.txt och runtime.txt används av Heroku vid deploy 
för att installera eller uppdatera Python-version och beroenden.

### Python-filer som används:
```
- app.py
  - Exponerar REST-endpoint: ('/granskningsinfo')
  - Läser in GET-parametrar från URL-strängen
  - Infospec
    - Anropar funktioner i DOC_document för att beräkna URL till Infospec i Bitbucket-repo
    - Sätter globals.docx_document till globals.IS
    - Anropar INFO_inspect_document i INFO_document_inspection
  - TKB
    - Anropar funktioner i DOC_document för att beräkna URL till TKB i Bitbucket-repo
    - Sätter globals.docx_document till globals.TKB
    - Anropar INFO_inspect_document i INFO_document_inspection
 
 - DOC_document.py
    - Funktioner för att beräkna URL till angivet dokument
 
- INFO_document_inspection.py
  - Då globals.IS valts: INFO_inspect_document anropar __inspect_IS
    - DOCX_prepare_inspection("IS_*.doc*")
    - IS_init_infomodel_classes_list()
    - Exekverar granskningskontroller
  - Då globals.TKB valts: INFO_inspect_document anropar __inspect_TKB
    - DOCX_prepare_inspection("TKB_*.doc*")
    - Exekverar granskningskontroller
    
- DOCX_display_document_contents.py
    - Funktioner som används vid granskning av docx-dokument
    
- IS_inspection.py
    - Funktioner som är specifika för granskning av Infospec
    
- TKB_inspection.py
    - Funktioner som är specifika för granskning av TKB

- globals.py
    - Globala variabler och konstanter samt en funktion för att initiera dem

- html_dashboard.py
    - Funktioner för att bygga den html som lämnas ut som svar på GET-anropet
    
- repo.py
    - Innehåller funktionen REPO_get_domain_docs_link
    
- uilities.py
    - Några funktioner som används både vid granskning av Infospec och TKB
```