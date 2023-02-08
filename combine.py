import pandas as pd
# import numpy as np
import os
from pathlib import Path
import argparse

from jusho import Jusho

def combine_data(pref_id, city_id):
    data_loc = "data"
    data_loc = os.path.join(data_loc, pref_id)
    data_loc = os.path.join(data_loc, city_id)

    data_loc = Path(data_loc)
    data_loc = str(data_loc.resolve())
    
    files = os.listdir(data_loc)
    files = [f for f in files if os.path.isfile(os.path.join(data_loc, f))]
    files.sort()
    
    df_concat = pd.DataFrame()
    labels = ["tel_number", "name", "prefecture", "city_ward", "chome", "detail"]
    labels_dict = {num: label for num, label in enumerate(labels)}

    for file in files:
        file_name = os.path.join(data_loc, file)
        df = pd.read_csv(file_name, header=None)
        df = df.rename(columns = labels_dict)
        #print(len(df))
        #print(df)

        #zip code
        postman = Jusho(database_path=Path("./database.db"))
        prefecture = postman.search_prefectures(df["prefecture"].iloc[0])[0]
        city = postman.search_cities(df["city_ward"].iloc[0], prefecture=prefecture)[0]
        #print(city)
        cho = postman.search_addresses(df["chome"].iloc[0], city=city)
        if not cho:
            df["zip_code"] = ""
        else:
            #print(cho[0])
            df["zip_code"] = cho[0].hyphen_zip
        #print(cho.hyphen_zip)
        
        df_concat = pd.concat([df_concat, df])

    #print(df_concat.loc[df_concat["zip_code"] == ""])

    save_name_pref = df["prefecture"].iloc[0]
    save_name_city = df["city_ward"].iloc[0]

    save_path = os.path.join(data_loc, "combined_data")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_path = os.path.join(save_path, save_name_pref + save_name_city + ".csv")
    df_concat.to_csv(save_path, index=False)

if __name__=="__main__":
    #pref_id = "11"
    #city_id = "1"
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pref_id", type=int, help="prefecture ID")
    parser.add_argument("-c", "--city_id", type=int, default=-1 ,help="city ID")

    args = parser.parse_args()
    if args.city_id == -1:
        i = 1
        while True:
            try:
                combine_data(str(args.pref_id), str(i))
                i+=1
            except:
                # print("error occured")
                break
    else:
        combine_data(str(args.pref_id), str(args.city_id))
