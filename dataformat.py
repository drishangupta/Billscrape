import polars as pl
import re

def data_gather():
    d1 = pl.read_excel(source="C://Users//drish//Downloads//BILL CHECK.xlsx",sheet_name="Sheet1",schema_overrides={"Mobile":pl.String,"BU":pl.Int32})
    dc = d1["Provider"]
    dbu=d1["BU"]

    pattern_replacement_dict = {
        "APDCL \(Non-RAPDR\)": "Assam",
        "BSES Rajdhani": "bses rajdhani pow",
        "BSES Yamuna": "bses yamuna pow",
        "\"CESC\"": "calc",
        "CHANDIGARH ELECTRICITY DEPARTMENT": "chandi",
        "Madhya Kshetra Vitaran \(Urban\)": "urban",
        "MSEDC": "mahara",
        "Paschim Gujarat Vij Company Limited \(PGVCL\)": "paschim gujarat",
        "Paschim Kshetra Vitaran": "paschim kshe",
        "TP Central Odisha Distribution Ltd": "tp central",
        "Uttarakhand Power Corporation Limited": "uttarakhand",
        "WBSEDCL": "west bengal state",
        "Tata Power - MUMBAI":"tata power - mumbai - mumbai",
        "Tata Power - DELHI":"tata power - delhi - delhi",
        "Torrent Power - AHMEDABAD" : "Torrent Power AHMEDABAD",
        "Torrent Power - SURAT" : "Torrent Power SURAT",
        "Dakshin Haryana Bijli Vitran Nigam \(DHBVN\)":"dakshin har",
        "UPCL":"uttarakhand"
        
        
    }

    for pattern, replacement in pattern_replacement_dict.items():
        dc = dc.str.replace_all(pattern, replacement)
        
    pattern = r"\s-([^-]+)$"
    replacement = ""

    dc = dc.str.replace_all(pattern, replacement)
    

    d1.replace_column(0,dc)
    d1.replace_column(3,dbu)
    d1.write_excel(include_header=True,autofit=True)
data_gather()
