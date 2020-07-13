# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:02:06 2020

@author: mvcostanzo
"""

import pandas as pd

covidData = pd.read_csv('C:\\Michael_Docs\\Git Repositories\\NY Times COVID Data\\us-counties.csv')
NYCcovidData = pd.read_csv('C:\\Michael_Docs\\Git Repositories\\NY Times COVID Data\\NYC COVID Details\\boro\\boroughs-case-hosp-death.csv')

#Drop the NYC aggregate from the NYT data
covidData.drop(covidData.loc[covidData['county']=='New York City'].index, inplace=True)

#Loop through the NYC Covid Data and Convert the Boroughs to Counties and add to overall COVID Data
NYC_DataFrame = pd.DataFrame(columns = ['date', 'county', 'state', 'fips', 'cases', 'deaths'])
bronx_cases = 0
bronx_deaths = 0 
manhattan_cases = 0
manhattan_deaths = 0
queens_cases = 0
queens_deaths = 0
staten_island_cases = 0
staten_island_deaths = 0
brooklyn_cases = 0
brooklyn_deaths = 0 
for rowindex, row in NYCcovidData.iterrows():
        bronx_cases = bronx_cases + row['BX_CASE_COUNT']
        bronx_deaths = bronx_deaths + row['BX_DEATH_COUNT']
        manhattan_cases = manhattan_cases + row['MN_CASE_COUNT']
        manhattan_deaths = manhattan_deaths + row['MN_DEATH_COUNT']
        brooklyn_cases = brooklyn_cases + row['BK_CASE_COUNT']
        brooklyn_deaths = brooklyn_deaths + row['BK_DEATH_COUNT']
        queens_cases = queens_cases + row['QN_CASE_COUNT']
        queens_deaths = queens_deaths + row['QN_DEATH_COUNT']
        staten_island_cases = staten_island_cases + row['SI_CASE_COUNT']
        staten_island_deaths = staten_island_deaths + row['SI_DEATH_COUNT']
        
        NYC_DataFrame = NYC_DataFrame.append({'date': row['DATE_OF_INTEREST'], 'county': 'New York', 'state': 'New York', 'fips': 36061, 
                              'cases': manhattan_cases , 'deaths': manhattan_deaths}, ignore_index=True)
        NYC_DataFrame = NYC_DataFrame.append({'date': row['DATE_OF_INTEREST'], 'county': 'Bronx', 'state': 'New York', 'fips': 36005, 
                              'cases': bronx_cases , 'deaths': bronx_deaths }, ignore_index=True)
        NYC_DataFrame = NYC_DataFrame.append({'date': row['DATE_OF_INTEREST'], 'county': 'Kings', 'state': 'New York', 'fips': 36047, 
                              'cases': brooklyn_cases, 'deaths': brooklyn_deaths }, ignore_index=True)
        NYC_DataFrame = NYC_DataFrame.append({'date': row['DATE_OF_INTEREST'], 'county': 'Queens', 'state': 'New York', 'fips': 36081, 
                              'cases': queens_cases, 'deaths': queens_deaths }, ignore_index=True)
        NYC_DataFrame = NYC_DataFrame.append({'date': row['DATE_OF_INTEREST'], 'county': 'Richmond', 'state': 'New York', 'fips': 36085, 
                              'cases': staten_island_cases , 'deaths': staten_island_deaths}, ignore_index=True)
        
#Write the NYC Data to the folder for appending in a Tableau Union
NYC_DataFrame.to_csv('C:\\Michael_Docs\\Git Repositories\\NY Times COVID Data\\NYC-counties.csv', index=False)
    