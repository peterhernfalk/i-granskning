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
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)
    # 2do: kontrollera att det finns innehåll i referensmodelltabellens versionskolumn
        # Avsnittsrubrik: "Referensmodellsförteckning (RIM)", Kolumnrubrik: "Version"
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla ett avsnitt för begreppsmodell")
    DOCX_display_paragraph_text_and_tables("Begreppsmodell och beskrivning", TITLE, NO_INITIAL_NEWLINE, NO_TEXT, NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")
    # 2do: kontrollera att begreppsavsnittet innehåller tabellen "Beskrivning av begrepp"
    # 2do: kontrollera att det finns en begreppslista i slutet av dokumentet
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infospecen ska innehålla en begreppslista")
    DOCX_display_paragraph_text_and_tables("Begreppssystem, klassifikationer och kodverk", TITLE, NO_INITIAL_NEWLINE, TEXT, NO_TABLES)
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående avsnittsinnehåll som underlag")
    # 2do: kontrollera att begrepp i begreppbeskrivningstabellen finns definierade i dokumentets begreppslista
    # 2do: kontrollera att begreppbeskrivningstabellens alla celler har innehåll
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
    # 2do: jämför klasstabellernas datakolumn med dokumentets kodverkstabell
    # 2do: visa innehåll i dokumentets kodverkstabell (manuell granskning)
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas attribut ska vara mappade till referensinformationsmodellen")
    IS_inspect_usage_of_reference_infomodel()
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas alla celler ska innehålla värde")
    IS_find_empty_table_cells()

def __inspect_TKB():
    DOCX_prepare_inspection("TKB_*.doc*")
    #write_detail_box_html("<br>")
    #write_detail_box_content("<b>Krav:</b> ResultCode ska inte förekomma i läsande tjänster (kollas av RIVTA:s verifieringsscript)")
    #write_detail_box_content("<b>Krav:</b> för uppdaterande tjänster som kan returnera returkoder ska det finnas beskrivning av hur ResultCode ska hanteras")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    write_detail_box_content("<b>Granskningsstöd:</b> alla interaktionser ska vara beskrivna i TKB")
    # 2do: kontrollera dokumentegenskaper avseende versionsnummer
    # 2do: kontrollera versionsnummer på dokumentets första sida
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    DOCX_inspect_revision_history()
    # 2do: kontrollera att revisionshistoriktabellens alla celler har innehåll
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)
    # 2do: kontrollera att referenstabellens alla celler har innehåll
    # 2do: kontrollera om domännamnet nämns i inledningsparagrafen (det ska vara på engelska)
    # 2do: visa innehåll i inledningens underparagraf (Svenskt namn), för manuell kontroll av svenskt namn och svenskt kortnamn
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> versionsnumret ska vara uppdaterat för samma version som domänen")
    write_detail_box_content("<b>Krav:</b> ändringsstatus för tjänstekontrakt ska överensstämma med granskningsbeställningen")
    DOCX_display_paragraph_text_and_tables("versionsinformation",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    """write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> adressering ska vara beskriven och korrekt")
    DOCX_display_paragraph_text_and_tables("adressering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> endast domäner som behöver använda aggregering kan använda systemadressering. Beskrivningen ska vara korrekt")
    write_detail_box_content("<b>Krav:</b> om EI används ska det vara beskrivet och de domänspecifika EI-elementen ska vara definierade i TKB")
    write_detail_box_content("<b>Krav:</b> för domäner som INTE använder patientbunden aggregering ska algoritmen (hur aggregering ska göras) vara beskriven")
    DOCX_display_paragraph_text_and_tables("aggregering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> SLA-krav ska vara beskrivna")
    DOCX_display_paragraph_text_and_tables("sla krav",TITLE,NO_INITIAL_NEWLINE,TEXT,TABLES)
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> felhantering ska vara korrekt beskriven")
    DOCX_display_paragraph_text_and_tables("felhantering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)"""
    # 2do: kontrollera att det finns en paragraf för meddelandemodell och att den har innehåll
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
