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

"""def __file_exists(path, search_pattern):
    file_exist = False
    os.chdir(path)
    for file in glob.glob(search_pattern):
        file_exist = True
    return file_exist"""

"""def __schemafile_correct_versionformat():
    correct_versionformat = True
    #path = globals.domain+"/schemas/core_components"
    #os.chdir(path)
    #__schemafiles_in_path(path)
    #find schemafiles with version format = x.y.z

    #path = globals.interactions
    #os.chdir(path)
    #__schemafiles_in_path(path)
    #find schemafiles with version format = x.y.z

    return correct_versionformat"""

"""def __schemafiles_in_path(path):
    schema_files = []
    return schema_files"""

def __show_missing_files():
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
        write_output("Saknad obligatorisk fil: docs/TKB_*.docx")

"""def __inspect_AB():
    write_output("\n\n----------------------------------")
    write_output("--- Kontrollerar AB-dokumentet ---")
    write_output("----------------------------------")
    write_output("Krav: alla AB ska ha minst två alternativ och motivering till det valda alternativet. Kontrolleras manuellt")
    write_output("Krav: om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    write_output("-----------------------------------------------------------------------------------------------------------")
    globals.document_path = globals.domain_folder_name+"/docs/"
    DOCX_prepare_inspection("AB_*.doc*")
    write_output("\n--------------------------------------------------------------------------------------------------------------------")
    write_output("Krav: revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_output("Granskningsstöd: om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    write_output("--------------------------------------------------------------------------------------------------------------------")
    DOCX_inspect_revision_history()
    write_output("\n-------------------------------------------------------")
    write_output("Krav: dokumentet ska innehålla rimliga arkitekturbeslut")
    write_output("-------------------------------------------------------")
    DOCX_display_paragraph_text_and_tables("arkitekturella beslut",TITLE,NO_INITIAL_NEWLINE,NO_TEXT,NO_TABLES)"""

def __inspect_IS():
    #write_output("<br><br>")
    #write_output("<h2>Kontroll av IS-dokumentet</h2>")
    #write_output("Krav: om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    #write_output("---------------------------------------------------------------------------------------------------")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    DOCX_prepare_inspection("IS_*.doc*")
    #globals.docx_document = globals.IS
    IS_init_infomodel_classes_list()
    #write_output("\n---------------------------------------------------------------------------------------------------------------------")
    #write_output("Krav: revisionshistoriken ska vara uppdaterad för samma version som domänen")
    #write_output("Granskningsstöd: om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    #write_output("---------------------------------------------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    DOCX_inspect_revision_history()
    #write_output("<br>---------------------------------------------")
    #write_output("Krav: länkarna i referenstabellen ska fungera")
    #write_output("---------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)
    #write_output("<br>Krav: infomodellklasserna ska komma i alfabetisk ordning")
    #write_output("Krav: infomodellklassernas rubriker ska börja med stor bokstav")
    #write_output("--------------------------------------------------------------")
    #write_output("Kontroll att infomodellklassernas rubriker är i alfabetisk ordning och börjar med stor bokstav")
    write_detail_box_content("<br><b>Krav:</b> infomodellklasserna ska komma i alfabetisk ordning")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas rubriker ska börja med stor bokstav")
    write_detail_box_content("Kontroll att infomodellklassernas rubriker är i alfabetisk ordning och börjar med stor bokstav")
    DOCX_display_paragraph_text_and_tables("klasser och attribut",TITLE,NO_INITIAL_NEWLINE,NO_TEXT,NO_TABLES)
    #write_output("För närvarande sker kontrollen manuellt, med ovanstående listning som underlag")
    write_detail_box_content("<b>Resultat:</b> för närvarande sker kontrollen manuellt, med ovanstående listning som underlag")
    IS_inspect_document_contents()
    #write_output("<br>---------------------------------------------------------------------------------")
    #write_output("Krav: infomodellklassernas rubriker ska ha beskrivning i anslutning till rubriken")
    #write_output("---------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas rubriker ska ha beskrivning i anslutning till rubriken")
    IS_inspect_class_description()
    #write_output("<br>-------------------------------------------------------------------")
    #write_output("Krav: multiplicitet ska vara ifyllt i infomodellklassernas tabeller")
    #write_output("-------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> multiplicitet ska vara ifyllt i infomodellklassernas tabeller")
    IS_inspect_attribute_multiplicity()
    #write_output("<br>---------------------------------------------------------------------")
    #write_output("Krav: infomodellklassernas attribut ska använda definierade datatyper")
    #write_output("---------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas attribut ska använda definierade datatyper")
    IS_inspect_usage_of_defined_datatypes()
    #write_output("<br>--------------------------------------------------------------------------------------")
    #write_output("Krav: infomodellklassernas attribut ska vara mappade till referensinformationsmodellen")
    #write_output("--------------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas attribut ska vara mappade till referensinformationsmodellen")
    IS_inspect_usage_of_reference_infomodel()
    #write_output("<br>----------------------------------------------------------")
    #write_output("Krav: infomodellklassernas alla celler ska innehålla värde")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> infomodellklassernas alla celler ska innehålla värde")
    IS_find_empty_table_cells()
    #write_output("<br>----------------------------------------------------------")

def __inspect_TKB():
    #write_output("<br><br><b>------------------------------------------------")
    #write_output("--- Kontrollerar TKB-dokumentet ---")
    #write_output("-----------------------------------------------</b>")
    #write_output("<br><br>")
    #write_output("<br><h2>Kontroll av TKB-dokumentet</h2>")
    #write_output("Krav: ResultCode ska inte förekomma i läsande tjänster (kollas av RIVTA:s verifieringsscript)")
    #write_output("Krav: för uppdaterande tjänster som kan returnera returkoder ska det finnas beskrivning av hur ResultCode ska hanteras")
    #write_output("Krav: om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    #write_output("Granskningsstöd: alla interaktionser ska vara beskrivna i TKB")
    #write_output("----------------------------------------------------------------------------------------------------------------------")
    write_detail_box_content("<b>Krav:</b> ResultCode ska inte förekomma i läsande tjänster (kollas av RIVTA:s verifieringsscript)")
    write_detail_box_content("<b>Krav:</b> för uppdaterande tjänster som kan returnera returkoder ska det finnas beskrivning av hur ResultCode ska hanteras")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> om dokumentegenskaper finns ska version och ändringsdatum stämma överens med granskad version")
    write_detail_box_content("<b>Granskningsstöd:</b> alla interaktionser ska vara beskrivna i TKB")
    DOCX_prepare_inspection("TKB_*.doc*")
    #globals.docx_document = globals.TKB
    #write_output("<br>--------------------------------------------------------------------------------------------------------------------")
    #write_output("Krav: revisionshistoriken ska vara uppdaterad för samma version som domänen")
    #write_output("Granskningsstöd: om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    #write_output("--------------------------------------------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> revisionshistoriken ska vara uppdaterad för samma version som domänen")
    write_detail_box_content("<b>Granskningsstöd:</b> om revisionshistoriken inte är uppdaterad, kontakta beställaren eller skriv en granskningskommentar")
    DOCX_inspect_revision_history()
    #write_output("<br>---------------------------------------------")
    #write_output("Krav: länkarna i referenstabellen ska fungera")
    #write_output("---------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> länkarna i referenstabellen ska fungera")
    DOCX_inspect_reference_links(TABLE_NUM_REF)
    #write_output("<br>---------------------------------------------------------------------------------------")
    #write_output("Krav: versionsnumret ska vara uppdaterat för samma version som domänen")
    #write_output("Krav: ändringsstatus för tjänstekontrakt ska överensstämma med granskningsbeställningen")
    #write_output("---------------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> versionsnumret ska vara uppdaterat för samma version som domänen")
    write_detail_box_content("<b>Krav:</b> ändringsstatus för tjänstekontrakt ska överensstämma med granskningsbeställningen")
    DOCX_display_paragraph_text_and_tables("versionsinformation",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    #write_output("<br>------------------------------------------------")
    #write_output("Krav: adressering ska vara beskriven och korrekt")
    #write_output("------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> adressering ska vara beskriven och korrekt")
    DOCX_display_paragraph_text_and_tables("adressering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    #write_output("<br>-----------------------------------------------------------------------------------------------------------------------")
    #write_output("Krav: endast domäner som behöver använda aggregering kan använda systemadressering. Beskrivningen ska vara korrekt")
    #write_output("Krav: om EI används ska det vara beskrivet och de domänspecifika EI-elementen ska vara definierade i TKB")
    #write_output("Krav: för domäner som INTE använder patientbunden aggregering ska algoritmen (hur aggregering ska göras) vara beskriven")
    #write_output("-----------------------------------------------------------------------------------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> endast domäner som behöver använda aggregering kan använda systemadressering. Beskrivningen ska vara korrekt")
    write_detail_box_content("<b>Krav:</b> om EI används ska det vara beskrivet och de domänspecifika EI-elementen ska vara definierade i TKB")
    write_detail_box_content("<b>Krav:</b> för domäner som INTE använder patientbunden aggregering ska algoritmen (hur aggregering ska göras) vara beskriven")
    DOCX_display_paragraph_text_and_tables("aggregering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)
    #write_output("<br>---------------------------------")
    #write_output("Krav: SLA-krav ska vara beskrivna")
    #write_output("---------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> SLA-krav ska vara beskrivna")
    DOCX_display_paragraph_text_and_tables("sla krav",TITLE,NO_INITIAL_NEWLINE,TEXT,TABLES)
    #<write_output("<br>---------------------------------------------")
    #write_output("Krav: felhantering ska vara korrekt beskriven")
    #write_output("---------------------------------------------")
    write_detail_box_html("<br>")
    write_detail_box_content("<b>Krav:</b> felhantering ska vara korrekt beskriven")
    DOCX_display_paragraph_text_and_tables("felhantering",TITLE,NO_INITIAL_NEWLINE,TEXT,NO_TABLES)

    """write_output("\n----------------------------------------------------------------------------------")
    write_output("Krav: alla interaktioner ska vara beskrivna i TKB")
    #write_output("Krav: alla interaktioner ska vara beskrivna i TKB med rätt versionsnr")
    write_output("Granskningsstöd: kolla att kapitelnummren hör till tjänstekontraktsavsnittet i TKB")
    write_output("----------------------------------------------------------------------------------")
    globals.interactions = globals.localGitRepo + "/" + globals.domain + "/schemas/interactions"
    globals.interaction_folders = [ f.path for f in os.scandir(globals.interactions) if f.is_dir() ]
    for interaction in sorted(globals.interaction_folders):
        interaction_name = os.path.split(interaction)[1].replace("Interaction","")
        schema_interaction_version = __get_schema_interaction_version(interaction, interaction_name)
        TK_in_TKB, result_description = TKB_display_paragragh_title(interaction_name)
        if TK_in_TKB == True:
            TKB_interaction_version = TKB_get_interaction_version(interaction_name)
            write_output(result_description + "\t(schema: " + schema_interaction_version + ")")
            #write_output("\tSchema: " + schema_interaction_version + " TKB: " + TKB_interaction_version)
            if TKB_interaction_version != schema_interaction_version:
                write_output("\t" + interaction_name + ":  Fel version angiven i TKB! Version '" + TKB_interaction_version + "' istället för '" + schema_interaction_version + "' i schemafilerna")
        else:
            write_output(result_description + "\t(schema: " + schema_interaction_version + ")")"""


"""def __get_schema_interaction_version(path,interaction_name):
    version_number = "0"
    os.chdir(path)
    subdir_name = os.path.split(os.getcwd())[1]
    for wsdl_file in glob.glob("*.wsdl"):
        version_number = wsdl_file.replace(subdir_name+"_","").replace("_RIVTABP21.wsdl","")

    return version_number"""

"""def __inspect_readme_file():
    if check_if_file_exists(globals.domain_folder_name, "readme.md") == True:
        write_output("\n\n-----------------")
        write_output("--- README.md ---")
        write_output("-----------------")
        write_output("Krav: länk till Release Notes ska gälla granskad domänversion")
        write_output("-------------------------------------------------------------")
        readme_file = open(globals.domain_folder_name+"/README.md", "r")
        readme_lines = readme_file.readlines()
        readme_file.close()
        import re
        for line in readme_lines:
            readme_line = format(line.strip())
            write_output(readme_line)
            if "http" in readme_line:
                url_in_line = re.search("(?P<url>https?://[^\s]+)", readme_line).group("url")
                status_code = verify_url_exists(url_in_line)
                if status_code < 404:
                    write_output("\tOK. Statuskod: " + str(status_code))
                else:
                    write_output("\tSidan saknas! Statuskod: " + str(status_code))"""

##########################
##### Public methods #####
##########################
"""def INFO_show_commit_info():
    write_output("\n\n---------------------------")
    write_output("--- Commit-info för tag ---")
    write_output("---------------------------")
    write_output("Krav: commit-id och sökväg till den på Bitbucket ska finnas för angiven tag")
    write_output("Granskningsstöd: commit-id och URL läggs in i granskningsrapporten")
    write_output("---------------------------------------------------------------------------")
    ###GIT_show_commit_info()
    write_output("Commit URL: https://bitbucket.org/rivta-domains/"+globals.domain+"/commits/tag/"+globals.tag)"""

"""def INFO_show_commit_diff():
    write_output("\n\n-------------------")
    write_output("--- Commit-diff ---")
    write_output("-------------------")
    write_output("Krav: förändringar ska enbart ha skett i de delar av domänen som granskningsbeställningen har angivit.")
    write_output("------------------------------------------------------------------------------------------------------")
    write_output("Diff mellan "+globals.prev_tag+" och "+globals.tag+":")
    ###GIT_show_commit_diff()"""

"""def INFO_show_subfolders():
    write_output("\n\n------------------------------------")
    write_output("--- Obligatoriska underkataloger ---")
    write_output("------------------------------------")
    write_output("Krav: domänen måste innehålla underkatalogerna: 'code_gen, docs, schemas, test-suite'")
    write_output("Granskningsstöd: om någon av katalogerna saknas så ska konfigurationsstyrning underkännas. Obs att även RIVTA-verifieringen kontrollerar detta")
    write_output("----------------------------------------------------------------------------------------------------------------------------------------------")
    globals.domain_folder_name = globals.localGitRepo + "/" + globals.domain
    os.chdir(globals.domain_folder_name)
    domain_folders = [ f.path for f in os.scandir(globals.domain_folder_name) if f.is_dir() ]
    for folder in domain_folders:
        subdir_name = os.path.split(folder)[1]
        if subdir_name != ".git":
            write_output("  Underkatalog: " + subdir_name)"""

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
