class Runner:

    from menu import Menu as m

    choice = m.display_menu()

    while choice != "q": 
        #If the user's choice is in the choice_map dictionary, call the function associated with the user's choice
        if choice in m.choice_map: 
            m.choice_map[choice]() 
        else:
            print("Please select either a,b,q") #If the user's choice is not in the choice_map dictionary, print an error message
        choice = m.display_menu()

