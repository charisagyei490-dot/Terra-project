print("WORLD OF IMAGINATION")
print("A world where your imagination comes to life.")

player_name = input("What is your name, dreamer? ")

print("Welcome, " + player_name + "!")
print("Your adventure is about to begin.")
print("Choose a place to explore:")
print("1. Dream Ocean")
print("2. Enchanted Forest")
print("3. Starlight Village")
print("And there are 10 locked worlds to unlock!")
print("Rule: Gather Resources in the 3 free towns to earn XP.")
print("Every 10 Xp levels you up, helping you unlock the 5 locked towns!")

choice = input("Where would you like to go? Enter 1, 2, or 3: ")

if choice == "1":
    print("Welcome To Dream Ocean!")
    print("A town With Endless Responsibilities")
    print("Explore Around!")
    print("Find Resourses to unlock the other towns")

elif choice == "2":
    print("Welcome to Enchanted Forest!")
    print("You have entered a magical forest!")
    print("Have Fun and remeber to Search for hidden treasures")
    print("Meet Magical creatures")
    print("Find a secret path")
    
elif choice == "3":
    print("\nWelcome to Starlight Village!")
    print("Glowing crystals floats in the night air, lightening up hidden pathways")
    print("Your search for rare celestial resources begins here")
    print("Legends says a secret map to Dragonrider Town is hidden nearby!")
    
elif choice == "4":
    print("\nCloud Kingdom (LOCKED)")
    print("How to unlock Cloud kingdom:")
    print("These are things you need to do to unlock this town:")
    print("Complete 5 missions")
    print("Collect the required coins")
    print("Reach level 10")
    print("Find 3 treasures")
    print("The Cloud Will Be Waiting For Your Return Until Our Next Adventure!")

    action = input("\nDO you want to search for these items now? (Yes/No):")
    if action == "Yes":
        print("You set off on a quest to gather resource!")
        print("\nYou have sevreal worlds to explore.")
        print("Each world holds different resources.")
        print("Choose where you want to begin search.")

        print("\nAVAILABLE WORLDS:")
        print("1. Dream Ocean")
        print("2. Enchanted Forest")
        print("3. Starlight Village")

        world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3:")

        if world == "1":
            print("\nWelcome back to Dream Ocean!")
            print("Your search for resources begins here")
            print("Your journey to unlock Dream Ocean has begun")

        elif world == "2":
              print("\nWelcome back to Enchanted Village!")
              print("Your search for resource begins here")
              print("Your journey to unlock Enchnated village has begun")

        elif world == "3":
              print("\nWelcome back to Starlight Village!")
              print("Your search for resource begins here")
              print("Your journey to unlock Starlight Village has begun")

    else:
        print("You returned to the main menu")

elif choice == "5": 
    print("\nCrystal Caves (LOCKED)")
    print("How to Unlock Crystal caves:")
    print("These are things you need to do to unlock this town:")
    print("Unlock Cloud Kingdom First")
    print("Collect 500 Coins")
    print("Find the Magical tree")
    print("Reach Level 15")
    print("Your Adventure Awaits Cant Wait TO See You Soon Dreamer!")

    action = input("\nDO you want to search for these items now? (Yes/No):")
    if action == "Yes":
        print("You set off on a quest to gather resource!")
        print("\nYou have several worlds to explore.")
        print("Each world holds different resources.")
        print("Choose where you want to begin your search.")

        print("\nAVAILABLE WORLDS:")
        print("1. Dream Ocean")
        print("2. Enchnated Forest")
        print("3. Starlight Village")
        print("4. Cloud Kingdom")

        world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3:")    

        if world == "1":
            print("\nWelcome back to Dream Ocean!")
            print("Your search for resources begins here.")
            print("Your journey to Unlock Dream Ocean has begun!")

        elif world == "2":
              print("\nWelcome back to Enhanted Forest")
              print("Your search for resources begins here.")
              print("Your journey to Unlock Dream Ocean has begun!")

        elif world == "3":
              print("\nWeclome back to Starlight Village")
              print("Your search for resources begins here.")
              print("Your journey to Unlock Dream Ocean has begun!")

        elif world == "4":
             print("\nWelcome back to Cloud Kingdom!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dream Ocean has begun!")

    else:
        print("You returned to the main menu")


elif choice == "6":
    print("\nMoonlight Mountains (LOCKED)")
    print("How to unlock Moonlight Mountains:")
    print("There are things you need to do to unlcok this town:")
    print("Unlock Crystal Caves First")
    print("Collect 700 coins")
    print("Reach Level 20")
    print("Find 5 hidden starts from Starlight Village")
    print("The Mountains Are Calling. Your Next Adventure Awaits! Cant wait to see you soon Dreamer!")

    action = input("\nDO you want to search for these items now? (Yes?No):")
    if action == "Yes":
        print("You set off on a quest to gather resource!")
        print("\nYou have several worlds to explore")
        print("Each world holds different resources")
        print("Choose where you want to begin your search")

        print("AVAILABLE WORLDS:")
        print("You returned to the main menu")
        print("1. Dream Ocean")
        print("2. Enchnated Forest")
        print("3. Starlight Village")
        print("4. Cloud Kingdom")
        print("5. Crystal Caves")

        World: str = input("\nWhich World would you like to explore? Enter 1, 2, 3:")

        if World == "1":
            print("\nWelcome back to Dream Ocean!")
            print("Your search for resource begins here.")
            print("Your journey to unlock Moonlight Mountain has begun")
      
        elif World == "2":
              print("\nWelcome back to Enchanted Forest!")
              print("Your search for resource begins here.")
              print("Your journey to unlock Moonlight Mountain has begun")

        elif World == "3":
              print("\nWelcome back to Starlight village")
              print("Your search for resource begins here")
              print("Your journey to unlock Moonlight Mountain has begun!") 

        elif World == "4":
             print("\nWelcome back to Cloud Kingdom!")
             print("Your search for resources begins here.")
             print("Your journey to unlock Moonlight Mountain has begun!") 

        elif World == "5":
             print("\nWelcome back to Crystal Cave!")
             print("Your search for resource begins here.")
             print("Your journey to unlock Moonlight Mountain has begun!")

    else: 
        print("You returned to the main menu")

elif choice == "7":
    print("\nTown of Darkness (LOCKED)")
    print("How to unlock Town of Darkness:")
    print("There are things you need to do to unlock this town:")
    print("Unlock Moonlight Mountains First")
    print("Collect 3,000 coins")
    print("Complete 20 missions in previously unlock town")
    print("Discover 10 hidden treasures")
    print("Reach Level 35")
    print("The secrets of this town remian hidden for now. We look forward to welcoming you when you're ready!")

    action= input("\nDo you want to search for these items now? (Yes/No):")
    if action == "Yes":
        print("You set off on a quest to gather resource!")
        print("\nYou have several worlds to explore.")
        print("Each world holds different resources.")
        print("Choose where you want to begin your search.")

        print("\nAVAILABLE WORLDS:")
        print("1. Dream ocean")
        print("2. Enchnated Forest")
        print("3. Starlight Village")
        print("4. Cloud Kingdom")
        print("5. Crystal Caves")
        print("6. Moonlight Mountains")

        world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3:")

        if world == "1":
            print("\nWelcome back to Dream Ocean!")
            print("Your search for resources begins here.")
            print("Your journey to unlock Town of Darkness has begun!")

        elif world == "2":
              print("\nWelcome back to Enchnated Forest!")
              print("Your search for resource begins here.")
              print("Your journey to unlock Town of Darkness has begun!")

        elif world == "3":
              print("\nWelcome back to starligt village!")
              print("Your search for resource begins here.")
              print("Your journey to unlock Town of Darkness has begun!")

        elif world == "4":
             print("\nWelcome back to Cloud Kingdom!")
             print("Your search for resources begins here.")
             print("Your journey to unlock Town of Darkness has begun!")

        elif world == "5":
             print("\nWelcome back to Crystal Cave!")
             print("Your search for resource begins here.")
             print("Your journey to unlock Town of Darkness has begun!")

        elif world == "6":
             print("\nWelcome back to Moonlight Mountain!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Echoes Of Mind has begun!")
     
    else:
        print("You returned to the main menu")  

elif choice == "8":
     print("\nEchoes of Mind (Locked)")
     print("How to unclock Echoes of Mind")
     print("There are things you need to do, to unlock this town")
     print("Unlock Town Of Darkness first")
     print("Collect 7,500 coins")
     print("Complete 35 missions.")
     print("Find All Special Hidden Objects")
     print("Reach Level 50")
     print("The secrets of this town remian hidden for now. We look forward to welcoming you when you're ready!")

     action = input("\nDo you want to search for these items now? (Yes/No):")

     if action == "Yes":
          print("You set off on a quest to gather resource!")
          print("\nYou have several worlds to explore.")
          print("Each world holds different resources.")
          print("Choose where you want to begin your search.")

          print("\nAVAILABLE WORLDS:")
          print("1. Dream Ocean")
          print("2. Enchanted Forest")
          print("3. Starlight Village")
          print("4. Cloud Kingdom")
          print("5. Crystal Caves")
          print("6. Moonlight Mountains")
          print("7. Town Of Darkness")

          world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3, 4, 5, 6, 7:")

          if world == "1":
               print("\nWelcome back to Dream Ocean!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "2":
               print("\nWelcome back to Enchanted Forest!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "3":
               print("\nWelcome back to Starlight Village!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "4":
               print("\nWelcome back to Cloud Kingdom!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "5":
               print("\nWelcome back to Crystal Cave!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "6":
               print("\nWelcome back to Moonlight Mountain!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

          elif world == "7":
               print("\nWelcome back to Town of Darkness!")
               print("Your search for resources begins here.")
               print("Your journey to Unlock Echoes Of Mind has begun!")

     else:
          print("You returned to the main menu")

elif choice == "9":
    print("\nDragonrider Town (LOCKED)")
    print("How to unlock Dragonrider town")
    print("There are things you need to do to unlock this town!")
    print("Unlock Echoed Of Mind first")
    print("Collect 15,000 coins")
    print("Complete 50 missions.")
    print("Find All Special Hidden Objects")
    print("Reach Level 100")
    print("The secrets of this town remian hidden for now. We look forward to welcoming you when you're ready!")

    action = input("\nDo you want to search for these items now? (Yes/No):")

    if action == "Yes":
        print("You set off on a quest to gather resource!")
        print("\nYou have several worlds to explore.")
        print("Each world holds different resources.")
        print("Choose where you want to begin your search.")

        print("\nAVAILABLE WORLDS:")
        print("1. Dream Ocean")
        print("2. Enchanted Forest")
        print("3. Starlight Village")
        print("4. Cloud Kingdom")
        print("5. Crystal Caves")
        print("6. Moonlight Mountains")
        print("7. Town of Darkness")
        print("8. Echoes Of Mind")

        world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3:")    

        if world == "1":
            print("\nWelcome back to Dream Ocean!")
            print("Your search for resources begins here.")
            print("Your journey to Unlock Dragonrider Town has begun!")

        elif world == "2":
              print("\nWelcome back to Enchnated Forest!")
              print("Your search for resources begins here.")
              print("Your journey to Unlock Dragonrider Town has begun!")

        elif world == "3":
              print("\nWelcome back to starlight village!")
              print("Your search for resources begins here.")
              print("Your journey to Unlock Dragonrider Town has begun!")

        elif world == "4":
             print("\nWelcome back to Cloud Kingdom!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dragonrider Town has begun!")

        elif world == "5":
             print("\nWelcome back to Crystal Cave!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dragonrider Town begun!")

        elif world == "6":
             print("\nWelcome back to Moonlight Mountain!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dragonrider Town begun!")

        elif world == "7":
             print("\nWelcome back to Town of Darkness!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dragonrider Town begun!")

        elif world == "8":
             print("\nWelcome back to Echoes Of Mind!")
             print("Your search for resources begins here.")
             print("Your journey to Unlock Dragonrider Town begun!")

    else:    
        print("You returned to the main menu")

elif choice == "10":
     print("\nRealm of the Celestials (Locked)")
     print("How to unlock Realm of the celestials")
     print("There are things you need to do to unlock this legendary realm!")
     print("Unlock Dragonrider Town first")
     print("Collect 50,000 coins")
     print("Complete 100 missions.")
     print("Find All Special Hidden Objects")
     print("Reach Level 150")
     print("The secrets of this town remian hidden for now. We look forward to welcoming you when you're ready!")


     action = input("\nDo you want to search for these items now? (Yes/No):")

     if action == "Yes":
          print("You set off on a quest to gather resource!")
          print("\nYou have several worlds to explore.")
          print("Each world holds different resources.")
          print("Choose where you want to begin your search.")

          print("\nAVAILABLE WORLDS:")
          print("1. Dream Ocean")
          print("2. Enchanted Forest")
          print("3. Starlight Village")
          print("4. Cloud kindom")
          print("5. Crystal Kingdom")
          print("6. Moonlight Mountains")
          print("7. Town of Darkness")
          print("8. Echoes of Mind")
          print("9. Dragonrider Town")

          world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3:")

          if world == "1":
               print("\nWelcome back to Dream Ocean!")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "2":
               print("\nWelcome back to Enchnated Forest!")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "3":
               print("\nWelcome back to starlight village!")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "4":
               print("\nWelcome back to cloud kingdom!")
               print("Your search for resources begins here")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "5":
               print("\nWelcome back to crystal cave")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "6":
               print("\nWelcome back to Moonlight Mountain!")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "7":
               print("\nWelcome back to Town of Darkness!")
               print("Your search for resources begins here.")
               print("Your journey to Realm Of Celestials has begun!")

          elif world == "8":
               print("\nWelcome back to Echoes of Mind!")
               print("Your search for resources begins here.")
               print("Your journey to Realm of Celestials has begun!")

          elif world == "9":
               print("\nWelcome back to Dragonrider town!")
               print("Your search for resources begins here.")
               print("Your journey to unlock Realm Of Celestials has begun!")

     else:
        print("You returned to the main menu")

elif choice == "11":
     print("\nThe Subconscious Core (Locked)")
     print("How to unlock The Subconscious core")
     print("There are things you need to do to unlock the ultimate realm of pure thugh!")
     print("Unlock Realm Of The Calestial first")
     print("Collect 100,000 coins")
     print("Complete 200 missions.")
     print("Find All Special Hidden Objects")
     print("Reach Level 200") 
     print("Complete A Final Adventure!")
     print("You've reach the end of this journey, but memories of your adventure will stay with you. Until we meet again!")

     action = input("\nDO you want to search for these items now? (Yes/No)")

     if action == "Yes":
          print("You set off on a quest to gather resource!")
          print("\nYou have several worlds to explore")
          print("Each world holds different resources.")
          print("Choose where you want to begin your search.")

          print("\nAVAILABLE WORLDS:")
          print("1. Dream Ocean")
          print("2. Enchanted Forest")
          print("3. Starlight Village")
          print("4. Cloud kindom")
          print("5. Crystal Kingdom")
          print("6. Moonlight Mountains")
          print("7. Town of Darkness")
          print("8. Echoes of Mind")
          print("9. Dragonrider Town")
          print("10. Realm Of The Celestials")

          world: str = input("\nWhich world would you like to explore? Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:")

          if world == "1":
               print("\nWelcome back to Dream Ocean!")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "2":
               print("\nWelcome back to Enchanted Forest")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "3":
               print("\nWelcome back to starlight village!")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")
          
          elif world == "4":
               print("\nWelcome back to cloud kingdom!")
               print("Your search for resources begins here")
               print("Your journey to The Subconscious core has begun!")

          elif world == "5":
               print("\nWelcome back to crystal cave")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "6":
               print("\nWelcome back to Moonlight Mountain!")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "7":
               print("\nWelcome back to Town of Darkness!")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "8":
               print("\nWelcome back to Echoes of Mind!")
               print("Your search for resources begins here.")
               print("Your journey to The Subconscious core has begun!")

          elif world == "9":
                print("\nWelcome back to Dragonrider town!")
                print("Your search for resources begins here.")
                print("Your journey to The Subconscious core has begun!")

          elif world == "10":
               print("\nWelcome back to Realm of Celestials")
               print("Your search for resources begins here.")
               print("Your journey to THe Subconscious core has begun")

else:
     print("You returned to the main menu")
          
               
               

