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
    #2do: add inspection code
    return False

