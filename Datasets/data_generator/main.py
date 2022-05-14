"""
DATA GENERATOR
Author : Kyllian BEGUIN
Objective :
- Generate data to simulate automaton data from one of the five unites of COOP'MILK
"""
# IMPORT AREA
import pandas as pd
from random import randint
import time
import json

# LOADING AREA
df_rules = pd.read_csv("rules_coopmilk.csv", sep=";")
with open("automates_type", "r") as f:
    automates_type = json.load(f)

# INITIATING VARIABLES
usine_ids = [1,2,3,4,5]
nb_automates = 10
automates_id = [i + 1 for i in range(nb_automates)]
# automates_type = [["0X0000BA20", "0X0000BA2F"][randint(0, 1)] for i in range(10)]
col = ["usine_id", "numero_automate", "type_automate" , "datetime"] + list(df_rules.iloc[0:,0])
# df_coopmilk = pd.DataFrame(columns=col)
# nb_days = 365
# time_range = pd.date_range(start='1/1/2021', end='31/12/2021', freq="1min")
# time_range_len = len(time_range)



# GENERATOR JSON
while True:
    for i in range(nb_automates):

        data = dict()
        data_automate = dict()

        data_automate["num_automate"] = automates_id[i]
        data_automate["type_automate"] = automates_type[i]
        data_automate["timestamp"] = time.strftime('new Date("%Y-%m-%dT%XZ")') # Mongo format : "2016-05-18T16:00:00Z"

        for j in range(len(df_rules)):
            if df_rules.iloc[j, 3] == 1:
                data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1], df_rules.iloc[j, 2])
            if df_rules.iloc[j, 3] == 0.1:
                data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1] * 10, df_rules.iloc[j, 2] * 10) / 10

        data[str(automates_id[i])] = data_automate

        file = str(data)
        file = file.replace("'new", 'new')
        file = file.replace(")', ", '), ')

        with open(f"automate_{i+1}.json", 'w') as f:
            json.dump(file, f)

    time.sleep(60)
    
    # GENERATOR BIG CSV
# for t in range(time_range_len):
#     print(time_range[t].strftime("%Y-%m-%d %X"))
#     for k in range(len(usine_ids)):
#         for i in range(nb_automates):
# 
#             data = dict()
#             data_automate = dict()
# 
#             data_automate["usine_id"] = usine_ids[k]
#             data_automate["numero_automate"] = automates_id[i]
#             data_automate["type_automate"] = automates_type[i]
#             data_automate["datetime"] = time_range[t].strftime("%Y-%m-%d %X")
# 
#             for j in range(len(df_rules)):
#                 if df_rules.iloc[j, 3] == 1:
#                     data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1], df_rules.iloc[j, 2])
#                 if df_rules.iloc[j, 3] == 0.1:
#                     data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1] * 10, df_rules.iloc[j, 2] * 10) / 10
# 
#             # print(data_automate)
#             # test = pd.DataFrame(data_automate, index = [len(df_coopmilk)])
#             df_coopmilk = pd.concat([df_coopmilk, pd.DataFrame(data_automate, index = [len(df_coopmilk)])], ignore_index=True)
# 
#     # print(round((k / time_range_len) * 100, 5))
# df_coopmilk.to_csv("grafana_database.csv", index=False)
