class Battle:
    #import required classes
    from attacker import Attacker as attacker
    from defender import Defender as defender
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #Request army and dice information from user
    attack_armies = int(input("\t Please enter the number of attacking armies "))
    attack_dice = int(input("\t Please enter the number of attacking dice "))
    defence_armies = int(input("\t Please enter the number of defending armies "))
    defence_dice = int(input("\t Please enter the number of defending dice "))
   
    #Battles will take the least number of armies put forward by either attack or defence
    if attack_armies < defence_armies:
        defence_armies = attack_armies
    else:
        attack_armies = defence_armies

    #Create an instance of an offence
    offence = attacker(attack_armies, attack_dice)
    #Create an instance of an defence
    defender = defender(defence_armies, defence_dice)

    #Roll the dice for the offence. This will create an numpy array to store the dice rolls for the attack
    offence_dice = offence.roll_dice()
    #Roll the dice for the defence. This will create an numpy array to store the dice rolls for the attack
    defence_dice = defender.roll_dice()

    #offence_armies_lost = offence.calculate_attacker_armies_lost(offence_dice, defence_dice)
    #print(offence_armies_lost)

    #Testing purposes
    #print("The attacking army dice rolls are ")
    #print(offence_dice)
    #print("The defending army dice rolls are ")
    #print(defence_dice)

    
    # Create a new matrix to store the results of the battles
    results = np.zeros((attack_armies, len(defence_dice[1])))

    # Loop through the dice rolls and compare the results
    for i in range(attack_armies):
       for j in range(len(defence_dice[1])):
            if defence_dice[i, j] == offence_dice[i, j]:
               results[i, 1] += 1
            elif defence_dice[i, j] > offence_dice[i, j]:
                results[i, 1] += 1
            else:
               results[i, 0] += 1

    #Print the results of the battle 
    #print(results)

    #Convert the results from a numpy float array to an integer array

    results = results.astype(int)
    results

    # Create a pandas dataframe to store the results

    df = pd.DataFrame(results, columns=['Attacker Wins', 'Defender Wins'])
    print(df)


    # Percentage of wins for the 
    attacker_percentage = 0
    for i in range (attack_armies):
        if df['Attacker Wins'][i] == 2:
            attacker_percentage += 1/(attack_armies)
    print(attacker_percentage)


    # Percentage of wins for the defender   
    defender_percentage = 0
    for i in range (attack_armies):
        if df['Defender Wins'][i] == 2:
            defender_percentage += 1/(attack_armies)
    print(defender_percentage)

    # Draw percentage
    draw_percentage = 1 - attacker_percentage - defender_percentage
    print(draw_percentage)

    # Double check the percentages
    draw_percentage_check=0
    for i in range (attack_armies):
        if df['Attacker Wins'][i] == 1 and df['Defender Wins'][i] == 1:
            draw_percentage_check += 1/(attack_armies)

    print(draw_percentage_check)

    attacker_armies_lost = offence.calculate_attacker_armies_lost(attack_armies, offence_dice, defence_dice)
    print(attacker_armies_lost)
   