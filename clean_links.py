LINKS = "links.txt"
URLS = "urls.txt"


def clean_links():
    input = open(LINKS, "r")
    output = open(URLS, "w")
    data = input.readlines()
    lines = sum(1 for line in open(LINKS))

    for line in range(0, lines):
        if "opennew" in data[line]:
            newline = data[line][data[line].rfind("opennew")+9:data[line].rfind("xml")+3]
            newline = newline[:-27] + "primary_doc.xml"
            output.write(newline)
            output.write("\n")

    input.close()
    output.close()
