import bs4 as bs
import urllib.request

#Constants
URL_PREFIX = https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text
URL_SUFFIX = 


def open_url():
    try: 
        broth = urllib.request.urlopen(URL).read()
    except (http.client.IncompleteRead) as e: 
        broth = e.partial
    return broth


def modify_url(startDoc):
    URL = (URL_PREFIX
           + startDoc
           + URL_SUFFIX)
    return URL


def export_urls():
    for a in soup.find_all('a', href=True):
        output.write(a['href'])
        output.write("\n")


