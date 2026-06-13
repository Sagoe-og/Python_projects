def adventure_game():
    bonus = "yes"
    while bonus == "yes":
        print("Welcome to the adventure game!")
        print("You just wake up in a dark room after being kidnapped.You can see a door to your left and a window to your right.")
        ans_1 = str(input("Do you want to go through the door or the window? (DOOR/WINDOW): "))
        ans_1 = ans_1.upper()
        print()
        if ans_1 == "DOOR":
            print("You open the door and find a long hallway. You can see a light at the end of the hallway.Before you make your decision, you feel a breeze from a vent above giving you another escape route.")
            print("Now you have three options...")
            ans_2 = str(input("Do you want to go down the hallway or stay in the room? (HALLWAY/ROOM/VENT): "))
            ans_2 = ans_2.upper()
            print()
            if ans_2 == "HALLWAY":
                print("You walk down the hallway and find a staircase leading up.")
                ans_3 = str(input("Do you want to go up the stairs or keep walking? (STAIRS/WALK): "))
                ans_3 = ans_3.upper()
                print()
                if ans_3 == "STAIRS":
                    print("You go up the stairs and find yourself back in the room. You are trapped!")
                elif ans_3 == "WALK":
                    print("You keep walking and find yourself in a dead end. You are trapped!")
                else:
                    print("Invalid input. Please try again.")
                    return  # this will exit the function if the input is invalid
            elif ans_2 == "ROOM":
                print("You stay in the room waiting for help but soon realize that no one is coming so you decide to go out anyway.Whiles trying to open the door, you find out its locked.")
                print("You find a key whiles panicking but also find a note that says 'The key is useless'.")
                ans_4 = str(input("Do you want to use the key or try to break the door? (KEY/BREAK): "))
                ans_4 = ans_4.upper()
                print()
                if ans_4 == "KEY":
                    print("You use the key but it doesn't work. You are still trapped!")
                elif ans_4 == "BREAK":
                    print("You break the door and the kidnappers hear the noise, They come and take you back to the room.")
                else:
                    print("Invalid input. Please try again.")
                    return  # this will exit the function if the input is invalid
            elif ans_2 == "VENT":
                print("You climb into the vent and find yourself in a dark room with no way out.")
                ans_5 = str(input("Do you want to try to find a way out or stay in the room? (FIND/STAY): "))
                ans_5 = ans_5.upper()
                print()
                if ans_5 == "FIND":
                    print("You try to find a way out but you are trapped!")
                elif ans_5 == "STAY":
                    print("You stay in the room waiting for help but soon realize that no one is coming so you decide to go out anyway.Whiles trying to open the door, you find out its locked.")
                    print("You find a key whiles panicking but also find a note that says 'The key is useless'.")
                    ans_6 = str(input("Do you want to use the key or try to break the door? (KEY/BREAK): "))
                    ans_6 = ans_6.upper()
                    print()
                    if ans_6 == "KEY":
                        print("You use the key but it doesn't work. You are still trapped!")
                    elif ans_6 == "BREAK":
                        print("You break the door and the kidnappers hear the noise, They come and take you back to the room.")
                    else:
                        print("Invalid input. Please try again.")
                        return
            else:
                print("Invalid input. Please try again.")
                return  # this will exit the function if the input is invalid
        elif ans_1 == "WINDOW":
            print("You open the window and find a fire escape ladder.")
            ans_5 = str(input("Do you want to climb down the ladder or stay in the room? (LADDER/ROOM): "))
            ans_5 = ans_5.upper()
            print()
            if ans_5 == "LADDER":
                print("You climb down the ladder and find yourself in a dark alley.")
                ans_6 = str(input("Do you want to go left or right? (LEFT/RIGHT): "))
                ans_6 = ans_6.upper()
                print()
                if ans_6 == "LEFT":
                    print("You go left and find yourself in a dead end. You are trapped!")
                elif ans_6 == "RIGHT":
                    print("You go right and find yourself on a busy street. Turns out they where all in on the plan to kidnap you.")
                    print("You are surrounded by kidnappers and they take you back to the room.")
                else:
                    print("Invalid input. Please try again.")
                    return  # this will exit the function if the input is invalid
            elif ans_5 == "ROOM":
                print("You stay in the room waiting for help but soon realize that no one is coming so you decide to go out anyway.Whiles trying to open the door, you find out its locked.")
                print("You find a key whiles panicking but also find a note that says 'The key is useless'.")
                ans_7 = str(input("Do you want to use the key or try to break the door? (KEY/BREAK): "))
                ans_7 = ans_7.upper()
                print()
                if ans_7 == "KEY":
                    print("You use the key but it doesn't work. You are still trapped!")
                elif ans_7 == "BREAK":
                    print("You break the door and the kidnappers hear the noise, They come and take you back to the room.")
                else:
                    print("Invalid input. Please try again.")
                    return  # this will exit the function if the input is invalid
            else:
                print("Invalid input. Please try again.")
                return      # this will exit the function if the input is invalid
        else:
            print("Invalid input. Please try again.")   
            return
        # If the user reaches this point, they are trapped in the simulation         
        print("It turns out you are in a simulation in which there is no chance of you escaping.The kidnappers are all in on it and they are all actors.")
        print("You are stuck in a never ending loop of being kidnapped and escaping.")
        print()
        print("Game Over!........Hope you get better options next time you play")    
        print()
        bonus = input("If you still belive you can escape, type 'YES' to play again or 'NO' to quit: ")
        bonus = bonus.upper()   
        if bonus == "NO":
            print("You are a coward and you will never escape.")
            print("Game Over!........Hope you get better options next time you play")
        else:
            print("Invalid input. Please try again.")
            return  # this will exit the function if the input is invalid

adventure_game()