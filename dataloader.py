import polars as pl
def load():
    d1 = pl.read_excel(source="C://Users//drish//Python_Projects_And_Repos//Billscrape//dataframe.xlsx",sheet_name="Sheet1",schema_overrides={"Mobile":pl.String})
    dc=d1["Provider"]
    dn=d1["Mobile"]
    dbu=d1["BU"]
    return [dc,dn,dbu]