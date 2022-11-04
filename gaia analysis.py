# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:04:23 2022

@author: DK
"""

import pandas as pd

data_f = pd.read_csv(r'') # enter local file location
data_p = pd.read_csv(r'') # enter local file location
imp_f = pd.DataFrame(data_f, columns=['r_min','t_yrs'])
imp_p = pd.DataFrame(data_p, columns=['r_min','t_yrs'])

#Past Death Stars
name_p = []
parallax_p = []
rad_v_p = []
r_min_p = []
t_yrs_p = []
pm_p = []
phot_g =[]

for i in range(35):  
    if imp_p['t_yrs'][i] > 11.6*10**6 and imp_p['t_yrs'][i] < 15.6*10**6:
        name_p.append(data_p.iloc[i,0])
        parallax_p.append(data_p.iloc[i,3])
        pm_p.append(data_p.iloc[i,5])
        rad_v_p.append(data_p.iloc[i,12])
        r_min_p.append(data_p.iloc[i,14])
        t_yrs_p.append(data_p.iloc[i,15])
        phot_g.append(data_p.iloc[i,10])
    elif imp_p['t_yrs'][i] > 37.8*10**6 and imp_p['t_yrs'][i] < 41.8*10**6:
        name_p.append(data_p.iloc[i,0])
        parallax_p.append(data_p.iloc[i,3])
        pm_p.append(data_p.iloc[i,5])
        rad_v_p.append(data_p.iloc[i,12])
        r_min_p.append(data_p.iloc[i,14])
        t_yrs_p.append(data_p.iloc[i,15])
        phot_g.append(data_p.iloc[i,10])
    elif imp_p['t_yrs'][i] > 66*10**6 and imp_p['t_yrs'][i] < 70*10**6:
        name_p.append(data_p.iloc[i,0])
        parallax_p.append(data_p.iloc[i,3])
        pm_p.append(data_p.iloc[i,5])
        rad_v_p.append(data_p.iloc[i,12])
        r_min_p.append(data_p.iloc[i,14])
        t_yrs_p.append(data_p.iloc[i,15])
        phot_g.append(data_p.iloc[i,10])
    elif imp_p['t_yrs'][i] > 93.9*10**6 and imp_p['t_yrs'][i] < 97.9*10**6:
        name_p.append(data_p.iloc[i,0])
        parallax_p.append(data_p.iloc[i,3])
        pm_p.append(data_p.iloc[i,5])
        rad_v_p.append(data_p.iloc[i,12])
        r_min_p.append(data_p.iloc[i,14])
        t_yrs_p.append(data_p.iloc[i,15]) 
        phot_g.append(data_p.iloc[i,10])

print(name_p)
print('parallax',parallax_p)
print('rad v',rad_v_p)
print('rmin',r_min_p)
print('tyr',t_yrs_p)
print('pm',pm_p)
print('gmag',phot_g)
