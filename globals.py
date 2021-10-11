AB = "AB"
AB_antal_brister_referenslänkar = 0
AB_antal_brister_revisionshistorik = 0
AB_antal_brister_tomma_referenstabellceller = 0
AB_antal_brister_tomma_revisionshistoriktabellceller = 0
AB_antal_brister_tomma_tabellceller = 0
AB_detail_box_contents = ""
AB_document_exists = False
AB_exists = False

alt_document_name = ""
COMMENTS_detail_box_contents = ""
DISPLAY_TYPE_TABLE = "display_type_table"
DISPLAY_TYPE_TEXT = "display_type_text"
docx_document = ""
docx_IS_document = ""
docx_TKB_document = ""
domain_name = ""
domain_prefix = ""
granskningsresultat = ""
HTML_2_SPACES = "&nbsp;&nbsp;"
HTML_3_SPACES = "&nbsp;&nbsp;&nbsp;"

IS = "IS"
IS_begreppslista_finns = False
IS_begreppsmodell_finns = False
IS_antal_brister_attributnamn = 0
IS_antal_brister_datatyper = 0
IS_antal_brister_klassbeskrivning = 0
IS_antal_brister_multiplicitet = 0
IS_antal_brister_referensinfomodell = 0
IS_antal_brister_referenslänkar = 0
IS_antal_brister_revisionshistorik = 0
IS_antal_brister_tomma_begreppsbeskrivningstabellceller = 0
IS_antal_brister_tomma_referenstabellceller = 0
IS_antal_brister_tomma_revisionshistoriktabellceller = 0
IS_antal_brister_tomma_tabellceller = 0
IS_detail_box_contents = ""
IS_document_exists = False
IS_document_name = ""
IS_exists = False
IS_felmeddelande = ""
IS_informationsmodell_finns = False
IS_kodverkstabell_finns = False
IS_referensinfomodell_finns = False

lower_case = "lower_case"
NOT_FOUND = "Not found"
TABLE_NUM_REVISION = 1   #Hard coded, assuming that the reference table is number 1 in the document
TABLE_NUM_REF = 2   #Hard coded, assuming that the reference table is number 2 in the document

tag = ""

TKB = "TKB"
TKB_antal_brister_referenslänkar = 0
TKB_antal_brister_revisionshistorik = 0
TKB_antal_brister_tomma_referenstabellceller = 0
TKB_antal_brister_tomma_revisionshistoriktabellceller = 0
#TKB_antal_brister_tomma_tabellceller = 0
TKB_detail_box_contents = ""
TKB_document_exists = False
TKB_document_name = ""
TKB_exists = False
TKB_meddelandemodeller_finns = False
UPPER_CASE = "UPPER_CASE"

def GLOBALS_init():
    global AB_antal_brister_referenslänkar
    global AB_antal_brister_revisionshistorik
    global AB_antal_brister_tomma_referenstabellceller
    global AB_antal_brister_tomma_revisionshistoriktabellceller
    global AB_antal_brister_tomma_tabellceller
    global AB_detail_box_contents
    global AB_document_exists
    global AB_exists
    global alt_document_name
    global COMMENTS_detail_box_contents
    global docx_document
    global docx_IS_document
    global docx_TKB_document
    global domain_name
    global domain_prefix
    global granskningsresultat
    global IS_begreppslista_finns
    global IS_begreppsmodell_finns
    global IS_antal_brister_attributnamn
    global IS_antal_brister_datatyper
    global IS_antal_brister_klassbeskrivning
    global IS_antal_brister_multiplicitet
    global IS_antal_brister_referensinfomodell
    global IS_antal_brister_referenslänkar
    global IS_antal_brister_revisionshistorik
    global IS_antal_brister_tomma_begreppsbeskrivningstabellceller
    global IS_antal_brister_tomma_referenstabellceller
    global IS_antal_brister_tomma_revisionshistoriktabellceller
    global IS_antal_brister_tomma_tabellceller
    global IS_detail_box_contents
    global IS_document_exists
    global IS_document_name
    global IS_exists
    global IS_felmeddelande
    global IS_informationsmodell_finns
    global IS_kodverkstabell_finns
    global IS_referensinfomodell_finns
    global tag
    global TKB_antal_brister_referenslänkar
    global TKB_antal_brister_revisionshistorik
    global TKB_antal_brister_tomma_referenstabellceller
    global TKB_antal_brister_tomma_revisionshistoriktabellceller
    #global TKB_antal_brister_tomma_tabellceller
    global TKB_detail_box_contents
    global TKB_document_exists
    global TKB_document_name
    global TKB_exists
    global TKB_meddelandemodeller_finns

    AB_antal_brister_referenslänkar = 0
    AB_antal_brister_revisionshistorik = 0
    AB_antal_brister_tomma_referenstabellceller = 0
    AB_antal_brister_tomma_revisionshistoriktabellceller = 0
    AB_antal_brister_tomma_tabellceller = 0
    AB_detail_box_contents = ""
    AB_document_exists = False
    AB_exists = False
    alt_document_name = ""
    COMMENTS_detail_box_contents = ""
    docx_document = ""
    docx_IS_document = ""
    docx_TKB_document = ""
    domain_name = ""
    domain_prefix = ""
    granskningsresultat = ""
    IS_begreppslista_finns = False
    IS_begreppsmodell_finns = False
    IS_antal_brister_attributnamn = 0
    IS_antal_brister_datatyper = 0
    IS_antal_brister_klassbeskrivning = 0
    IS_antal_brister_multiplicitet = 0
    IS_antal_brister_referensinfomodell = 0
    IS_antal_brister_referenslänkar = 0
    IS_antal_brister_revisionshistorik = 0
    IS_antal_brister_tomma_begreppsbeskrivningstabellceller = 0
    IS_antal_brister_tomma_referenstabellceller = 0
    IS_antal_brister_tomma_revisionshistoriktabellceller = 0
    IS_antal_brister_tomma_tabellceller = 0
    IS_detail_box_contents = ""
    IS_document_exists = False
    IS_document_name = ""
    IS_exists = False
    IS_informationsmodell_finns = False
    IS_kodverkstabell_finns = False
    IS_referensinfomodell_finns = False
    IS_felmeddelande = ""
    tag = ""
    TKB_antal_brister_referenslänkar = 0
    TKB_antal_brister_revisionshistorik = 0
    TKB_antal_brister_tomma_referenstabellceller = 0
    TKB_antal_brister_tomma_revisionshistoriktabellceller = 0
    #TKB_antal_brister_tomma_tabellceller = 0
    TKB_detail_box_contents = ""
    TKB_document_exists = False
    TKB_document_name = ""
    TKB_exists = False
    TKB_meddelandemodeller_finns = False


