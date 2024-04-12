# xml_processor.py

import xml.etree.ElementTree as ET
import json

def extract_links_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    namespaces = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    all_links = []
    for url_element in root.findall('sitemap:url', namespaces):
        loc_element = url_element.find('sitemap:loc', namespaces)
        if loc_element is not None:
            all_links.append(loc_element.text)
    return json.dumps(all_links, indent=4)