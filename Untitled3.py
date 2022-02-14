#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random

user_win = 0
computer_win = 0

options = ["rock","paper","scissor"]

while True:
    user_input=input("tpye rock \ paper \ scissor and Q for quit game ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
  

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer_pick",computer_pick)
    if user_input=="rock" and computer_pick=="scissor":
        print("You won")
        user_win+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won")
        user_win+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("You won")
        user_win+=1
    else:
        print("You lost")
        computer_win+=1
    
print("YOU WON",user_win)
print("computer win",computer_win,"\n")
print("GOOD BYE!")


# In[ ]:





# In[ ]:




