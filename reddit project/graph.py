# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:43:58 2020

@author: truet
"""
import matplotlib.pyplot as plt

def plot_data(data):
    labels = 'Right Leaning', 'Left Leaning', 'Undetermined'
    sizes = data
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()