import json
import re

def filter_links(o_links, parent_paths):
    links = json.loads(o_links)
    print(f"Total links loaded: {len(links)}")

    # Compile regex patterns to match URLs that include the specific paths
    regex_patterns = [re.compile(rf".*{path}.*") for path in parent_paths]

    # Filter links based on regex patterns, adding detailed debugging
    filtered_links = []
    for link in links:
        match_found = False
        for pattern in regex_patterns:
            if pattern.search(link):
                match_found = True
                break
        if match_found:
            filtered_links.append(link)
    
    print(f"Number of filtered links: {len(filtered_links)}")
    return json.dumps(filtered_links, indent=4)
