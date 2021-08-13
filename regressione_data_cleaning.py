

import numpy as np
import pandas as pd
import math
import random
import copy
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 

df2 = pd.read_csv(r"C:\Users\angus\OneDrive\Desktop\FPL\complete_timeseries_dataset.csv") 
df = pd.read_csv(r"C:\Users\angus\OneDrive\Desktop\FPL\players_odds.csv") 

cols = list(df.columns)
cols[1] = 'Goal odds_30'
cols[2] = 'Ass odds_30'
cols[3] = 'CS odds_30' 
df.columns = cols


temp = df2[df2['name'] == 'Wood'][['1_minutes', '1_round']]

#problemi con la 34 giornata per rashford mane e ihenacho, robetrson e salah
d = {'Aguero': [3,[30,34,35,38]],
     'Antonio': [3,[30,34,35,36,37,38]],
     'Aubameyang': [2,[30,34,37,38]],  #add secondo 35
     'Bale': [2,[34]],
     'Bamford': [3, [30,31,32,33,34,35,36,37,38]],
     'Calvert-Lewin': [3,[30,33,34,35,36,37,38]], ###add 35x
     'Cancelo': [1,[31,34,35,36]],
     'Cavani': [3,[32,37]],   #add terza 35x
     'De Breuyne': [2, [30,38]],
     'Firmino': [3, [38]],
     'Foden': [2, [32,37,38]],
     'Grealish': [2, [37,38]],
     'Greenwood': [2, [37]],
     'Gündogan': [2,[31,32,36,37]],
     'Iheanacho': [3, [33,34,35,37,38]],  #add 35x
     'Ings': [3,[31,32,36,37,38]], #add 35x
     'Jesus': [3, [30,31,32,34,35,36]],
     'Jota': [2, [30,31,33,35]], #add 35x
     'Kane': [3, [30,31,34,35,36,37,38]],
     'Lacazette': [3, [30,31,32,34,35,37,38]],   #add 35x
     'Lingard': [2, [32,33,34,35,36,37,38]],
     'Mahrez': [2, [30,32,37,38]],
     'Mané': [2, [30,32,33,35,36,37,38]],
     'Martinez': [0, [30,31,32,33,34,35,36,37,38]] ,    #add 35x
     'Maupay': [3, [30,31,33,34,35]],
     'McCarthy': [0,[32,34,36,37]],
     'Raphinha': [2, [38]],
     'Rashford': [2,[30,31,32,33,35]],
     'Richarlisson': [3, [36]],
     'Robertson': [1, [30,31,32,33,35]],
     'Rodriguez': [2, [30,31,32,33,36]],
     'Son': [2,[30,31,32,34,35,36,37,38]],
     'Salah': [2, [30,31,33,35,36,37]], #add 35x
     'Trossard': [2, [30,31,32,33,34,35,36,37,38]],
     'Wilson': [3, [34, 35]],
     'Wood' : [3,[30,31,32,33,34,35,36,37,38] ]
     }   
    
cleaned = pd.DataFrame()
for pl in d:
    for gameweek in d[pl][1]:
        print(pl, gameweek)
        row = [np.nan for i in range(6)]
        row[0] = pl
        row[1] = d[pl][0]
        if gameweek != 38:
            row[2] = df2[(df2['name'] == pl) & (df2['1_round'] == gameweek)]['1_total_points'].reset_index(drop = True)[0]
        else:
            row[2] = df2[(df2['name'] == pl) & (df2['gameweek'] == gameweek)]['total_points'].reset_index(drop = True)[0]
        
    
        row[3] = 1 / df[(df['Player:'] == pl)]['Goal odds_' + str(gameweek)].reset_index(drop = True)[0]
        if np.isnan(row[3]):
            print(pl, gameweek, 'goal')
            row[3] = 0
        row[4] = 1 / df[(df['Player:'] == pl)]['Ass odds_' + str(gameweek)].reset_index(drop = True)[0]
        if np.isnan(row[4]):
            print(pl, gameweek, 'ass')
            row[4] = 0
        row[5] = 1 / df[(df['Player:'] == pl)]['CS odds_' + str(gameweek)].reset_index(drop = True)[0]
        if np.isnan(row[5]):
            print(pl, gameweek, 'CS')    
            row[5] = 0
            
        row = np.array(row).reshape(1, 6)
        row = pd.DataFrame(data = row)
        
        cleaned = pd.concat([cleaned, row])
        
        
cleaned.to_csv(r"C:\Users\angus\OneDrive\Desktop\FPL\per_regressione.csv")
