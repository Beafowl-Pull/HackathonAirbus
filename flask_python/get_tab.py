#!/usr/bin/env python3
from pathlib import Path
import sys

class Metal:
    def __init__(self, Metal: str, SmelterID: str, StandardSmelterName: str, State_Province_Region: str, CountryLocation: str, CompanyWebsitewithCMPolicy: str, LastAuditDate: str, AuditCycle: str, ReauditInProgress: str, LBMARG: str, RJC: str):
        self.metal = Metal
        self.smelterid = SmelterID
        self.standardsmeltername = StandardSmelterName
        self.state_province_region = State_Province_Region
        self.countrylocation = CountryLocation
        self.companywebsitewithcmpolicy = CompanyWebsitewithCMPolicy
        self.lastauditdate = LastAuditDate
        self.auditcycle = AuditCycle
        self.reauditinprogress = ReauditInProgress
        self.lbmarg = LBMARG
        self.rjc = RJC
        self.error = False

    def display(self):
        print("Metal:\t\t\t\t", self.metal)
        print("Smelter ID\t\t\t", self.smelterid)
        print("Standard Smelter Name:\t\t", self.standardsmeltername)
        print("State/Province/Region:\t\t", self.state_province_region)
        print("Country Location:\t\t", self.countrylocation)
        print("Company Website with CMPolicy:\t", self.companywebsitewithcmpolicy)
        print("Last Audit Date:\t\t", self.lastauditdate)
        print("Audit Cycle:\t\t\t", self.auditcycle)
        print("Reaudit In Progress:\t\t", self.reauditinprogress)
        print("LBMARG:\t\t\t\t", self.lbmarg)
        print("RJC:\t\t\t\t", self.rjc)

def get_tab(tab):
    metals = []
    path = Path().absolute()
    tab = open(f"{path}/{tab}", "r")
    full = tab.read()
    for data in full.split("<Row>")[1:]:
        data = data.split("</Row>")
        for j, i in enumerate(data):
            data[j] = i.split('</Data></Cell>')
            for x, y in enumerate(data[j]):
                data[j][x] = y.split(">")[-1]
        data = data[0]
        if (len(data) >= 11):
            metals.append(Metal(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    return metals

def get_element_by_id(metals: Metal, id: str):
    if (id.lower() in "metal" or "metal" in id.lower()):
        return metals.metal
    if (id.lower() in "smelterid" or "smelterid" in id.lower()):
        return metals.smelterid
    if (id.lower() in "standardsmeltername" or "standardsmeltername" in id.lower()):
        return metals.standardsmeltername
    if (id.lower() in "state_province_region" or "state_province_region" in id.lower()):
        return metals.state_province_region
    if (id.lower() in "countrylocation" or "countrylocation" in id.lower()):
        return metals.countrylocation
    if (id.lower() in "companywebsitewithcmpolicy" or "companywebsitewithcmpolicy" in id.lower()):
        return metals.companywebsitewithcmpolicy
    if (id.lower() in "lastauditdate" or "lastauditdate" in id.lower()):
        return metals.lastauditdate
    if (id.lower() in "auditcycle" or "auditcycle" in id.lower()):
        return metals.auditcycle
    if (id.lower() in "reauditinprogress" or "reauditinprogress" in id.lower()):
        return metals.reauditinprogress
    if (id.lower() in "lbmarg" or "lbmarg" in id.lower()):
        return metals.lbmarg
    if (id.lower() in "rjc" or "rjc" in id.lower()):
        return metals.rjc
    print(f"error: {id} is not a valid id")
    return "error"

def get_search(metals, search: str, name: str):
    output = []
    for metal in metals:
        element = get_element_by_id(metal, search)
        if (element != "error"):
            if (element.lower() in name.lower() or name.lower() in element.lower()):
                output.append(metal)
    if (output == []):
        print(f"error: no '{name}' in category '{search}'")
    return output

def put_html_tab(tab, nbr_indent = 0):
    output = "  " * 4 + "<tr>\n"
    for i in tab:
        output += ("  " * nbr_indent) + "<th>" + i + "</th>\n"
    output += "  " * 4 + "</tr>\n"
    return output

def add_header_part():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href='static/header.css'>
    <link rel="stylesheet" href='static/log-in.css'>
    <link rel="stylesheet" href='static/tableau.css'>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href='static/footer_log-in.css'>
    <link rel="icon" href="https://logodix.com/logo/884365.png" type="image/icon type">
    <script src="../script.js"></script>
    <title>Supplier conflict minerals tool</title>
</head>
<body>
    <header>
        <a href="main"><img src="https://1000marcas.net/wp-content/uploads/2020/01/Airbus-emblema-600x338.jpg" alt=""> </a>
        <div id="links">
            <a href="main" class="link" > Home </a>
            <a href="register" class="link" > Declaration Forms </a>
            <a href="getdata" class="link" > Get data </a>
            <a href="suppliers" class="link" > Supplier page </a>
            <a href="log-in" class="link" > Login </a>
        </div>
    </header>
    <main>
        <h1>Result for you research: </h1>
        <div class=parsed>
"""

def add_footer_part():
    return """
        </div>
        <a href="getdata" class="link2" > Another research? </a>
    </main>
    <footer>
        <div class="footer">
            <img class="image_left" src="https://1000marcas.net/wp-content/uploads/2020/01/Airbus-emblema-600x338.jpg" alt="">
            <div id="links_f">
                <a href="termofuse" class="link_f" > Term Of Use </a>
                <a href="privacy" class="link_f" > Privacy Policy </a>
                <a href="contact" class="link_f" > Contact Use </a>
                <a href="cookie" class="link_f" > Cookie Settings </a>
                <a> ©Airbus 2022 </a>
            </div>
            <div class="left">
                <p>
                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley">
                        <img src="https://cdn.pixabay.com/photo/2015/05/17/10/51/facebook-770688_960_720.png" alt="">
                    </a>
                    <a href="https://www.instagram.com/">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png" alt="">
                    </a>
                    <a href="https://www.twitter.com/">
                        <img src="https://cdn-icons-png.flaticon.com/512/124/124021.png" alt="">
                    </a>
                </p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

def tab_to_html(metals):
    tab = add_header_part()
    tab += '<html lang="en">\n  <header>\n    <div class=parsed>\n      <table border="1">\n'
    classes = ["metal", "smelterid", "standardsmeltername", "state_province_region", "countrylocation", "companywebsitewithcmpolicy", "lastauditdate", "auditcycle", "reauditinprogress", "lbmarg", "rjc"]
    tab += put_html_tab(classes, 5)
    for metal in metals:
        tab += 8 * " " + "<tr>\n"
        for i in classes:
            tab += " " * 10 + "<td>" + get_element_by_id(metal, i) + "</td>\n"
        tab += 8 * " " + "</tr>\n"
    tab += '      </table>\n'
    tab += add_footer_part()
    return (tab)

def search_bar(argv = []):
    if (len(argv) != 2):
        return 84
    metals = get_tab("FullConformantSmelter_List2022-06-01.xml")
    metals = get_search(metals, argv[0], argv[1])
    for i in metals:
        i.display()
    return tab_to_html(metals)
