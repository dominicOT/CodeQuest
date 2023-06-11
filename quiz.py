# Python quiz game
# Author - DominiOT
# 09 - 11 - 2022

import time
import sys

def main_play():
    print("                   Welcome to CodeVer")
    print("Personalize your game play.")
    time.sleep(1)
    p_game_play = input('''
    1. Tough.   (1)
    2. Difficult.        (2)
    3. Normal.           (3)
    4. Simple.           (4)
    5. Random.           (5)
    ''')

    # Tough gameplay
    def tough_gplay():
        # Question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 2
        print("Question 2 ....")
        time.sleep(2)
        t_ansr2 = input("")

        if t_ansr2 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 3
        print("Question 3 ....")
        time.sleep(2)
        t_ansr3 = input("")

        if t_ansr3 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

    # Difficult gameplay
    def diff_gplay():
        # Question 1
        print("Question 1 ....")
        time.sleep(2)
        d_ansr1 = input("")

        if d_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 2
        print("Question 2 ....")
        time.sleep(2)
        d_ansr2 = input("")

        if d_ansr2 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 3
        print("Question 3 ....")
        time.sleep(2)
        d_ansr3 = input("")

        if d_ansr3 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

    # Normal gameplay
    def norm_gplay():
        # Question 1
        print("Question 1 ....")
        time.sleep(2)
        n_ansr1 = input("")

        if n_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 2
        print("Question 2 ....")
        time.sleep(2)
        n_ansr2 = input("")

        if n_ansr2 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 3
        print("Question 3 ....")
        time.sleep(2)
        n_ansr3 = input("")

        if n_ansr3 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

    # Simple gameplay
    def simp_gplay():
        # Question 1
        print("Question 1 ....")
        time.sleep(2)
        s_ansr1 = input("")

        if s_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 2
        print("Question 2 ....")
        time.sleep(2)
        s_ansr2 = input("")

        if s_ansr2 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 3
        print("Question 3 ....")
        time.sleep(2)
        s_ansr3 = input("")

        if s_ansr3 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

    # Random gameplay
    def rand_gplay():
        # Question 1
        print("Question 1 ....")
        time.sleep(2)
        r_ansr1 = input("")

        if r_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 2
        print("Question 2 ....")
        time.sleep(2)
        r_ansr2 = input("")

        if r_ansr2 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

        # Question 3
        print("Question 3 ....")
        time.sleep(2)
        r_ansr3 = input("")

        if r_ansr3 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")

    if p_game_play == "1":
        tough_gplay()
    elif p_game_play == "2":
        diff_gplay()
    elif p_game_play == "3":
        norm_gplay()
    elif p_game_play == "4":
        simp_gplay()
    elif p_game_play == "5":
        rand_gplay()
    else:
        sys.exit()


print("             Welcome to CodeVer Quiz Game!")
player_name = input("Enter Your Name:")
time.sleep(2)
player_age = input("Enter Your Age: ")
player_age_int = int(player_age)
time.sleep(2)
player_gender = input("Enter Your Preferred Gender: ")
time.sleep(2)

if player_age_int <= 17:
    if player_gender == "":
        print("Requirement Not Met!!")
    sys.exit()

print("Game Instructions...>>")
print("")
print('''
1. CodeVer is a Trivia Quiz Game. Every question is based on reality and tech.
2. To Continue with the game, press P
3. To exit, press X
4. To change your username, press M
5. To check your stats, press S
5. To rate or contribute to the game, press R
6. GoodLuck!!
''')

desc = input("")

if desc.lower() == 'p':
    print("               .....processing....")
    time.sleep(4)
    main_play()
elif desc.lower() == 'x':
    sys.exit()
elif desc.lower() == 'm':
    print("")
elif desc.lower() == "r":
    print("https://github.com/DominicOT")
else:
    print("...")
