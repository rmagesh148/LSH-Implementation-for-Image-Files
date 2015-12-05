# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:29:56 2015

@author: MaGesh
"""
import numpy as np
from scipy.ndimage import imread
from lshash import LSHash
lsh=LSHash(20,32*32) #32*32 is the dimension with 20 hash buckets
resultSet=[]
for i in range(1,100001):
    print i;
    X="F:\\Fall 2015\\Data Mining\\Programming Assignments\\PA5\\data\\dataset\\"+str(i)+".bmp"
    im=imread(X,flatten=True)
    single_array=im.flatten()
    lsh.index(single_array)#hashing the each values in to the bucket
for i in range(1,11):
    print i,"for querying"    
    X1="F:\\Fall 2015\\Data Mining\\Programming Assignments\\PA5\\data\\Query\\"+str(i)+".bmp"
    imQ=imread(X1,flatten=True) #converting to grey scale
    imFlatten=imQ.flatten()
    value=lsh.query(imFlatten,distance_func="euclidean") #querying the nearest points
    resultSet.append(value)