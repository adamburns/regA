import url_scrape as us
import clean_links as cl
#import clean_xml as cx


def main():
    get_links()
    cl.clean_links()

def get_links():
    output = us.open_output_file()
    for x in range(4):
        broth = us.open_url(us.modify_url((100*x)+1))
        us.export_links(output, broth)
    us.close_output_file(output)


if __name__ == "__main__":
    main()
