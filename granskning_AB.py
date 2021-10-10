import DOCX_display_document_contents
from DOCX_display_document_contents import *
import docx
from docx.table import *
from docx.oxml.text.paragraph import CT_P
from docx.text.paragraph import *
from docx.oxml.table import *
from docx.api import Document  # noqa
import Document_mangagement
from utilities import *


TITLE = True
NO_TITLE = False
INITIAL_NEWLINE = True
NO_INITIAL_NEWLINE = False
TEXT = True
NO_TEXT = False
TABLES = True
NO_TABLES = False
TABLE_NUM_REVISION = 1   #Hard coded, assuming that the reference table is number 1 in the document
TABLE_NUM_REF = 2   #Hard coded, assuming that the reference table is number 2 in the document



def prepare_AB_inspection(domain, tag, alt_document_name):
    """
    Beräknar url till AB-dokumentet för angiven domain och tag.

    Laddar ner dokumentet till en virtuell fil som läses in i ett docx-Document.

    Anropar därefter metoden "INFO_inspect_document" som genomför granskning av dokumentet.
    """
    """
    2do: Förenkla och snygga till koden
    """
    global AB_page_link
    global AB_document_paragraphs
    AB_page_link = Document_mangagement.DOC_get_document_page_link(domain, tag, globals.AB)
    downloaded_AB_page = Document_mangagement.DOC_get_downloaded_document(AB_page_link)

    AB_document_paragraphs = ""

    AB_head_hash = Document_mangagement.DOC_get_head_hash(downloaded_AB_page)
    AB_document_link = Document_mangagement.DOC_get_document_link(domain, tag, globals.AB, AB_head_hash, alt_document_name)
    downloaded_AB_document = Document_mangagement.DOC_get_downloaded_document(AB_document_link)
    if downloaded_AB_document.status_code == 404:
        globals.AB_exists = False
    else:
        globals.docx_AB_document = Document_mangagement.DOC_get_docx_document(downloaded_AB_document)
        globals.AB_document_exists = True
        globals.AB_exists = True
        ### dev test ###
        for paragraph in globals.docx_AB_document.paragraphs:
            if paragraph.text.strip() != "":
                AB_document_paragraphs += paragraph.text + "<br>"
        ### dev test ###

        DOCX_prepare_inspection("AB_*.doc*")

def perform_AB_inspection():
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    write_detail_box_html("<br>")
    #globals.document_path = globals.domain_folder_name+"/docs/"
    #DOCX_prepare_inspection("AB_*.doc*")
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    globals.AB_antal_brister_revisionshistorik = DOCX_inspect_revision_history(globals.AB,TABLE_NUM_REVISION)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    globals.AB_antal_brister_referenslänkar = DOCX_inspect_reference_links(TABLE_NUM_REF)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> alla AB ska ha minst två alternativ och motivering till det valda alternativet. Kontrolleras manuellt")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    write_detail_box_content("<b>Krav:</b> dokumentet ska innehålla rimliga arkitekturbeslut")
    DOCX_display_paragraph_text_and_tables("arkitekturella beslut",TITLE,NO_INITIAL_NEWLINE,NO_TEXT,NO_TABLES)
