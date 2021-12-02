import granskning_AB
import granskning_IS
import granskning_TKB
from repo import *

AB_antal_brister = 0
IS_antal_brister = 0
TKB_antal_brister = 0

def get_page_html():
    """
    Funktionen anropas av app.py för att få en ifylld dashboard i html-format

    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.domain_name
    - globals.tag
    - globals.IS_detail_box_contents
    - globals.COMMENTS_detail_box_contents
    """
    global AB_antal_brister
    AB_antal_brister = 0
    global IS_antal_brister
    IS_antal_brister = 0
    global TKB_antal_brister
    TKB_antal_brister = 0

    html = __html_start() + __html_head() + __html_body_start() + __html_sidebar() + __html_overview_start(globals.domain_name, globals.tag)
    html += __html_summary_infospec() + __html_summary_TKB_box() + __html_section_end()

    html += __html_detail_section_begin("Infospec")
    html += __html_recent_inspection_box_begin("Infospec-granskning") + granskning_IS.IS_detail_box_contents + __html_recent_inspection_box_end()

    html += __html_br() + __html_detail_box_begin_TKB() + granskning_TKB.TKB_detail_box_contents + __box_content_end()

    html += __html_br() + __html_detail_box_begin_AB() + granskning_AB.AB_detail_box_contents + __box_content_end()

    globals.COMMENTS_detail_box_contents = "Här ska förslag till granskningskommentarer visas, inklusive färgkodning och i samma struktur som granskningsrapporten"
    html += __html_br() + __html_detail_box_begin_COMMENTS() + globals.COMMENTS_detail_box_contents + __box_content_end()

    html += __html_section_end()+__html_br()+__html_br()+__html_body_end()+__html_end()
    return html

def __html_start():
    html = '''
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    '''
    return html

def __html_end():
    """html = '''
    </html>
    '''
    return html"""
    return "</html>"

def __html_head():
    html = '''
    <head>
    <meta charset="UTF-8">
    <title> I-granskning </title>
    '''
    html += __html_style()
    html += '''
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    '''
    return html

def __html_style():
    html = '''
    <style>
    /* Googlefont Poppins CDN Link */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
    *{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }
    
    .sidebar{
      position: fixed;
      height: 100%;
      width: 240px;
      background: gray;  //#0A2558;
      transition: all 0.5s ease;
    }
    .sidebar.active{
      width: 60px;
    }
    .sidebar .nav-links{
      margin-top: 10px;
    }
    .sidebar .nav-links li{
      position: relative;
      list-style: none;
      height: 50px;
    }
    .sidebar .nav-links li a{
      height: 100%;
      width: 100%;
      display: flex;
      align-items: center;
      text-decoration: none;
      transition: all 0.4s ease;
    }
    .sidebar .nav-links li a.active{
      background: #505050;
    }
    .sidebar .nav-links li a:hover{
      background: #081D45;
    }
    .sidebar .nav-links li i{
      padding-left: 20px;
      text-align: center;
      font-size: 18px;
      color: #fff;
    }
    .sidebar .nav-links li a .links_name{
      color: #fff;
      font-size: 15px;
      font-weight: 400;
      white-space: nowrap;
    }
    .sidebar .nav-links .log_out{
      position: absolute;
      bottom: 0;
      width: 100%;
    }
    .sidebar .logo-details{
      height: 80px;
      display: flex;
      align-items: center;
    }
    .sidebar .logo-details i{
      font-size: 28px;
      font-weight: 500;
      color: #fff;
      min-width: 60px;
      text-align: center
    }
    .sidebar .logo-details .logo_name{
      color: #fff;
      font-size: 24px;
      font-weight: 500;
    }
    .home-section{
      position: relative;
      background: #f5f5f5;
      min-height: 30vh;  //100vh;
      width: calc(100% - 240px);
      left: 240px;
      transition: all 0.5s ease;
    }
    .home-section nav .sidebar-button{
      display: flex;
      align-items: center;
      font-size: 24px;
      font-weight: 500;
    }
    nav .sidebar-button i{
      font-size: 35px;
      margin-right: 10px;
    }
    .home-section .home-content{
      position: relative;
      padding-top: 40px;
    }
    .home-content .overview-boxes{
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      padding: 0 20px;
    }
    .overview-boxes .box{
      display: flex;
      justify-content: center;
      width: calc(100% / 2 - 55px);
      background: #fff;
      padding: 15px 14px;
      border-radius: 12px;
      box-shadow: 0 5px 10px rgba(0,0,0,0.1);
    }
    .overview-boxes .box-topic{
      font-size: 20px;
      font-weight: 500;
    }
    /* left box */
    .home-content .detail-boxes .recent-inspection{
      width: 97%;
      background: #fff;
      padding: 20px 30px;
      margin: 0 20px;
      border-radius: 12px;
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }
    .detail-boxes .box .title{
      font-size: 24px;
      font-weight: 500;
    }
    .detail-boxes .inspection-details li{
      list-style: none;
      margin: 8px 0;
    }
    
    @media (max-width: 1240px) {
      .sidebar{
        width: 60px;
      }
      .sidebar.active{
        width: 220px;
      }
      .home-section{
        width: calc(100% - 60px);
        left: 60px;
      }
      .sidebar.active ~ .home-section{
        /* width: calc(100% - 220px); */
        overflow: hidden;
        left: 220px;
      }
      .home-section nav{
        width: calc(100% - 60px);
        left: 60px;
      }
      .sidebar.active ~ .home-section nav{
        width: calc(100% - 220px);
        left: 220px;
      }
    }
    @media (max-width: 1150px) {
      .home-content .inspection-boxes{
        flex-direction: column;
      }
      .home-content .inspection-boxes .box{
        width: 100%;
        overflow-x: scroll;
        margin-bottom: 30px;
      }
      .home-content .inspection-boxes{
        margin: 0;
      }
    }
    @media (max-width: 1000px) {
      .overview-boxes .box{
        width: calc(100% / 2 - 15px);
        margin-bottom: 15px;
      }
    }
    @media (max-width: 700px) {
      nav .sidebar-button .dashboard,
      nav .profile-details .admin_name,
      nav .profile-details i{
        display: none;
      }
      .home-section nav .profile-details{
        height: 50px;
        min-width: 40px;
      }
      .home-content .inspection-boxes .inspection-details{
        width: 560px;
      }
    }
    @media (max-width: 550px) {
      .overview-boxes .box{
        width: 100%;
        margin-bottom: 15px;
      }
      .sidebar.active ~ .home-section nav .profile-details{
        display: none;
      }
    }
    </style>
    '''
    return html

def __html_br():
    """html = '''
    <br>
    '''
    return html"""
    return "<br> "

def __html_body_start():
    """html = '''
    <body>
    '''
    return html"""
    return "<body>"

def __html_body_end():
    """html = '''
    </body>
    '''
    return html"""
    return "</body>"

def __html_sidebar():
    html = '''
      <div class="sidebar">
      <ul class="nav-links">
        <li>
          <a href="#" class="active">
            <i></i>
            <span class="links_name"><b>Innehåll</b></span>
          </a>
        </li>
        <li>
          <a href="#Infospec">
            <i></i>
            <span class="links_name">Infospec-granskning</span>
          </a>
        </li>
        <li>
          <a href="#TKB">
            <i></i>
            <span class="links_name">TKB-granskning</span>
          </a>
        </li>
        <li>
          <a href="#AB">
            <i></i>
            <span class="links_name">AB-granskning</span>
          </a>
        </li>
        <li>
          <a href="#Comments">
            <i></i>
            <span class="links_name">Granskningskommentarer</span>
          </a>
        </li>
        </div>
    '''
    return html

def __html_overview_start(domain_name, tag):
    html = '''
      <section class="home-section">
    <nav>
      <div class="sidebar-button">
        <i></i>
        <span class="dashboard">I-granskning av: &nbsp; '''
    html += domain_name + ' (' + tag + ')</span>'
    html += '''
    </div>
    </nav>
    <div class="home-content">
    <div class="overview-boxes">
    '''
    return html


def __html_summary_infospec():
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.IS_exists
    - globals.IS
    - globals.domain_name
    - globals.tag
    """
    html = '''
    <ul class="recent-result box">
    <div>
    <div class="box-topic">Sammanfattning: infospec-granskning</div>
    '''
    if granskning_IS.IS_exists == True:
        html += '<div><li>' + __get_infospec_summary("revisionshistorik") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("revisionshistorik_cellinnehåll") + '</li></div>'
        html += "<br>"
        html += '<div><li>' + __get_infospec_summary("referenslänkar") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("referenslänkar_cellinnehåll") + '</li></div>'
        html += "<br>"
        html += '<div><li>' + __get_infospec_summary("referensinfomodell_finns") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("begreppsmodell_finns") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("begreppsmodellr_cellinnehåll") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("begreppslista_finns") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("informationsmodell_finns") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("kodverkstabell_finns") + '</li></div>'
        html += "<br>"
        html += '<div><li>' + __get_infospec_summary("klassbeskrivning") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("attributnamn") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("multiplicitet") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("datatyper") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("referensinfomodell") + '</li></div>'
        html += '<div><li>' + __get_infospec_summary("tabellcellinnehåll") + '</li></div>'
        html += "<br>"
        html += "<b>" + str(IS_antal_brister) + " &nbsp;brister i Infospec</b> upptäckta av automatiserad granskning<br>"
    else:
        html += __text_document_not_found(globals.IS, globals.domain_name, globals.tag)
    html += '''
    </div>
    </ul>
    '''
    return html

def __text_document_not_found(doc, domain, tag):
    """
    Sammanställer ett meddelande till användaren då sökt dokument saknas eller då fel dokumentnamn har angivits.

    Returenar: information i html-format
    """
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.IS
    - globals.TKB
    - globals.AB
    - globals.HTML_2_SPACES
    - resultatet av REPO_get_domain_docs_link(domain, tag)
    """
    document_name = "Infospec"
    if doc == globals.TKB:
        document_name = globals.TKB
    elif doc == globals.AB:
        document_name = globals.AB

    document_info = globals.HTML_2_SPACES
    document_info += "<br><b>" + document_name + " saknas</b> eller har annat namn än det förväntade: <i><br>" + globals.HTML_2_SPACES+globals.HTML_2_SPACES + doc.upper() + "_" + domain.replace(".", "_") + ".docx</i>"
    docs_link = REPO_get_domain_docs_link(domain, tag)
    document_info += "<br><br>" + globals.HTML_2_SPACES + "Kontrollera dokumentnamn här: <a href='" + docs_link + "'" + " target='_blank'>" + docs_link + "</a>"
    document_info += "<br><br>" + globals.HTML_2_SPACES + "Om det finns en " + document_name + " så har den ett annat än det förväntade namnet. "
    if doc == globals.IS:
        document_info += "<br>" + globals.HTML_2_SPACES + "I så fall kan du ange det namnet som en url-parameter enligt: <br>" + globals.HTML_2_SPACES + globals.HTML_2_SPACES + "<i>url...</i><b>&is=dokumentnamn</b>"
        document_info += "<br>" + globals.HTML_2_SPACES + "Om detta är en applikationsspecifik domän kan du ange det i en url-parameter: <br>" + globals.HTML_2_SPACES+globals.HTML_2_SPACES + "<i>url...</i><b>&domainprefix=true</b>"
    elif doc == globals.TKB:
        document_info += "<br>" + globals.HTML_2_SPACES + "I så fall kan du ange det namnet som en url-parameter enligt: <br>" + globals.HTML_2_SPACES + globals.HTML_2_SPACES + "<i>url...</i><b>&tkb=dokumentnamn</b>"
        document_info += "<br>" + globals.HTML_2_SPACES + "Om detta är en applikationsspecifik domän kan du ange det i en url-parameter: <br>" + globals.HTML_2_SPACES+globals.HTML_2_SPACES + "<i>url...</i><b>&domainprefix=true</b>"
    elif doc == globals.AB:
        document_info += "<br>" + globals.HTML_2_SPACES + "I så fall kan du ange det namnet som en url-parameter enligt: <br>" + globals.HTML_2_SPACES + globals.HTML_2_SPACES + "<i>url...</i><b>&ab=dokumentnamn</b>"
        document_info += "<br>" + globals.HTML_2_SPACES + "Om detta är en applikationsspecifik domän kan du ange det i en url-parameter: <br>" + globals.HTML_2_SPACES+globals.HTML_2_SPACES + "<i>url...</i><b>&domainprefix=true</b>"

    return document_info


def __get_infospec_summary(topic):
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.IS_antal_brister_revisionshistorik
    - globals.IS_antal_brister_tomma_revisionshistoriktabellceller
    - globals.IS_antal_brister_referenslänkar
    - globals.IS_antal_brister_tomma_referenstabellceller
    - globals.IS_referensinfomodell_finns
    - globals.IS_begreppsmodell_finns
    - globals.IS_antal_brister_tomma_begreppsbeskrivningstabellceller
    - globals.IS_begreppslista_finns
    - globals.IS_kodverkstabell_finns
    - globals.IS_antal_brister_klassbeskrivning
    - globals.IS_antal_brister_attributnamn
    - globals.IS_antal_brister_multiplicitet
    - globals.IS_antal_brister_datatyper
    - globals.IS_antal_brister_referensinfomodell
    - globals.IS_antal_brister_tomma_tabellceller
    """
    global IS_antal_brister
    html = ""
    if topic == "revisionshistorik":
        if granskning_IS.IS_antal_brister_revisionshistorik == 0:
            html += "Revisionshistoriken har <b>korrekt</b> version angiven"
        else:
            html += "<b>Fel versionsnummer</b> angivet i revisionshistoriken"
            IS_antal_brister += 1
    elif topic == "revisionshistorik_cellinnehåll":
        html += "<b>" + str(granskning_IS.IS_antal_brister_tomma_revisionshistoriktabellceller) + " &nbsp;</b>tomma celler i revisionshistoriken"
        IS_antal_brister += granskning_IS.IS_antal_brister_tomma_revisionshistoriktabellceller
    elif topic == "referenslänkar":
        html += "<b>" + str(granskning_IS.IS_antal_brister_referenslänkar) + " &nbsp;</b>felaktiga länkar i referenstabellen"
        IS_antal_brister += granskning_IS.IS_antal_brister_referenslänkar
    elif topic == "referenslänkar_cellinnehåll":
        html += "<b>" + str(granskning_IS.IS_antal_brister_tomma_referenstabellceller) + " &nbsp;</b>tomma celler i referenstabellen"
        IS_antal_brister += granskning_IS.IS_antal_brister_tomma_referenstabellceller
    elif topic == "referensinfomodell_finns":
        if granskning_IS.IS_referensinfomodell_finns == True:
            html += "Referensinformationsmodell (RIM) <b>finns</b>"
        else:
            html += "Referensinformationsmodell (RIM) <b>saknas</b>"
            IS_antal_brister += 1
    elif topic == "begreppsmodell_finns":
          if granskning_IS.IS_begreppsmodell_finns == True:
                html += "Begreppsmodell <b>finns</b>"
          else:
                html += "Begreppsmodell <b>saknas</b>"
                IS_antal_brister += 1
    elif topic == "begreppsmodellr_cellinnehåll":
        html += "<b>" + str(granskning_IS.IS_antal_brister_tomma_begreppsbeskrivningstabellceller) + " &nbsp;</b>tomma celler i begreppsbeskrivningstabellen"
        IS_antal_brister += granskning_IS.IS_antal_brister_tomma_begreppsbeskrivningstabellceller
    elif topic == "begreppslista_finns":
        if granskning_IS.IS_begreppslista_finns == True:
            html += "Begreppslista <b>finns</b>"
        else:
            html += "Begreppslista <b>saknas</b>"
            IS_antal_brister += 1
    elif topic == "informationsmodell_finns":
        if granskning_IS.IS_informationsmodell_finns == True:
            html += "Informationsmodell <b>finns</b>"
        else:
            html += "Informationsmodell <b>saknas</b>"
            IS_antal_brister += 1
    elif topic == "kodverkstabell_finns":
        if granskning_IS.IS_kodverkstabell_finns == True:
            html += "Kodverkstabell <b>finns</b>"
        else:
            html += "Kodverkstabell <b>saknas</b>"
            IS_antal_brister += 1
    elif topic == "klassbeskrivning":
        html += "<b>" + str(granskning_IS.IS_antal_brister_klassbeskrivning) + " &nbsp;</b>saknade klassbeskrivningar"
        IS_antal_brister += granskning_IS.IS_antal_brister_klassbeskrivning
    elif topic == "attributnamn":
        html += "<b>" + str(granskning_IS.IS_antal_brister_attributnamn) + " &nbsp;</b>klassattribut med fel skiftläge"
        IS_antal_brister += granskning_IS.IS_antal_brister_attributnamn
    elif topic == "multiplicitet":
        html += "<b>" + str(granskning_IS.IS_antal_brister_multiplicitet) + " &nbsp;</b>saknade multipliciteter i klasstabeller"
        IS_antal_brister += granskning_IS.IS_antal_brister_multiplicitet
    elif topic == "datatyper":
        html += "<b>" + str(granskning_IS.IS_antal_brister_datatyper) + " &nbsp;</b>odefinierade datatyper"
        IS_antal_brister += granskning_IS.IS_antal_brister_datatyper
    elif topic == "referensinfomodell":
        html += "<b>" + str(granskning_IS.IS_antal_brister_referensinfomodell) + " &nbsp;</b>saknade referenser till RIM i klasstabeller"
        IS_antal_brister += granskning_IS.IS_antal_brister_referensinfomodell
    elif topic == "tabellcellinnehåll":
        html += "<b>" + str(granskning_IS.IS_antal_brister_tomma_tabellceller) + " &nbsp;</b>tomma celler i klasstabeller"
        IS_antal_brister += granskning_IS.IS_antal_brister_tomma_tabellceller
    return html

def __html_summary_TKB_box():
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.TKB_exists
    - globals.TKB
    - globals.domain_name
    - globals.tag
    """
    html = '''
    <ul class="recent-result box">
    <div>
    <div class="box-topic">Sammanfattning: TKB-granskning</div>
    '''

    if granskning_TKB.TKB_exists == True:
        html += __get_TKB_summary()
    else:
        html += __text_document_not_found(globals.TKB, globals.domain_name, globals.tag)

    if granskning_AB.AB_exists == True:
        html += '''
            <br><hr><br><div class="box-topic">Sammanfattning: AB-granskning</div>
        '''
        html += __get_AB_summary()
    else:
        html += __text_document_not_found(globals.AB, globals.domain_name, globals.tag)

    html += '<br><hr><br><div class="box-topic">Sammanfattning: granskningskommentarer</div>'
    html += "<div><li>Detta är <b> inte implementerat</b></li></div>"

    html += '''
    </div>
    </ul>
    </div>
    '''
    return html

def __get_TKB_summary():
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.TKB_antal_brister_revisionshistorik
    - globals.TKB_antal_brister_tomma_revisionshistoriktabellceller
    - globals.TKB_antal_brister_referenslänkar
    - globals.TKB_antal_brister_tomma_referenstabellceller
    """
    global TKB_antal_brister
    html = ""
    if granskning_TKB.TKB_antal_brister_revisionshistorik == 0:
        html += "<div><li>Revisionshistoriken har <b>korrekt</b> version angiven</li></div>"
    else:
        html += "<div><li><b>Fel versionsnummer</b> angivet i revisionshistoriken</li></div>"
        TKB_antal_brister += 1
    html += "<div><li><b>" + str(granskning_TKB.TKB_antal_brister_tomma_revisionshistoriktabellceller) + " &nbsp;</b>tomma celler i revisionshistoriken</li></div>"
    TKB_antal_brister += granskning_TKB.TKB_antal_brister_tomma_revisionshistoriktabellceller
    html += "<br>"
    html += "<div><li><b>" + str(granskning_TKB.TKB_antal_brister_referenslänkar) + " &nbsp;</b>felaktiga länkar i referenstabellen</li></div>"
    TKB_antal_brister += granskning_TKB.TKB_antal_brister_referenslänkar
    html += "<div><li><b>" + str(granskning_TKB.TKB_antal_brister_tomma_referenstabellceller) + " &nbsp;</b>tomma celler i referenstabellen</li></div>"
    TKB_antal_brister += granskning_TKB.TKB_antal_brister_tomma_referenstabellceller
    html += "<br>"
    if granskning_TKB.TKB_meddelandemodeller_finns == True:
        html += "<div><li>Meddelandemodeller <b>finns</b></li></div>"
    else:
        html += "<div><li>Meddelandemodeller <b>saknas</b></li></div>"
        TKB_antal_brister += 1
    html += "<br>"
    #html += "<h4>Antal brister i TKB: " + str(TKB_antal_brister) + "</h4>"
    html += "<b>" + str(TKB_antal_brister) + " &nbsp;brister i TKB</b> upptäckta av automatiserad granskning<br>"

    return html

def __html_summary_AB():
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.AB_exists
    - globals.AB
    - globals.domain_name
    - globals.tag
    """
    html = '''
    <ul class="recent-result box">
    <div>
    <div class="box-topic">Sammanfattning: AB-granskning</div>
    '''

    if globals.AB_exists == True:
        html += __get_AB_summary()
    else:
        html += __text_document_not_found(globals.AB, globals.domain_name, globals.tag)

    html += '''
        <br><div class="box-topic">Sammanfattning: AB-granskning</div>
        <div><li><b>0  &nbsp;</b>granskade krav på AB-dokumentet</div></li>
    '''


    html += '''
    </div>
    </ul>
    </div>
    '''
    return html

def __get_AB_summary():
    """
    Tänkbar förbättring: lägg till dessa inparametrar:
    - globals.AB_antal_brister_revisionshistorik
    - globals.AB_antal_brister_tomma_revisionshistoriktabellceller
    """
    global AB_antal_brister
    html = ""
    if granskning_AB.AB_antal_brister_revisionshistorik == 0:
        html += "<div><li>Revisionshistoriken har <b>korrekt</b> version angiven</li></div>"
    else:
        html += "<div><li><b>Fel versionsnummer</b> angivet i revisionshistoriken</li></div>"
        AB_antal_brister += 1
    html += "<div><li><b>" + str(granskning_AB.AB_antal_brister_tomma_revisionshistoriktabellceller) + " &nbsp;</b>tomma celler i revisionshistoriken</li></div>"
    AB_antal_brister += granskning_AB.AB_antal_brister_tomma_revisionshistoriktabellceller

    html += "<div><li><b>" + str(granskning_AB.AB_antal_brister_referenslänkar) + " &nbsp;</b>felaktiga länkar i referenstabellen</li></div>"
    AB_antal_brister += granskning_AB.AB_antal_brister_referenslänkar

    html += "<div><li><b>" + str(granskning_AB.AB_antal_brister_tomma_referenstabellceller) + " &nbsp;</b>tomma celler i referenstabellen</li></div>"
    AB_antal_brister += granskning_AB.AB_antal_brister_tomma_referenstabellceller
    html += "<br><b>" + str(AB_antal_brister) + " &nbsp;brister i AB</b> upptäckta av automatiserad granskning<br>"

    return html

def __html_section_end():
    """html = "</section>"
    return html"""
    return "</section>"

def __html_detail_section_begin(id):
    if id.strip() != "":
        html = '''
        <section id="'''+id+'''" class="home-section">
        <div class="home-content">
          <div class="detail-boxes">
        '''
    else:
        html = '''
        <section class="home-section">
        <div class="home-content">
          <div class="detail-boxes">
        '''
    return html

def __html_section_end():
    """html = '''
    </section>
    '''
    return html"""
    return "</section>"

def __html_recent_inspection_box_begin(title):
    html = ""
    if title.strip() != "":
        html = '''
        <div class="recent-inspection box">
        <div class="title">'''+title+'''</div>
        <div class="inspection-details">
        <ul class="details">
        <li class="topic">
        '''
    return html

def __html_recent_inspection_box_end():
    html = '''
    </ul>
    </div>
    </div>
    </div>
    '''
    return html

def __html_detail_box_begin_TKB():
    html = '''
    <div id = "TKB" class="detail-boxes">
	<div class="recent-inspection box">
    <div class="title">TKB-granskning</div>
    <div class="inspection-details">
    <ul class="details">
    '''
    return html

def __html_detail_box_begin_AB():
    html = '''
        <div id = "AB" class="detail-boxes">
	    <div class="recent-inspection box">
        <div class="title">AB-granskning</div>
        <div class="inspection-details">
        <ul class="details">
    '''
    return html

def __html_detail_box_begin_COMMENTS():
    html = '''
    <div id = "Comments" class="detail-boxes">
	<div class="recent-inspection box">
    <div class="title">Förslag till granskningskommentarer</div>
    <div class="inspection-details">
    <ul class="details">
    '''
    return html

def __box_content_end():
    html = '''
    </ul>
    </div>
    </div>
    '''
    return html
