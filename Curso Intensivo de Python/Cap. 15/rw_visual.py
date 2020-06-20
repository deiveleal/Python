#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:25:12 2020

@author: deive
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Continua criando novos passeios enquanto o programa estiver ativo
while True:    
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.scatter(rw.x_values, rw.y_values, s=5)
    
    keep_running = input('Fazer outra caminhada? (s/n): ')
    if keep_running == 'n':
        break

