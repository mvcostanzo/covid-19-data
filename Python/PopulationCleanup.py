# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:21:12 2020

@author: mvcostanzo
"""

import pandas as pd
import numpy as np
    
populationData = pd.read_csv('C:\\Michael_Docs\\Git Repositories\\NY Times COVID Data\\County Population Data.csv', encoding='latin1')
populationData['County Name'] = np.where(populationData["STNAME"] != 'Louisiana', populationData['CTYNAME'].replace(r" County", "", regex=True), populationData['CTYNAME'])
populationData['County Name'] = np.where(populationData["STNAME"] == 'Louisiana', populationData['CTYNAME'].replace(r" Parish", "", regex=True), populationData['County Name'])
populationData.to_csv('C:\\Michael_Docs\\Git Repositories\\NY Times COVID Data\\County Population Data (Modified).csv', index=False)