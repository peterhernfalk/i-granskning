import IS_inspection
from IS_inspection import *
from TKB_inspection import *
#from utilities import write_output, write_detail_box_content, verify_url_exists, check_if_file_exists
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

local_test = False

###########################
##### Private methods #####
###########################
def __execute_command(command):
    os.system(command)

"""def __show_missing_files():
    write_output("\n\n-----------------------------------")
    write_output("--- Saknade obligatoriska filer ---")
    write_output("-----------------------------------")
    write_output("Krav: domänen måste innehålla TKB-dokumentet, annars ska de underkännas. Infospecen bör finnas, men är inte obligatorisk")
    write_output("--------------------------------------------------------------------------------------------------------------------------------")
    globals.IS_exists = check_if_file_exists(globals.domain_folder_name+"/docs/", "IS_*.docx")
    if globals.IS_exists == False:
        write_output("Saknad obligatorisk fil: docs/IS_*.docx")
    globals.TKB_exists = check_if_file_exists(globals.domain_folder_name+"/docs/", "TKB_*.docx")
    if globals.TKB_exists == False:
        write_output("Saknad obligatorisk fil: docs/TKB_*.docx")"""

def __inspect_IS():
    DOCX_prepare_inspection("IS_*.doc*")
    IS_init_infomodel_classes_list()

    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    # 2do: kontrollera dokumentegenskaper avseende versionsnummer   https://python-docx.readthedocs.io/en/latest/dev/analysis/features/coreprops.html
    """
        Exempel på Core properties:
            Title, Subject, Author
            
        Exempel på Custom properties:
            datepublished, datumpubliserad, Publisheddate
            domain_1,_2,_3
            svekortnamn
            svename, svenamn, SvensktDomänNamn
            Version, version, Version_1,_2,_3, Version_RC, version1,2,3
    """
    # 2do: kontrollera versionsnummer på dokumentets första sida: förekomst av "Version" med efterföljande versionsnummer

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    DOCX_inspect_revision_history()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistorikens alla tabellceller ska ha innehåll")
    DOCX_empty_table_cells_exists(TABLE_NUM_REVISION, True, globals.DISPLAY_TYPE_TABLE)
    globals.IS_antal_brister_tomma_revisionshistoriktabellceller = globals.IS_antal_brister_tomma_tabellceller

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> referenstabellens alla tabellceller ska ha innehåll")
    DOCX_empty_table_cells_exists(TABLE_NUM_REF, True, globals.DISPLAY_TYPE_TEXT)
    globals.IS_antal_brister_tomma_referenstabellceller = globals.IS_antal_brister_tomma_tabellceller

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> Referensmodellsförteckning ska finnas och ha innehåll")
    write_detail_box_content("<b>Krav:</b> Versionskolumnen ska finnas och ha innehåll")
    # 2do: kontrollera att det finns innehåll i referensmodelltabellens versionskolumn, Kolumnrubrik: "Version"
    globals.IS_referensinfomodell_finns = DOCX_display_paragraph_text_and_tables("Referensmodellsförteckning (RIM)", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, TABLES)
    if globals.IS_referensinfomodell_finns  == False:
        write_detail_box_content("<b>Granskningsstöd:</b> inget innehåll visas, vilket kan bero på att avsnittsrubriken saknas eller är annan än den förväntade (Referensmodellsförteckning (RIM))")
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla ett avsnitt för begreppsmodell och beskrivning av begrepp")
    globals.IS_begreppsmodell_finns = DOCX_display_paragraph_text_and_tables("Begreppsmodell och beskrivning", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> begreppsmodellens tabell med begreppsbeskrivningar ska finnas och ha innehåll")
    begreppsbeskrivning_tabell = IS_get_tableno_for_first_title_cell("begrepp")
    DOCX_empty_table_cells_exists(begreppsbeskrivning_tabell, True, globals.DISPLAY_TYPE_TABLE)
    globals.IS_antal_brister_tomma_begreppsbeskrivningstabellceller = globals.IS_antal_brister_tomma_tabellceller

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla en begreppslista")
    globals.IS_begreppslista_finns = DOCX_display_paragraph_text_and_tables("Begreppssystem, klassifikationer och kodverk", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    if globals.IS_begreppslista_finns == False:
        write_detail_box_content("<b>Granskningsstöd:</b> inget innehåll visas, vilket kan bero på att avsnittsrubriken saknas eller är annan än den förväntade (Begreppssystem, klassifikationer och kodverk)")
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående avsnittsinnehåll som underlag")

    # 2do: kontrollera att begrepp i begreppbeskrivningstabellen finns definierade i dokumentets begreppslista
    # tolkning: jämför begreppskolumnen med beskrivningskolumnen i begreppsbeskrivningstabellen
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> begrepp i begreppsbeskrivningstabellen ska finnas definierade i dokumentets begreppslista")
    if begreppsbeskrivning_tabell > 0 and globals.IS_begreppslista_finns == True:
        write_detail_box_content("<b>Resultat:</b> kontrollen är inte utvecklad än, så för närvarande kan inget resultat visas!")
    else:
        write_detail_box_content("<b>Resultat:</b> kravet är inte uppfyllt eftersom inte både begreppsbeskrivningstabellen och begreppslistan finns i dokumentet")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla ett avsnitt för Informationsmodell")
    DOCX_display_paragraph_text_and_tables("Informationsmodell och beskrivning", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")

    write_detail_box_content("<br><b>Krav:</b> infomodellklasserna ska komma i alfabetisk ordning")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas rubriker ska börja med stor bokstav")
    write_detail_box_content("Kontroll att infomodellklassernas rubriker är i alfabetisk ordning och börjar med stor bokstav")
    write_detail_box_content("Kontroll att infomodellklassernas attributnamn börjar med liten bokstav")
    # 2do: Kontrollera att infomodellklassernas attributnamn börjar med liten bokstav
    DOCX_display_paragraph_text_and_tables("klasser och attribut",TITLE,NO_INITIAL_NEWLINE,NO_TEXT,NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")
    IS_inspect_document_contents()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas rubriker ska ha beskrivning i anslutning till rubriken")
    IS_inspect_class_description()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> multiplicitet ska vara ifyllt i infomodellklassernas tabeller")
    IS_inspect_attribute_multiplicity()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas attribut ska använda definierade datatyper")
    IS_inspect_usage_of_defined_datatypes()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla en tabell med användna kodverk")
    search_phrase_kodverk = "Identifikationer och kodverk"
    globals.IS_kodverkstabell_finns = DOCX_display_paragraph_text_and_tables(search_phrase_kodverk, TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    if globals.IS_kodverkstabell_finns == False:
        search_phrase_kodverk = "Identifierare och kodverk"
        globals.IS_kodverkstabell_finns = DOCX_display_paragraph_text_and_tables(search_phrase_kodverk, TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
        if globals.IS_kodverkstabell_finns == False:
            search_phrase_kodverk = "Begreppssystem, klassifikationer och kodverk"
            globals.IS_kodverkstabell_finns = DOCX_display_paragraph_text_and_tables(search_phrase_kodverk, TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
            if globals.IS_kodverkstabell_finns == False:
                write_detail_box_content("<b>Granskningsstöd:</b> inget av avsnitten 'Identifikationer och kodverk' eller 'Begreppssystem, klassifikationer och kodverk' hittades i infospecen")
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")
    # 2do: jämför klasstabellernas med dokumentets kodverkstabell
    # Kolumner: data, kodverk/format/regler, kodverk

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> Kodverkstabellen ska ha relevant innehåll")
    if globals.IS_kodverkstabell_finns == True:
        DOCX_display_paragraph_text_and_tables(search_phrase_kodverk, TITLE, NO_INITIAL_NEWLINE, NO_TEXT, TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas attribut ska vara mappade till referensinformationsmodellen")
    IS_inspect_usage_of_reference_infomodel()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas alla celler ska innehålla värde")
    empty_cells_found = False
    antal_tomma_klasstabellceller = 0
    for table_index in range(len(IS_inspection.infomodel_table_indexes)):
        table_number = IS_inspection.infomodel_table_indexes[table_index]
        if DOCX_empty_table_cells_exists(table_number, False, globals.DISPLAY_TYPE_TEXT) == True:
            empty_cells_found = True
            antal_tomma_klasstabellceller += globals.IS_antal_brister_tomma_tabellceller
    if empty_cells_found == True:
        write_detail_box_content("<b>Resultat:</b> det finns infomodellklass(er) med en eller flera celler utan innehåll")
    else:
        write_detail_box_content("<b>Resultat:</b> alla infomodellklassers alla celler har innehåll")
    globals.IS_antal_brister_tomma_tabellceller = antal_tomma_klasstabellceller


def __inspect_TKB():
    DOCX_prepare_inspection("TKB_*.doc*")
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
    DOCX_inspect_revision_history()

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistorikens alla tabellceller ska ha innehåll")
    DOCX_empty_table_cells_exists(TABLE_NUM_REVISION, True, globals.DISPLAY_TYPE_TABLE)
    globals.TKB_antal_brister_tomma_revisionshistoriktabellceller = globals.TKB_antal_brister_tomma_tabellceller

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> referenstabellens alla tabellceller ska ha innehåll")
    DOCX_empty_table_cells_exists(TABLE_NUM_REF, True, globals.DISPLAY_TYPE_TABLE)
    globals.TKB_antal_brister_tomma_referenstabellceller = globals.TKB_antal_brister_tomma_tabellceller

    # 2do: kontrollera om domännamnet nämns i inledningsparagrafen (det ska vara på engelska)
    # 2do: visa innehåll i inledningens underparagraf (Svenskt namn), för manuell kontroll av svenskt namn och svenskt kortnamn

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> versionsnumret ska vara uppdaterat för samma version som domänen")
    write_detail_box_content("<b>Krav:</b> ändringsstatus för tjänstekontrakt ska överensstämma med granskningsbeställningen")
    DOCX_display_paragraph_text_and_tables("versionsinformation",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)

    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> TKB ska innehålla ett avsnitt för meddelandemodeller")
    DOCX_display_paragraph_text_and_tables("Tjänstedomänens meddelandemodeller", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående avsnittsinnehåll som underlag")

    # 2do (senare): kontrollera att det finns V-MIM-tabeller (en gemensam eller en per tjänstekontrakt)
    # 2do (senare): kontrollera att meddelandemodelltabellens attribut mappar mot motsvarande i xsd-schemas


##########################
##### Public methods #####
##########################
def INFO_inspect_document(doc):
    if doc == globals.IS:
        __inspect_IS()
    elif doc == globals.TKB:
        __inspect_TKB()

############################## TEST ##############################
if local_test == True:
    ### info class name list OK ###
    #globals.domain = "riv-application.supportprocess.logistics.complaintsandfeedback"
    #globals.domain = "riv.clinicalprocess.activity.request"
    globals.domain = "riv.clinicalprocess.healthcond.actoutcome"
    #globals.domain = "riv.clinicalprocess.healthcond.certificate"
    #globals.domain = "riv.clinicalprocess.logistics.cervixscreening"
    #globals.domain = "riv.crm.requeststatus"
    #globals.domain = "riv.informationsecurity.authorization.blocking"
    #globals.domain = "riv.informationsecurity.authorization.consent"
    #globals.domain = "riv.strategicresourcemanagement.persons.person"   ### ERROR parsing URL
    #globals.domain = "riv.supportprocess.serviceprovisioning.healthcareoffering"
    #globals.domain = "riv.supportprocess.logistics.carelisting"

    ### 8.6 (Organisation) is displayed instead of 8.17 (Vårdgivare)  ###
    #globals.domain = "riv.clinicalprocess.activity.actions"

    globals.document_path = "/Users/peterhernfalk/Desktop/Aktuellt/_T-granskningar/git-Repo/"+globals.domain+"/docs"
    globals.domain_folder_name = "/Users/peterhernfalk/Desktop/Aktuellt/_T-granskningar/git-Repo/"+globals.domain

    #INFO_show_missing_files_and_inspect_documents()
    #__inspect_readme_file()
    #__inspect_AB()
    __inspect_IS()
    #__inspect_TKB()
