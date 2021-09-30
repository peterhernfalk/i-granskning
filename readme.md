# I-granskning av tjänstedomäner

## Beskrivning:
Granskningsprocedur som läser in Infospec och TKB från Bitbucket-repo.
Dokumenten läses in i varsin instans av typen DOCX Document-klass. 
Granskningsflödet exekveras i sekvens per dokument. 

All kod är skriven i Python, som använder några bibliotek.
Koden är skriven i form av funktioner som anropas i ett flöde per dokument. 
Koden bör förenklas och renodlas innan slutleverans. 
Vid refaktorering skulle det kunna skapas en klass per dokument, 
innehållande de funktioner som idag finns i Python-filer.

## Python-filer som används:
```
- app.py
  - Exponerar REST-endpoint: ('/granskningsinfo')
  - Läser in GET-parametrar från URL-strängen
  - Infospec
    - Beräknar URL till Infospec i Bitbucket-repo
    - Anropar INFO_inspect_document i INFO_document_inspection
    - Sätter globals.docx_document till globals.IS
  - TKB
    - Beräknar URL till TKB i Bitbucket-repo
    - Sätter globals.docx_document till globals.TKB
    - Anropar INFO_inspect_document i INFO_document_inspection
  
- INFO_document_inspection.py
  - Då globals.IS valts: INFO_inspect_document anropar __inspect_IS
    - DOCX_prepare_inspection("IS_*.doc*")
    - IS_init_infomodel_classes_list()
    - Exekverar granskningskontroller
  - Då globals.TKB valts: INFO_inspect_document anropar __inspect_TKB
    - DOCX_prepare_inspection("TKB_*.doc*")
    - Exekverar granskningskontroller
    
- DOCX_display_document_contents.py
- IS_inspection.py
- TKB_inspection.py
- globals.py
- html_dashboard.py
- repo.py
- uilities.py
```