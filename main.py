import random
from replit import clear
from art import logo


start_game=input("Do you want to play blackjack (y/n) : ").lower()



def blackjack_game():
  
  should_continue=True
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  def total_calc():
    def draw_card(cards):
      user_chosen_card=random.sample(cards, 2)
      computer_chosen_card=random.sample(cards, 2)
      return user_chosen_card, computer_chosen_card
 
    user_chosen_card,_=draw_card(cards)
    _,computer_chosen_card=draw_card(cards)
   
   
    def calculation(items):
      total=0
      for item in items:
        total+=item
      return total
    user_total=calculation(user_chosen_card)
    computer_total=calculation(computer_chosen_card)
    print(f"Your current cards are {user_chosen_card} and current score is {user_total}")
   
    return user_total, computer_total, user_chosen_card, computer_chosen_card
 
  def new_draw():
    added_user_chosen_card=random.choice(cards)
    added_computer_chosen_card=random.choice(cards)
    return added_user_chosen_card, added_computer_chosen_card
   
  def add_valv(u_t,c_t,u_cc,c_card):
   
   
    user_chosen_card.append(added_user_chosen_card)
   
    computer_chosen_card.append(added_computer_chosen_card)
    new_user_total=user_total+u_cc
    new_computer_total=computer_total+c_card
    return new_user_total, new_computer_total, user_chosen_card, computer_chosen_card
   
  def check_blackjack(chosen_total, chosen_card):
    if chosen_total==21 and len(chosen_card)==2:
      return 0
 
  user_total,computer_total,user_chosen_card,computer_chosen_card=total_calc()
  black_jack_user= check_blackjack(user_total, user_chosen_card)
  black_jack_computer=check_blackjack(computer_total ,computer_chosen_card)
 
  if black_jack_computer==0:
    should_continue=False
    clear()
    print(logo)
    print("you lose, computer got black jack!")
  elif black_jack_user==0:
    should_continue=False
    clear()
    print(logo)
    print("Congrats!!You won! you got black jack!")
  while user_total<21 and computer_total<21 and should_continue:
    next_question=input("Do you want to add another number?(y/n) : ")
    if next_question=="y":
      print(f"Computer first card is :{computer_chosen_card[0]}")
      added_user_chosen_card,added_computer_chosen_card=new_draw()
      user_total,computer_total,new_user_chosen_card,new_computer_chosen_card=add_valv(u_t=user_total,c_t=computer_total,u_cc=added_user_chosen_card,c_card=added_computer_chosen_card)
      print(f"new user total is {user_total} and cards are {new_user_chosen_card}")
      #print(f"new computer total score is {computer_total} and cards are {new_computer_chosen_card}")
    elif next_question=="n":
      should_continue=False
   
      if user_total>computer_total:
        print(f"Congrats!Your score is {user_total} and computer score is {computer_total} You won!")
      elif user_total<computer_total and computer_total<21:
     
        print(f"Sorry !Your score is {user_total} and computer Score is {computer_total} and cards are {computer_chosen_card} You lost!")
 
  if user_total>21 and black_jack_user==0:
    for value in range(len(user_chosen_card)):
      if user_chosen_card[value]==11:
        user_chosen_card[value]=1
       
  if user_total>21:
    print(f"You lose! computer total is {computer_total}")
  elif computer_total>21 and user_total<21:
    should_continue=False
    print(f"Congrats!Your score is {user_total} and computer Score is {computer_total} and cards are {computer_chosen_card} You won!")
 
  if user_total==computer_total and user_total<21:
    print(f"Oh! This game is draw! your cards are {user_chosen_card} and computer cards are {computer_chosen_card}.")

if start_game=="y":
  clear()
  print (logo)
  print("Welcome to the Black Jack game!")
  blackjack_game()
elif start_game=="n":
  print("Good Bye!")
while input("Do you want to play again (y/n): ")=="y":
  clear()
  print(logo)
  blackjack_game()


  