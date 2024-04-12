from xml_processor import extract_links_from_xml, save_results_to_json

# Example usage
xml_file = '../sitemaps/gohugo.xml'  # XML file to process
parent_paths = ['./getting-started', './installation'] # Parent paths to search within the XML
output_file = '../clean_links.json'

links = extract_links_from_xml(xml_file)
save_results_to_json(links, output_file)
