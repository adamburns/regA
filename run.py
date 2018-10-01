import url_scrape.py as us


def main():
    for x in range(4):
        open_url(modify_url(x))
        export_links(open_output_file())


def get_links():
    for x in range(4):
        open_url(modify_url(x))
        export_links(open_output_file())


def scrape_links():
    
    

if __name__ == "__main__":
    main()
