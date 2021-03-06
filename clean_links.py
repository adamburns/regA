LINKS = "links.txt"
CIKS = "ciks.txt"


def clean_links():
    input = open(LINKS, "r")
    output = open(CIKS, "w")
    data = input.readlines()
    lines = sum(1 for line in open(LINKS))

    for line in range(0, lines):
        if "opennew" in data[line]:
            newline = data[line][data[line].rfind("opennew")+9:data[line].rfind("xml")+3]
            newline = newline[39:-48]
            output.write(newline)
            output.write("\n")

    input.close()
    output.close()
