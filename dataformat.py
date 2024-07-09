import polars as pl
import re

def data_gather():
    d1 = pl.read_excel(source="C://Users//drish//Downloads//test data.xlsx",sheet_name="Sheet1",schema_overrides={"Mobile":pl.String})
    dc = d1["Provider"]
    print

    pattern = r"\s-([^-]+)$"
    replacement = ""

    dc = dc.str.replace_all(pattern, replacement)

    pattern_replacement_dict = {
        "APDCL (Non-RAPDR)": "Assam",
        "BSES Rajdhani": "bses rajdhani pow",
        "BSES Yamuna": "bses yamuna pow",
        "CESC": "calc",
        "CHANDIGARH ELECTRICITY DEPARTMENT": "chandi",
        "Madhya Kshetra Vitaran (Urban)": "urban",
        "MSEDC": "mahara",
        "Paschim Gujarat Vij Company Limited (PGVCL)": "paschim gujarat",
        "Paschim Kshetra Vitaran": "paschim kshe",
        "Tata Power": "tata power - mumbai",
        "TP Central Odisha Distribution Ltd": "tp central",
        "Uttarakhand Power Corporation Limited": "uttarakhand",
        "WBSEDCL": "west bengal state"
    }

    for pattern, replacement in pattern_replacement_dict.items():
        dc = dc.str.replace_all(pattern, replacement)

    d1.replace_column(0,dc)
    d1.write_excel(include_header=True,)
data_gather()
