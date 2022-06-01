#!/usr/bin/env python3
from pathlib import Path

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
        if (get_element_by_id(metal, search).lower() in name.lower() or name.lower() in get_element_by_id(metal, search).lower()):
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


def tab_to_html(metals):
    path = Path().absolute()
    tab = open(f"{path}/tab.html", "w")
    tab.write('<html lang="en">\n  <header>\n    <div class=parsed>\n      <table border="1">\n')
    classes = ["metal", "smelterid", "standardsmeltername", "state_province_region", "countrylocation", "companywebsitewithcmpolicy", "lastauditdate", "auditcycle", "reauditinprogress", "lbmarg", "rjc"]
    tab.write(put_html_tab(classes, 5))
    for metal in metals:
        tab.write(8 * " " + "<tr>\n")
        for i in classes:
            tab.write(" " * 10 + "<td>" + get_element_by_id(metal, i) + "</td>\n")
        tab.write(8 * " " + "</tr>\n")
    tab.write('      </table>\n    </div>\n  </header>\n</html>')

metals = get_tab("FullConformantSmelter_List2022-06-01.xml")
#for i in get_search(metals, "metals", "golds"):
#    i.display()
#    print("")

tab_to_html(get_search(metals, "country", "germany"))

