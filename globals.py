AB = "AB"

alt_document_name = ""
COMMENTS_detail_box_contents = ""
DISPLAY_TYPE_TABLE = "display_type_table"
DISPLAY_TYPE_TEXT = "display_type_text"
docx_document = ""
docx_AB_document = ""
docx_IS_document = ""
docx_TKB_document = ""
domain_name = ""
domain_prefix = ""
granskningsresultat = ""
HTML_2_SPACES = "&nbsp;&nbsp;"
HTML_3_SPACES = "&nbsp;&nbsp;&nbsp;"

TITLE = True
NO_TITLE = False
INITIAL_NEWLINE = True
NO_INITIAL_NEWLINE = False
TEXT = True
NO_TEXT = False
TABLES = True
NO_TABLES = False

IS = "IS"

lower_case = "lower_case"
NOT_FOUND = "Not found"
TABLE_NUM_REVISION = 1   #Hard coded, assuming that the reference table is number 1 in the document
TABLE_NUM_REF = 2   #Hard coded, assuming that the reference table is number 2 in the document

tag = ""

TKB = "TKB"
UPPER_CASE = "UPPER_CASE"

def GLOBALS_init():
    global alt_document_name
    global COMMENTS_detail_box_contents
    global docx_document
    global docx_AB_document
    global docx_IS_document
    global docx_TKB_document
    global domain_name
    global domain_prefix
    global granskningsresultat
    global tag
    alt_document_name = ""
    COMMENTS_detail_box_contents = ""
    docx_document = ""
    docx_IS_document = ""
    docx_TKB_document = ""
    domain_name = ""
    domain_prefix = ""
    granskningsresultat = ""
    tag = ""

