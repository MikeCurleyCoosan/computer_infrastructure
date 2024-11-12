class Menu:
#Author: Michael Curley
#Date: 24/10/2024
# This class will be used to display a menu to the user, and will run the appropriate code based on the user's choice
    

    def display_menu():
        print("\t Risk Game Menu")
        print("\t(a). Simulate a battle")
        print("\t(b). Simulate a war")
        print("\t(Q). Exit")

        choice = input("Type one letter (a,b or q):").strip().lower()
        return choice

    def simulate_battle():
       print("\t Create a battle simulation")
       from battle import Battle as battle
       battle()

    
    def simulate_war():
        pass

    def do_nothing():
        pass

    choice_map = {
        "a": simulate_battle,
        "b": simulate_war,
        "q": do_nothing
    }

    