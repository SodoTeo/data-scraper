from xml_processor import extract_links_from_xml
from link_filter import filter_links

# Example usage
xml_file = '../sitemaps/gohugo.xml'  # XML file to process

# Extract and save links from xml
clean_links = extract_links_from_xml(xml_file)

# Define parent paths for filtering
parent_paths = ['getting-started', 'installation']

# Filter links and save them
filter_links(clean_links, parent_paths)