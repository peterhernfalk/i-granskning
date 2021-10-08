
from docx import Document
import Document_mangagement
from flask import Flask, request    # jsonify
from flask_cors import CORS

import granskning_AB
import granskning_TKB
from granskning_TKB import *
import granskning_IS
import html_dashboard
#from html_dashboard import *

#import globals
#import io
from repo import *
#import requests

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

    ###########################
    ### 2do: förenkla koden ###
    ###########################

    ##### PREPARE #####
    globals.GLOBALS_init()
    domain = request.args.get('domain', default="")
    domain = domain.replace("riv.","")
    domain = domain.replace("riv-application.","")
    globals.domain_name = domain
    domain_prefix_param = request.args.get('domainprefix', default="")
    tag = request.args.get('tag', default="")
    globals.tag = tag
    alt_AB_name = request.args.get('ab', default="")
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
        granskning_IS.prepare_IS_inspection(domain, tag, alt_IS_name)
        globals.alt_document_name = alt_IS_name
        if globals.IS_exists == True:
            granskning_IS.perform_IS_inspection()

        globals.docx_document = globals.TKB
        granskning_TKB.prepare_TKB_inspection(domain, tag, alt_TKB_name)
        if globals.TKB_exists == True:
            granskning_TKB.perform_TKB_inspection()

        globals.docx_document = globals.AB
        granskning_AB.prepare_AB_inspection(domain, tag, alt_AB_name)
        if globals.AB_exists == True:
            granskning_AB.perform_AB_inspection()


        #html = __get_html_response(riv_domain, IS_page_link, TKB_page_link, IS_document_paragraphs, TKB_document_paragraphs)
        html = html_dashboard.get_page_html()
    else:
        html = "<br><h1>Webbadressen är inte korrekt!</h1>"
        html += "<br>Någon av de obligatoriska url-parametrarna <i>domain</i> eller <i>tag</i> <b>saknas i anropet!</b>"
        html += "<br><br>Ange dem i adressraden enligt följande format: <i>url...</i><b>/granskningsinfo?domain=</b><i>[domännamn utan riv-prefix]</i><b>&tag=</b><i>[tag]</i>"

    ##### REPLY #####
    return html


if __name__ == '__main__':
    port = 4001
    usedHost = '127.0.0.1'
    app.run(host=usedHost, port=port)

