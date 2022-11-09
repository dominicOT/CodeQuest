#python quiz game
#Author - DominiOT
#09 - 11 - 2022

import time
import sys



def mainPlay():
    print("                   Welcome to CodeVer")
    print("Personalize your game play.")
    time.sleep(1)
    p_gamePlay = input('''1. Tough.   (1)
    2. Difficult.        (2)
    3. Normal.           (3)
    4. Simple.           (4)
    5. Random.           (5)
    ''')


                                                #TOUGH GAMEPLAY
    def tough_gplay():
#question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 2
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 3
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")



                                                #DIFFICULT GAMEPLAY
    def diff_gplay():
#question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 2
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 3
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")



                                                    #NORMAL GAMEPLAY
    def norm_gplay():
#question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 2
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 3
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")



                                                #SIMPLE GAMEPLAY
    def simp_gplay():
#question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 2
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 3
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
    

                                                #RANDOM GAMEPLAY
    def rand_gplay():
#question 1
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 2
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")
        
#question 3
        print("Question 1 ....")
        time.sleep(2)
        t_ansr1 = input("")

        if t_ansr1 == "":
            print("Correct!!")
        else:
            print("Incorrect!!")



    if p_gamePlay == "1":
        tough_gplay()
    elif p_gamePlay == "2":
        diff_gplay()
    elif p_gamePlay == "3":
        norm_gplay()
    elif p_gamePlay == "4":
        simp_gplay()
    elif p_gamePlay == "5":
        rand_gplay()
    else:
        sys.exit()


#def exitPlay():

#def changeUsrNm():

#def rateGame():

#def usrData():


print("             Welcome to CodeVer Quiz Game!")
plyr_name = input("Enter Your Name:")
time.sleep(2)
plyr_age = input("Enter Your Age: ")
plyr_ageInt = int(plyr_age)
time.sleep(2)
plyr_gend = input("Enter Your Preferred Gender: ")
time.sleep(2)

if plyr_ageInt <= 17:
    if plyr_gend == NULL:
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

if desc == 'P' or 'p':
    print("               .....processing....")
    time.sleep(4)
    mainPlay()

elif desc == 'X' or 'x':
    sys.exit()
    
elif desc == 'M' or 'm':
    print("")

elif desc == "R" or 'r':
    print("https://github.com/DominicOT")

else:
    print("...")
