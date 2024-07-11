import polars as pd
import re
strings = {"index":[1,2,3],"value":["Hello world", "Python is great", "I love programming"]}
df=pd.DataFrame(strings)
print(df["value"])
pattern=r"\s(\w+)$"
replace=""
last_word = df["value"][1].split()[-1]
valuess=df.item(1,"value")
valuess=valuess.replace(last_word,"")
valuess.rstrip
print(valuess)