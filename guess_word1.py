#this is guess word game 
print("GUESS WORD")
#in this game the user is to guess a number of words in a attempt
print("The goal is to guess the correct word from the list of words below: ")
print("Please Note that Only Three(3) attempt is given")
ber = "--$$##$$--"
attempt = 0
list1 =  ["benzeen123OP", "John@n12WICK", "BuNunm@10pad", "Astr0@t35pad", "Capt@ioy45paD", "PaItM@joG4pad", "KinGn@rmal1"]
list1 = list1 + ["cArbon@1995#", "Motor@504pad", "correct@12pad", "john@n21WICk"]
correct_answer = "John@n12WICK"
# corr = correct_answer.upper()
for i in list1:
  print(ber,i,ber)
user_player = input("please guess the word : ")
for j in range(3):
  if user_player != correct_answer:
    attempt += 1
    user_player = input("please guess the word : ")
    print("the number of attempt is ", attempt)
  
  elif user_player == correct_answer:
    print("CONGAT, You guess the word", "THE WORD IS ", corr)
  else:
    print("PLEASE RESTART THE GAME")
