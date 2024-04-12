from doc_maker import extract_links_from_xml, filter_links, scrape_content_from_links

def main():
    xml_file = 'sitemaps/gohugo.xml'  # Adjust path as necessary
    output_json = 'gohugo.json'       # Adjust path as necessary

    # Extract and save links from XML
    clean_links = extract_links_from_xml(xml_file)

    # Define parent paths for filtering
    parent_paths = ['getting-started', 'installation']

    # Filter links and save them
    links_to_be_scraped = filter_links(clean_links, parent_paths)

    # Scrape content from links and save to JSON
    scrape_content_from_links(links_to_be_scraped, output_json)

    print("Process completed successfully.")

if __name__ == "__main__":
    main()
