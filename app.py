
from docx import Document
import DOC_document
from flask import Flask, request    # jsonify
from flask_cors import CORS

import html_dashboard
from html_dashboard import *

import globals
from INFO_document_inspection import *
import io
from repo import *
import requests

##############################
# Startup settings
##############################
# Instantiate the App
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#pip install -U flask-cors
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


##############################
# App Endpoints
##############################
app = Flask(__name__)
@app.route('/')
def emptyrequest():
    """
    Tar emot anrop för endpoint: "/"

    Sätter ihop och returnerar text som ska underlätta för användaren att förstå hur anropet ska utformas.

    Returnerar: en sträng med html-innehåll
    """
    ##### PREPARE #####
    html = ""
    html = "<br><h1>Webbadressen är inte korrekt!</h1>"
    html += "<br>Någon av de obligatoriska url-parametrarna <i>domain</i> eller <i>tag</i> <b>saknas i anropet!</b>"
    html += "<br><br>Ange dem i adressraden enligt följande format: <i>url...</i><b>/granskningsinfo?domain=</b><i>[domännamn utan riv-prefix]</i><b>&tag=</b><i>[tag]</i>"
    html += "<br><br>Exempelvis: <i><a href='https://i-granskning.herokuapp.com/granskningsinfo?domain=clinicalprocess.healthcond.certificate&tag=4.0.5'>https://i-granskning.herokuapp.com/granskningsinfo?domain=clinicalprocess.healthcond.certificate&tag=4.0.5</a></i>"

    ##### REPLY #####
    return html

@app.route('/granskningsinfo')
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def reponse2request():
    """
    Tar emot anrop för endpoint: "/granskningsinfo"

    Verifierar att obligatoriska inparametrar finns, samt anropar då metoder för att granska infospec och TKB

    Returnerar: en sträng med html-innehåll
    """

    ##### PREPARE #####
    globals.GLOBALS_init()
    #detail_box_content = ""
    domain = request.args.get('domain', default="")
    domain = domain.replace("riv.","")
    domain = domain.replace("riv-application.","")
    globals.domain_name = domain
    domain_prefix_param = request.args.get('domainprefix', default="")
    tag = request.args.get('tag', default="")
    globals.tag = tag
    alt_IS_name = request.args.get('is', default="")
    alt_TKB_name = request.args.get('tkb', default="")

    if domain != "" and tag != "":
        if domain_prefix_param.strip() != "":
            riv_domain = "riv-application." + domain
            globals.domain_prefix = "riv-application."
        else:
            riv_domain = "riv."+domain
            globals.domain_prefix = "riv."

        ##### INSPECT #####
        globals.docx_document = globals.IS
        __inspect_IS_document(domain, tag, alt_IS_name)

        globals.docx_document = globals.TKB
        __inspect_TKB_document(domain, tag, alt_TKB_name)

        #html = __get_html_response(riv_domain, IS_page_link, TKB_page_link, IS_document_paragraphs, TKB_document_paragraphs)
        html = html_dashboard.get_page_html()
    else:
        html = "<br><h1>Webbadressen är inte korrekt!</h1>"
        html += "<br>Någon av de obligatoriska url-parametrarna <i>domain</i> eller <i>tag</i> <b>saknas i anropet!</b>"
        html += "<br><br>Ange dem i adressraden enligt följande format: <i>url...</i><b>/granskningsinfo?domain=</b><i>[domännamn utan riv-prefix]</i><b>&tag=</b><i>[tag]</i>"

    ##### REPLY #####
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
    #IS_page_link = __get_document_page_link(domain, tag, globals.IS)
    #downloaded_IS_page = __get_downloaded_document(IS_page_link)
    IS_page_link = DOC_document.DOC_get_document_page_link(domain, tag, globals.IS)
    downloaded_IS_page = DOC_document.DOC_get_downloaded_document(IS_page_link)

    IS_document_paragraphs = ""

    IS_head_hash = DOC_document.DOC_get_head_hash(downloaded_IS_page)
    IS_document_link = DOC_document.DOC_get_document_link(domain, tag, globals.IS, IS_head_hash, alt_document_name)
    downloaded_IS_document = DOC_document.DOC_get_downloaded_document(IS_document_link)
    if downloaded_IS_document.status_code == 404:
        ###IS_document_paragraphs = APP_text_document_not_found(globals.IS, domain, tag)
        ###globals.granskningsresultat += "<br><h2>Infospec</h2>" + APP_text_document_not_found(globals.IS, domain, tag)
        #globals.IS_felmeddelande = APP_text_document_not_found(globals.IS, domain, tag)
        globals.IS_exists = False
        docx_IS_document = ""
    else:
        globals.docx_IS_document = DOC_document.DOC_get_docx_document(downloaded_IS_document)
        globals.IS_document_exists = True
        globals.IS_exists = True
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
    #TKB_page_link = __get_document_page_link(domain, tag, globals.TKB)
    #downloaded_TKB_page = __get_downloaded_document(TKB_page_link)
    TKB_page_link = DOC_document.DOC_get_document_page_link(domain, tag, globals.TKB)
    downloaded_TKB_page = DOC_document.DOC_get_downloaded_document(TKB_page_link)

    TKB_document_paragraphs = ""

    TKB_head_hash = DOC_document.DOC_get_head_hash(downloaded_TKB_page)
    TKB_document_link = DOC_document.DOC_get_document_link(domain, tag, globals.TKB, TKB_head_hash, alt_document_name)
    downloaded_TKB_document = DOC_document.DOC_get_downloaded_document(TKB_document_link)
    if downloaded_TKB_document.status_code == 404:
        ###TKB_document_paragraphs = APP_text_document_not_found(globals.TKB, domain, tag)
        ###globals.granskningsresultat += "<br><br><h2>TKB</h2>" + APP_text_document_not_found(globals.TKB, domain, tag)
        docx_TKB_document = ""
        #globals.TKB_felmeddelande = APP_text_document_not_found(globals.TKB, domain, tag)
        globals.TKB_exists = False
    else:
        globals.docx_TKB_document = DOC_document.DOC_get_docx_document(downloaded_TKB_document)
        globals.TKB_document_exists = True
        globals.TKB_exists = True
        ### dev test ###
        for paragraph in globals.docx_TKB_document.paragraphs:
            if paragraph.text.strip() != "":
                TKB_document_paragraphs += paragraph.text + "<br>"
        ### dev test ###
        INFO_inspect_document(globals.TKB)


if __name__ == '__main__':
    #from argparse import ArgumentParser

    port = 4001
    usedHost = '127.0.0.1'
    app.run(host=usedHost, port=port)

