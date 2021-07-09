
from docx import Document
from flask import Flask, request    # jsonify
import globals
from INFO_inspection_information import *
import io
import requests

##############################
# Startup settings
##############################
# Instantiate the App

app = Flask(__name__)
#app.config['JSON_SORT_KEYS'] = False

#pip install -U flask-cors
#CORS(app)
#2app.config['CORS_HEADERS'] = 'Content-Type'


##############################
# App Endpoints
##############################
app = Flask(__name__)
@app.route('/granskningsinfo')
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def reponse2request():
    """
    Tar emot anrop för endpoint: "/granskningsinfo"

    Verifierar att obligatoriska inparametrar finns, samt anropar då metoder för att granska infospec och TKB

    Returnerar: html
    """
    domain = request.args.get('domain', default="")
    domain_prefix_param = request.args.get('domainprefix', default="")
    tag = request.args.get('tag', default="")
    globals.tag = tag
    alt_IS_name = request.args.get('is', default="")
    alt_TKB_name = request.args.get('tkb', default="")

    globals.granskningsresultat = ""

    if domain != "" and tag != "":
        global domain_prefix
        if domain_prefix_param.strip() != "":
            riv_domain = "riv-application." + domain
            domain_prefix = "riv-application."
        else:
            riv_domain = "riv."+domain
            domain_prefix = "riv."

        __inspect_IS_document(domain, tag, alt_IS_name)
        __inspect_TKB_document(domain, tag, alt_TKB_name)

        html = __get_html_response(riv_domain, IS_page_link, TKB_page_link, IS_document_paragraphs, TKB_document_paragraphs)
    else:
        html = "<br><h1>Webbadressen är inte korrekt!</h1>"
        html += "<br>Någon av de obligatoriska url-parametrarna <i>domain</i> eller <i>tag</i> <b>saknas i anropet!</b>"
        html += "<br><br>Ange dem i adressraden enligt följande exempel: <i>url...</i><b>/granskningsinfo?domain=</b><i>[domännamn utan riv-prefix]</i><b>&tag=</b><i>[tag]</i>"

    return html

##############################
# Internal methods
##############################
def __inspect_IS_document(domain, tag, alt_document_name):
    """
    Beräknar url till infospecdokumentet för angiven domain och tag.

    Laddar ner dokumentet till en virtuell fil som läses in i ett docx-Document.

    Anropar därefter metoden "INFO_inspect_document" som genomför granskning av dokumentet.
    """
    global IS_page_link
    global IS_document_paragraphs
    IS_page_link = __get_document_page_link(domain, tag, globals.IS)
    downloaded_IS_page = __get_downloaded_document(IS_page_link)

    IS_document_paragraphs = ""

    IS_head_hash = __get_head_hash(downloaded_IS_page)
    IS_document_link = __get_document_link(domain, tag, globals.IS, IS_head_hash, alt_document_name)
    downloaded_IS_document = __get_downloaded_document(IS_document_link)
    if downloaded_IS_document.status_code == 404:
        IS_document_paragraphs = __text_document_not_found(globals.IS,domain,tag)
        globals.granskningsresultat += "<br><h2>Infospec</h2>" + __text_document_not_found(globals.IS,domain,tag)
        docx_IS_document = ""
    else:
        globals.docx_IS_document = __get_docx_document(downloaded_IS_document)
        globals.IS_document_exists = True
        ### dev test ###
        for paragraph in globals.docx_IS_document.paragraphs:
            if paragraph.text.strip() != "":
                IS_document_paragraphs += paragraph.text + "<br>"
        ### dev test ###
        INFO_inspect_document(globals.IS)

def __inspect_TKB_document(domain, tag, alt_document_name):
    """
    Beräknar url till TKB-dokumentet för angiven domain och tag.

    Laddar ner dokumentet till en virtuell fil som läses in i ett docx-Document.

    Anropar därefter metoden "INFO_inspect_document" som genomför granskning av dokumentet.
    """
    global TKB_page_link
    global TKB_document_paragraphs
    TKB_page_link = __get_document_page_link(domain, tag, globals.TKB)
    downloaded_TKB_page = __get_downloaded_document(TKB_page_link)

    TKB_document_paragraphs = ""

    TKB_head_hash = __get_head_hash(downloaded_TKB_page)
    TKB_document_link = __get_document_link(domain, tag, globals.TKB, TKB_head_hash, alt_document_name)
    downloaded_TKB_document = __get_downloaded_document(TKB_document_link)
    if downloaded_TKB_document.status_code == 404:
        TKB_document_paragraphs = __text_document_not_found(globals.TKB,domain,tag)
        globals.granskningsresultat += "<br><br><h2>TKB</h2>" + __text_document_not_found(globals.TKB,domain,tag)
        docx_TKB_document = ""
    else:
        globals.docx_TKB_document = __get_docx_document(downloaded_TKB_document)
        globals.TKB_document_exists = True
        ### dev test ###
        for paragraph in globals.docx_TKB_document.paragraphs:
            if paragraph.text.strip() != "":
                TKB_document_paragraphs += paragraph.text + "<br>"
        ### dev test ###
        INFO_inspect_document(globals.TKB)


def __get_document_page_link(domainname, tag, document):
    """
    Beräknar url till sidan som innehåller länk till angivet dokument för vald domän och tag i Bitbucket-repot.

    Returenar: länk till dokumentsidan
    """
    url_prefix = "https://bitbucket.org/rivta-domains/"
    global domain_prefix
    url_domain = domain_prefix + domainname + "/"
    url_src = "src/"
    url_tag = tag + "/"
    url_docs = "docs/"
    domain_name = domainname.replace(".","_")
    url_doc = document +"_" + domain_name + ".docx"
    document_page_link = url_prefix+url_domain+url_src+url_tag+url_docs+url_doc

    return document_page_link

def __get_domain_docs_link(domainname, tag):
    """
    Beräknar url till docs-sidan för vald domän och tag i Bitbucket-repot.

    Returenar: länk till dokumentsidan
    """
    url_prefix = "https://bitbucket.org/rivta-domains/"
    global domain_prefix
    url_domain = domain_prefix + domainname + "/"
    url_src = "src/"
    url_tag = tag + "/"
    url_docs = "docs/"
    document_page_link = url_prefix+url_domain+url_src+url_tag+url_docs

    return document_page_link

def __get_document_link(domainname, tag, document, head_hash, alt_document_name):
    """
    Beräknar url till angivet dokument för vald domän och tag i Bitbucket-repot.

    Returenar: länk som kan användas vid nerladdning av angivet dokument
    """
    url_prefix = "https://bitbucket.org/rivta-domains/"
    url_domain = "riv." + domainname + "/"
    url_raw = "raw/"
    url_docs = "docs/"
    domain_name = domainname.replace(".","_")
    if len(alt_document_name.strip()) > 0:
        url_doc = alt_document_name
    else:
        url_doc = document +"_" + domain_name + ".docx"
    document_link = url_prefix+url_domain+url_raw+head_hash+"/"+url_docs+url_doc

    if document == globals.IS:
        globals.IS_document_name = url_doc
    elif document == globals.TKB:
        globals.TKB_document_name = url_doc

    return document_link

def __get_downloaded_document(document_link):
    """
    Laddar ner dokument från angiven länk.

    Returenar: nerladdat dokument
    """
    downloaded_doc = requests.get(document_link, stream=True)

    return downloaded_doc

"""def __get_document_in_docx_format(document):
    docx_document = document.content

    return docx_document"""

def __get_head_hash(document_page):
    """
    hämtar head-hash för det dokument som ska laddas ner. Hashen finns i den Bitbucketsida som innehåller länk till dokumentet.

    Returenar: head-hash
    """
    hash_start = document_page.text.find('{"hash":')
    hash_end = hash_start+17
    head_hash = document_page.text[hash_start+10:hash_end]

    return head_hash

def __get_docx_document(downloaded_document):
    """
    Läser in angivet dokuments innehåll i ett docx-Document.

    Returenar: docx-Documentet
    """
    with io.BytesIO(downloaded_document.content) as inmemoryfile:
        docx_document = Document(inmemoryfile)

    return docx_document

def __text_document_not_found(doc, domain, tag):
    """
    Sammanställer ett meddelande till användaren då sökt dokument saknas eller då fel dokumentnamn har angivits.

    Returenar: information i html-format
    """
    document_name = "Infospec"
    if doc == globals.TKB:
        document_name = globals.TKB

    document_info = document_name + " saknas eller har annat namn än det förväntade: <i>" + doc.upper() + "_" + domain.replace(".", "_") + ".docx</i>"
    docs_link = __get_domain_docs_link(domain, tag)
    document_info += "<br>Kontrollera dokumentnamn här: <a href='" + docs_link + "'" + " target='_blank'>" + docs_link + "</a>"
    document_info += "<br>Om det finns en " + document_name + " så har den ett annat än det förväntade namnet. "
    document_info += "I så fall kan du ange det namnet som en url-parameter enligt: <i>url...</i><b>&is=dokumentnamn</b>"
    document_info += "<br>Om detta är en applikationsspecifik domän kan du ange det i en url-parameter enligt: <i>url...</i><b>&domainprefix=true</b>"

    return document_info


def __get_html_response(riv_domain, IS_page_link, TKB_page_link, IS_document_paragraphs, TKB_document_paragraphs):
    """
    Sammanställer ett meddelande till användaren med granskningsresultat

    Returenar: information i html-format
    """
    """html = '''
        <h1>I-granskningsstöd för: {}</h1>
        <br><h2><a href={}>Infospec-sida</a> &nbsp;&nbsp;&nbsp; <a href={}>TKB-sida</a></h2>
        <br><h2><b>IS-paragrafer:</b></h2> {}
        <br><h2><b>TKB-paragrafer:</b></h2> {}
        '''.format(riv_domain, IS_page_link, TKB_page_link, IS_document_paragraphs, TKB_document_paragraphs)"""

    html = '''
        <h1>I-granskningsstöd för: {}</h1>
        <br>{}
        '''.format(riv_domain, globals.granskningsresultat)

    return html

if __name__ == '__main__':
    from argparse import ArgumentParser

    port = 4001
    usedHost = 'https://callistabackend.herokuapp.com'
    instance_address = "http://" + usedHost + ":" + str(port)

    usedHost = '127.0.0.1'
    app.run(host=usedHost, port=port)

