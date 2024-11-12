class Attacker:

#This class will be used to create an attacker object. The attacker object will be used in the game of Risk to attack a defender object
#The attacker object will have the following attributes:
#1. The number of attacking armies
#3. The number of attacking dice
#The attacker object will have the following methods:
#1. A method to roll the dice
#2. A method to calculate the number of armies lost by the attacker
#3. A method to determine the number of armies remaining for the attacker

#Author: Michael Curley
#Date: 24/10/2024
   

    def __init__(self, attacking_armies, attacking_dice):
        self.attacking_armies = attacking_armies
        self.attacking_dice = attacking_dice

    #Method used to generate an attacker armies dice numpy array. This array will be of size attacking armies and each armies will
    #be of attacking dice size.
    def roll_dice(self):
        #Import the required classes, random and numpy
        import random
        import numpy as np
        ## Generate a random dice roll x no of attacking dice times no of attacking armies
        attacking_dice_rolls = np.random.randint(1,7,(self.attacking_armies, self.attacking_dice))
        #Sort the dice rolls from hightest to lowest
        attacking_dice_rolls = np.sort(attacking_dice_rolls, axis=1)[:, ::-1]
        #Whittle down the array to just 2 columns 
        attacking_dice_rolls = attacking_dice_rolls[:, :self.attacking_dice -1]
        return attacking_dice_rolls 
    
    def calculate_attacker_armies_lost(self,attacking_armies, attacking_dice_rolls, defending_dice_rolls):
        import numpy as np
        armies_lost = 0
        # Loop through the dice rolls and compare the results
        for i in range(attacking_armies):
            for j in range(len(defending_dice_rolls[1])):
                if defending_dice_rolls[i, j] == attacking_dice_rolls[i, j]:
                    armies_lost += 1
                elif defending_dice_rolls[i, j] > attacking_dice_rolls[i, j]:
                    armies_lsot += 1
                else:
                    armies_lost += 1
            return armies_lost
    
        
    def armies_remaining_attacker(self, attacking_armies, attacking_armies_lost):
        return attacking_armies - attacking_armies_lost

    
    def __str__(self):
        return f"Attacker: {self.attacking_armies} armies, {self.attacking_dice} dice"