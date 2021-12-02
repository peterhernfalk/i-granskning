
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import globals
import granskning_AB
import granskning_IS
import granskning_TKB
import re
import requests.exceptions
from requests import head
from requests.exceptions import MissingSchema
import urllib3

def extract_urls_from_table(document, table_number):
    rels = document.part.rels
    document_relations = {}
    for rel in rels:
        if rels[rel].reltype == RT.HYPERLINK:
            document_relations[rel] = rels[rel]._target

    table = document.tables[table_number]
    links = []
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                xml_str = str(paragraph.paragraph_format.element.xml)
                if "<w:hyperlink" in xml_str or 'w:val="Hyperlink"' in xml_str:
                    wt_list = re.findall('<w:t[\S\s]*?</w:t>', xml_str)
                    if "<w:t xml:" not in str(wt_list[0]):
                        hyperlink = str(wt_list[0]).replace("<w:t>","").replace("</w:t>","")
                        if hyperlink.endswith("%20"):
                            hyperlink = hyperlink.removesuffix("%20")
                        if "http" not in hyperlink:
                            ### Workaround for w:t that contains disply text instead of url ###
                            relation_id = re.findall('r:id="[\S\s]*?"', xml_str)
                            if len(relation_id) > 0:
                                relation_id_key = str(relation_id[0]).replace('r:id=','').replace('"','')
                                hyperlink = document_relations[relation_id_key]
                        if globals.docx_document == globals.TKB:
                            if "http" not in hyperlink:
                                ### Workaround for when complete url is found in <w:instrText instead of in <w:t ###
                                link_in_instrtext = re.findall('HYPERLINK "[\S\s]*?"', xml_str)
                                link_in_instrtext_str = str(link_in_instrtext[0]).replace('HYPERLINK "','').replace('"','')
                                hyperlink = link_in_instrtext_str
                        links.append(hyperlink)
                elif paragraph.text.lower().find("http") >= 0:
                    paragraph_links = paragraph.text.split("\n")
                    for paragraph_link in paragraph_links:
                        if paragraph_link.lower().find("http") >= 0:
                            if paragraph_link.strip() != "":
                                links.append(paragraph_link)

    return links


def write_detail_box_content(text):
    detail_box_content = "<li>" + text + "</li>"
    if globals.docx_document == globals.IS:
        granskning_IS.IS_detail_box_contents += detail_box_content
    elif globals.docx_document == globals.TKB:
        granskning_TKB.TKB_detail_box_contents += detail_box_content
    elif globals.docx_document == globals.AB:
        granskning_AB.AB_detail_box_contents += detail_box_content

def write_output_without_newline(text):
    globals.granskningsresultat += text


def verify_url_exists(searched_url):
    status_code = 200
    urllib3.disable_warnings()
    try:
        response = head(searched_url.strip(), allow_redirects=True, verify=False)    #If needed, this can be added: timeout=2
        status_code = response.status_code
    except requests.exceptions.ConnectionError:
        status_code = 400  # http status code, meaning bad request
    except MissingSchema:
        status_code = 400   # http status code, meaning bad request
    except requests.exceptions.InvalidSchema:
        status_code = 400   # http status code, meaning bad request
    #else:
    #    status_code = 400  # http status code, meaning bad request
    return status_code
