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
unite_id = 1
nb_automates = 10
automates_id = [i + 1 for i in range(nb_automates)]
# automates_type = [["0X0000BA20", "0X0000BA2F"][randint(0, 1)] for i in range(10)]

# GENERATOR
while True:
    for i in range(nb_automates):

        data = dict()
        data_automate = dict()

        data_automate["num_automate"] = automates_id[i]
        data_automate["type_automate"] = automates_type[i]
        data_automate["timestamp"] = time.strftime('new Date("%Y-%m-%dT%XZ")') # Mongo format : "2016-05-18>

        for j in range(len(df_rules)):
            if df_rules.iloc[j, 3] == 1:
                data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1], df_rules.iloc[j, 2])
            if df_rules.iloc[j, 3] == 0.1:
                data_automate[df_rules.iloc[j, 0]] = randint(df_rules.iloc[j, 1] * 10, df_rules.iloc[j, 2] * 10) / 10

        data[str(automates_id[i])] = data_automate

        file = str(data)
        file = file.replace("'new", 'new')
        file = file.replace(")', ", '), ')

        with open(f"/home/usine1_data/automate_{i+1}.json", 'w') as f:
            json.dump(file, f)

    time.sleep(60)
