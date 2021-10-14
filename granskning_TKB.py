"""import Document_mangagement
#from TKB_inspection import *
#from utilities import write_output, write_detail_box_content, verify_url_exists, check_if_file_exists
from utilities import *"""
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


def prepare_TKB_inspection(domain, tag, alt_document_name):
    """
    Beräknar url till TKB-dokumentet för angiven domain och tag.

    Laddar ner dokumentet till en virtuell fil som läses in i ett docx-Document.

    Anropar därefter metoden "INFO_inspect_document" som genomför granskning av dokumentet.
    """
    """
    2do: Förenkla och snygga till koden
    """
    global TKB_page_link
    global TKB_document_paragraphs
    #TKB_page_link = __get_document_page_link(domain, tag, globals.TKB)
    #downloaded_TKB_page = __get_downloaded_document(TKB_page_link)
    TKB_page_link = Document_mangagement.DOC_get_document_page_link(domain, tag, globals.TKB)
    downloaded_TKB_page = Document_mangagement.DOC_get_downloaded_document(TKB_page_link)

    TKB_document_paragraphs = ""

    TKB_head_hash = Document_mangagement.DOC_get_head_hash(downloaded_TKB_page)
    TKB_document_link = Document_mangagement.DOC_get_document_link(domain, tag, globals.TKB, TKB_head_hash, alt_document_name)
    downloaded_TKB_document = Document_mangagement.DOC_get_downloaded_document(TKB_document_link)
    if downloaded_TKB_document.status_code == 404:
        ###TKB_document_paragraphs = APP_text_document_not_found(globals.TKB, domain, tag)
        ###globals.granskningsresultat += "<br><br><h2>TKB</h2>" + APP_text_document_not_found(globals.TKB, domain, tag)
        docx_TKB_document = ""
        #globals.TKB_felmeddelande = APP_text_document_not_found(globals.TKB, domain, tag)
        globals.TKB_exists = False
    else:
        globals.docx_TKB_document = Document_mangagement.DOC_get_docx_document(downloaded_TKB_document)
        globals.TKB_document_exists = True
        globals.TKB_exists = True
        ### dev test ###
        for paragraph in globals.docx_TKB_document.paragraphs:
            if paragraph.text.strip() != "":
                TKB_document_paragraphs += paragraph.text + "<br>"
        ### dev test ###

        DOCX_prepare_inspection("TKB_*.doc*")

def perform_TKB_inspection(domain, tag, alt_document_name):
    prepare_TKB_inspection(domain, tag, alt_document_name)
    if globals.TKB_exists == False:
        return

    #write_detail_box_html("<br>")
    #write_detail_box_content("<b>Krav:</b> ResultCode ska inte förekomma i läsande tjänster (kollas av RIVTA:s verifieringsscript)")
    #write_detail_box_content("<b>Krav:</b> för uppdaterande tjänster som kan returnera returkoder ska det finnas beskrivning av hur ResultCode ska hanteras")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    # 2do: kontrollera dokumentegenskaper avseende versionsnummer
    # 2do: kontrollera versionsnummer på dokumentets första sida
    write_detail_box_content("<b>Granskningsstöd:</b> alla interaktioner ska vara beskrivna i TKB")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    used_table_no = DOCX_display_document_contents.DOCX_get_tableno_for_paragraph_title("revisionshistorik")
    if used_table_no > 0:
        globals.TKB_antal_brister_revisionshistorik = DOCX_inspect_revision_history(globals.TKB, used_table_no)
    else:
        globals.TKB_antal_brister_revisionshistorik = DOCX_inspect_revision_history(globals.TKB,TABLE_NUM_REVISION)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistorikens alla tabellceller ska ha innehåll")
    if used_table_no > 0:
        result, globals.TKB_antal_brister_tomma_revisionshistoriktabellceller = DOCX_empty_table_cells_exists(used_table_no, True, globals.DISPLAY_TYPE_TABLE)
    else:
        result, globals.TKB_antal_brister_tomma_revisionshistoriktabellceller = DOCX_empty_table_cells_exists(TABLE_NUM_REVISION, True, globals.DISPLAY_TYPE_TABLE)
    #globals.TKB_antal_brister_tomma_revisionshistoriktabellceller = globals.TKB_antal_brister_tomma_tabellceller

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    globals.TKB_antal_brister_referenslänkar = DOCX_inspect_reference_links(TABLE_NUM_REF)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> referenstabellens alla tabellceller ska ha innehåll")
    if used_table_no > 0:
        result, globals.TKB_antal_brister_tomma_referenstabellceller = DOCX_empty_table_cells_exists(used_table_no, True, globals.DISPLAY_TYPE_TABLE)
    else:
        result, globals.TKB_antal_brister_tomma_referenstabellceller = DOCX_empty_table_cells_exists(TABLE_NUM_REF, True, globals.DISPLAY_TYPE_TABLE)
    #globals.TKB_antal_brister_tomma_referenstabellceller = globals.TKB_antal_brister_tomma_tabellceller

    # 2do: kontrollera om domännamnet nämns i inledningsparagrafen (det ska vara på engelska)
    # 2do: visa innehåll i inledningens underparagraf (Svenskt namn), för manuell kontroll av svenskt namn och svenskt kortnamn

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> versionsnumret ska vara uppdaterat för samma version som domänen")
    write_detail_box_content("<b>Krav:</b> ändringsstatus för tjänstekontrakt ska överensstämma med granskningsbeställningen")
    DOCX_display_paragraph_text_and_tables("versionsinformation",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> TKB ska innehålla ett avsnitt för meddelandemodeller")
    globals.TKB_meddelandemodeller_finns = DOCX_display_paragraph_text_and_tables("Tjänstedomänens meddelandemodeller", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    if globals.TKB_meddelandemodeller_finns == False:
        write_detail_box_content("<b>Granskningsstöd:</b> inget innehåll visas, vilket kan bero på att avsnittsrubriken saknas eller är annan än den förväntade (Tjänstedomänens meddelandemodeller)")
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående avsnittsinnehåll som underlag")

    # 2do (senare): kontrollera att det finns V-MIM-tabeller (en gemensam eller en per tjänstekontrakt)
    # 2do (senare): kontrollera att meddelandemodelltabellens attribut mappar mot motsvarande i xsd-schemas

######################################################
##### Privata funktioner (från TKB_inspection.py #####
######################################################
def TKB_get_interaction_version(interaction_name):
    version_number = "0"
    #2do: extract version number from interaction paragraph
    searched_paragraph_level = DOCX_document_structure_get_exact_levelvalue(interaction_name)
    #__display_paragraph_text_by_paragraph_level(interaction_name,searched_paragraph_level)
    version_number = DOCX_display_paragraph_text_by_paragraph_level(searched_paragraph_level,interaction_name)

    return version_number


def TKB_display_paragragh_title(searched_title_name):
    result = True
    result_description = ""
    searched_paragraph_level = DOCX_document_structure_get_exact_levelvalue(searched_title_name)
    if searched_paragraph_level != "":
        #result_description = "OK. TKB (" + searched_paragraph_level + "):  \t" + searched_title_name
        result_description = "TKB (" + searched_paragraph_level + "):  \t" + searched_title_name
        #write_output("OK. TKB (" + searched_paragraph_level + "):  \t" + searched_title_name)
    else:
        result_description = "FEL! " + searched_title_name + " verkar inte vara beskrivet i TKB!"
        #write_output("FEL! " + searched_title_name + " verkar inte vara beskrivet i TKB!")
        result = False
    return result, result_description

def __display_paragraph_text_by_paragraph_level(searched_paragraph_level,display_keylevel_text):
    global document_paragraph_index_dict
    previous_key = ""
    for key, value in document_paragraph_index_dict.items():
        if key[0:len(searched_paragraph_level)] == searched_paragraph_level:
            key_level_length = key.find(" ")
            if len(key.strip()) > key_level_length:
                this_key_level = key.strip()[0:key_level_length]
                if this_key_level == previous_key:
                    if display_keylevel_text == True:
                        write_output("\t" + key.strip()[key_level_length+1:])
                else:
                    write_output(key)
                previous_key = key.strip()[0:key_level_length]
