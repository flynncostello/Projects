import random
import math
import math_questions
import race_art #trophy, lucky_lane, ghost_gorge, volcano_valley

def play_race_mania():

    # Total points earned
    total_points = 0
    ending_info = []

    # Main menu for race game
    while True:
    
        print("""
        **************************************************************
        *  Welcome to Race Mania, the best math racing game of 2020. *
        *                                                            *
        *  Enter 1 to continue                                       *
        *  Enter 2 to quit                                           *
        *                                                            *
        * (for ages 10 - 15)                                         *
        **************************************************************
        """)
        while True:
            try:
                main_menu_choice = int(input("> "))
                if main_menu_choice != 1 and main_menu_choice != 2:
                    print("Invalid Input")
                    print()
                    continue
                break
            except ValueError:
                print("Invalid Input")
                print()
                continue

        # Player has chosen to continue
        if main_menu_choice == 2:
            break

        elif main_menu_choice == 1:
        
            print("""
        Before we begin could you please fill out the following information.
        
        1) What is your name?
        """)
            race_name = input("> ")


            print("""
        2) How old are you?
        """) # age used for difficulty of questions
            while True:
                try:
                    race_age = int(input("> "))
                    break
                except ValueError:
                    print("Invalid input")
                    print()
                    continue

            # Checking if race age is between required ages
            if race_age < 10 or race_age > 15:
                print("Invalid age, you must be between 10 and 15. Returning to home menu.")
                print()
                continue
        
            # Area of math applies for all race tracks in this play of game (if player returns to main menu this will have to be re done)
            print("""
        3) What area of maths would you like to focus on (enter corresponding letter):
            a) Basic arithmatics (i.e. addition, subtraction, multiplication, division)
            b) Measurement (i.e. perimeter, area, unit conversion)
        """)

            while True:
                # Area of math
                race_math_area = input("> ")

                if race_math_area.lower() != "a" and race_math_area.lower() != "b" and race_math_area.lower() != "c":
                    print("Invalid input, try again.")
                    print()
                    continue
                break

            print("""
        4) What would you like to set the AI difficulty to? (1, 2 or 3)
        
        Note: Harder AI difficulty will be rewarded with more points""")
            print()

        
            while True:
                try:
                    ai_dif = int(input("> "))
                    if ai_dif != 1 and ai_dif != 2 and ai_dif != 3:
                        print("Invalid Input")
                        print()
                        continue
                    break
                except ValueError:
                    print("Invalid Input")
                    print()
                    continue



            print("""
        Exellent, now travelling to the first track...
        ************************************************""")

        # Question that is asked during race
        def race_questions(race_age):
            if race_age <= 12:
                number_range1 = random.randint(1, 12)
                number_range2 = random.randint(1, 12)
            else:
                number_range1 = random.randint(1, 24)
                number_range2 = random.randint(1, 24)

            if race_math_area.lower() == "a":
                num1 = number_range1
                num2 = number_range2
                basic_q = math_questions.basic_math_skills(num1, num2) # Setting basic_q = True or False
                
                return basic_q
            
            elif race_math_area.lower() == "b":
                m_length1 = number_range1
                m_length2 = number_range2
                measure_q = math_questions.measurement(m_length1, m_length2) # setting measure_q = True or False

                return measure_q


        # Race
        # definign how track works for all tracks
        def tracks (track_distance, track_welcome, ai_difficulty):

            # printing track welcome
            print(track_welcome)

            correct_answers = 0
            incorrect_answers = 0

            player_distance = 0
            player_multiplier = 1.0
            player_place = 0

            ai1_distance = 0.0

            while True:            

                # input to start ll race
                start_track = input("> ")

                # player wants to start
                if start_track == "1":
                    print("""
        Racer ready.
        3
        2
        1
        GO!""") 
                    

                    print()
                    question = race_questions(race_age)
                    
                    while True:
                        # Answer is correct
                        if question[0]:
                            correct_answers += 1
                            increased_distace = 200 * player_multiplier # 200
                            print("Correct, +{} distance!".format(increased_distace))

                            player_distance += (increased_distace)
                            ai1_distance += (ai_difficulty * random.randint(150, 300))

                            if player_multiplier < 5:
                                player_multiplier += 1

                            if player_distance > ai1_distance:
                                player_place = "1st"
                            elif player_distance < ai1_distance:
                                player_place = "2nd"
                            break
                
                        ai1_distance += (ai_difficulty * random.randint(150, 300))

                        if player_distance > ai1_distance:
                            player_place = "1st"
                        elif player_distance < ai1_distance:
                            player_place = "2nd"

                        # Answer is incorrect
                        print("Incorrect, +0 distance!")
                        print(f"Correct answer = {question[1]}")
                        player_multiplier = 1
                        incorrect_answers += 1
                        break

                    # During the race
                    while player_distance < track_distance and ai1_distance < track_distance:

                        print()
                        track_choice = input("> ")

                        # Player wants  next q
                        if track_choice.lower() == "next":
                            print()

                            # Younger player = easier q's
                        
                                    
                            question = race_questions(race_age)

                            # Answer is correct
                            if question[0]:
                                correct_answers += 1
                                increased_distace = 200 * player_multiplier # 200
                                print("Correct, +{} distance!".format(increased_distace))

                                player_distance += (increased_distace)
                                ai1_distance += (ai_difficulty * random.randint(150, 300))

                                if player_multiplier < 5:
                                    player_multiplier += 1

                                if player_distance > ai1_distance:
                                    player_place = "1st"
                                elif player_distance < ai1_distance:
                                    player_place = "2nd"
                                continue
                    
                            ai1_distance += (ai_difficulty * random.randint(150, 300))

                            if player_distance > ai1_distance:
                                player_place = "1st"
                            elif player_distance < ai1_distance:
                                player_place = "2nd"

                            # Answer is incorrect
                            incorrect_answers += 1
                            print("Incorrect, +0 distance!")
                            print(f"Correct answer = {question[1]}")
                            player_multiplier = 1
                            continue

                        



                        elif track_choice.lower() == "info":
                            distance_from_finish = track_distance - player_distance
                            info = ("""
        Current Place = {}
        Current Distance = {}
        Distance From Finish = {}
        Player Multiplier = {}
        AI Distance = {}""").format(player_place, player_distance, distance_from_finish, player_multiplier, ai1_distance)
                            print(info)
                            continue

                        else:
                            print("Invalid input, try again.")
                            continue

                    def finish_text (place, track): # track uses track distance to determine which track it is
                        if track == 10000:
                            string = ("""
        Race Complete!
        You finished {}
        *********************************
        """.format(place))
                            return string
                        
                        string = ("""
        Race Complete!
        You finished {}
                    
        Now travelling to the next tack...
        **********************************
        """.format(place))
                        return string

                    
                    print(finish_text(player_place, track_distance))

                    if player_place == "1st":
                        race_end = [True, 1, correct_answers, incorrect_answers]
                    else:
                        race_end = [True, 0, correct_answers, incorrect_answers]
                    return race_end # This means that the race is done

                elif start_track == "2":
                    # return to main menu 
                    print("Now returning to main menu...")
                    if player_place == "1st":
                        return [False, 1] # returns false from the function is player wants to return to home sceen
                    return [False, 0]

                else:
                    print("Invalid input try again.")
                    print()
                    continue

        # Function for all tracks info
        def track_welcome (track_name, distance, ai_dif, track_pic):
            welcome_text = ("""
        Welcome to {}! 
        Distance = {}km
        AI Difficulty = {}
        Track:
        {}

        To begin enter 1
        To return to main menu enter 2

        Note: Once race has started enter:
        - info to get current information of race
        - next to get the next question
        """.format(track_name, distance, ai_dif, track_pic))

            return welcome_text


        wins = 0 # total wins for all tracks
        total_correct = 0
        total_incorrect = 0

        # Lucky lane race
        ll_distance = 4000
        ll_welcome = track_welcome("Lucky Lane", 4, ai_dif, race_art.lucky_lane)

        ll_race = tracks(ll_distance, ll_welcome, ai_dif) # This will run and ask for all inputs
        # return [True, 1, correct_answers, incorrect_answers] 1 means they won the race 0 means they lost

        # return to main menu if player wants to return there
        if not ll_race[0]:
            continue
        if ll_race[1] == 1:
            wins += 1
        total_correct += ll_race[2]
        total_incorrect += ll_race[3]


        # Ghost gorge race
        gg_distance = 6000
        gg_welcome = track_welcome("Ghost Gorge", 6, ai_dif, race_art.ghost_gorge)

        gg_race = tracks(gg_distance, gg_welcome, (ai_dif + 1))

        if not gg_race[0]:
            continue
        if gg_race[1] == 1: 
            wins += 1
        total_correct += gg_race[2]
        total_incorrect += gg_race[3]

        # Volcano Valley race

        vv_distance = 10000
        vv_welcome = track_welcome("Volcano Valley", 10, ai_dif, race_art.volcano_valley)

        vv_race = tracks(vv_distance, vv_welcome, (ai_dif + 2))

        if not vv_race[0]:
            continue
        if vv_race[1] == 1:
            wins += 1
        total_correct += vv_race[2]
        total_incorrect += vv_race[3]

        ending = ("""
        All Races Complete:
        You won {} races

        {}

        Enter 1 to return to Race Mania menu 
        Enter 2 to quit
        """.format(wins, race_art.trophy))

        print(ending)

        play_again = False

        while True:
            end_choice = int(input("> "))

            if end_choice == 1:
                play_again = True
                break
            elif end_choice == 2:
                break
            print("Invalid input")
            continue
        total_points += float(((10 * ai_dif) * (10 * wins) * (10 * total_correct)) / (total_incorrect + 1) )
        ls_info = [race_name, total_points]
        ending_info.append(ls_info) # ending info is what will be added to leaderboard

        if play_again:
            continue
        break
        
    print("Returning to home menu...")
    print()
    return ending_info