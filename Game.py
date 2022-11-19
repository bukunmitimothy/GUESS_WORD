#Game Version 2.0
list1 = ["JBTD@012r", "BGHY@109s", "Atro@200R", "SPAC@578g", "BLAC@600t", "CATR@500y"]
list1 += ["JoHn@234r", "GANI@098s", "Gdrt@567T", "fish@567D"]
number_of_words = len(list1)
corr_ans = list1[3]
#list1 = list1.sort()
print(corr_ans.index("@"))
print(len(list1[-1]))
#introduction to the game
being1 = "Welcome to the guess-the-code, , In this game you will be given a set of code, and in other to win you have to guess the correct code, but remember that you will be givien 4 attempt.  GOOD LUCK and HAVE FUN"
Game_title = being1[14:29]
title = Game_title.upper()
#the instructions
print("                     ", title, )
print(being1)
user_start =( input("Are you ready for this Game: "))
if user_start == "yes" or user_start != "no":
        for i in list1:
            print("$$$- ", i ," -$$$")
         #now the real deal
        user_ans = input("please enter your guessed code : ")
        while len(user_ans) != 9:
                print("please enter one of the code above")
                user_ans = input("please enter your guessed code : ")
        x = 0
        while user_ans != corr_ans:
                    x += 1
                    print("The number of attept ", x)
                    user_ans = input("please enter your guessed code > ")
        print("Congat, you guesses it " , user_ans)
else:
        print("okay bye")
        

                    