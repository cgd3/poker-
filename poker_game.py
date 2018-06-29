#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:48:13 2018

@author: carolinedavis
""" 
import numpy as np

def poker_game():
## creating deck of cards
    values = ['2 of ', '3 of ', '4 of ', '5 of ', '6 of ', '7 of ', '8 of ', '9 of ', '10 of ', 'Jack of ', 'Queen of ', 'King of ', 'Ace of ']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = [value + suit for value in values for suit in suits]
    
## gives each card a value to compare   
    deck_value =  [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6 ,6 , 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12 ,12 , 13, 13 ,13 ,13]
    card_dictionary = dict(zip(deck, deck_value))
        
## user input, inputs number of players and names for each 
    number_of_players = int(input('Enter number of players:'))
    names = []
    for i in range(number_of_players):
        name = input('Enter player name:')
        names.append(name)
                
## deal 5 random cards to each player   
    hands = []
    for i in range(0, number_of_players):
        hands.append([])
        for j in range(0,5):
            hands[i].append(np.random.choice(deck, replace = False))
        print ("Player " + str(i + 1) + "'s hand:")
        print(hands[i][:]) 
##find winning card print winner  

poker_game()