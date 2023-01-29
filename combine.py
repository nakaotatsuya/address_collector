import pandas as pd
import numpy as np
import os
from pathlib import Path

data_loc = "data"
data_loc = Path(data_loc)
data_loc = str(data_loc.resolve())

save_path = "data/combined_data"
save_path = Path(save_path)
save_path = str(save_path.resolve())

files = os.listdir(data_loc)
files = [f for f in files if os.path.isfile(os.path.join(data_loc, f))]

df_concat = pd.DataFrame()
labels = ["tel_number", "name", "prefecture", "city_ward", "chome", "detail"]
labels_dict = {num: label for num, label in enumerate(labels)}

for file in files:
    file_name = os.path.join(data_loc, file)
    df = pd.read_csv(file_name, header=None)
    df = df.rename(columns = labels_dict)
    #print(len(df))
    df_concat = pd.concat([df_concat, df])

save_name_pref = df["prefecture"].iloc[0]
save_name_city = df["city_ward"].iloc[0]
save_path = os.path.join(save_path, save_name_pref + save_name_city + ".csv")
df_concat.to_csv(save_path, index=False)
#print(df_concat)