#this is guess word game code 
#my_game plan
print("GUESS WORD")
#in this game the user is to guess a number of words in a attempt
print("The goal is to guess the correct word from the list of words give", "the number of attempt given is 3")
ber = "$$##"
attempt = 0
# list1 = "benzeen123OP"
list2 = "Johnon12WICK"
for i in ["benzeen123OP", "Johnon12WICK", "bukunmi109Strom", "AstroStrom345", "Captainboy4567.9", "FaIthOjoGaN4r56", "KinGnormal123"]:
  print(ber, i)
user_player = input("please guess the word : ")
for j in range(3):
  if user_player != list2:
    attempt += 1
    print("the number of attempt is ", attempt)
    user_player = input("please guess the word : ")
  elif user_player == list2:
    print("Congat, you passed")
  else:
    print("please play the game")
