#boolean mask:
import pandas as pd
df=pd.read_json("Homework2/band_gap_data.json")
mask=((df["temperature_K"]> 50)&(df["crystallinity"]== "Polycrystalline")&(df["exp_method"]== "Reflection"))
print(df[mask])

# `for`-loop while utilizing `iat`:
filtered_rows = []
for i in range(len(df)):
    tem=df.iat[i,df.columns.get_loc("temperature_K")]
    cryst=df.iat[i,df.columns.get_loc("crystallinity")]
    method=df.iat[i,df.columns.get_loc("exp_method")]
    if pd.notna(tem) and tem>50 and cryst== "Polycrystalline" and method=="Reflection":
        filtered_rows.append(df.iloc[i])
filtered_df = pd.DataFrame(filtered_rows)
print(filtered_df)

#`iloc`:
filtered_rows2 = []
for i in range(len(df)):
     temp = df.iloc[i]["temperature_K"]
     cryst = df.iloc[i]["crystallinity"]
     method = df.iloc[i]["exp_method"]
     if pd.notna(tem) and tem>50 and cryst== "Polycrystalline" and method=="Reflection":
        filtered_rows2.append(df.iloc[i])
filtered_df2 = pd.DataFrame(filtered_rows2)
print(filtered_df2)
