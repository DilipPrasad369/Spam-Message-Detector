# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:52:06 2022

@author: HOME
"""

import pickle
file = open("model.pkl",'rb')
model = pickle.load(file)
file.close()

model

file = open("model2.pkl",'rb')
cv = pickle.load(file)
file.close()

cv
