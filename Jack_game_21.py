
import os,time,random
n_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]#this list for choosen 
u_list=[]
c_list=[]

def display_games():
    while True:
      intro=input("""
    -----------------------------------------------

      ░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗
      ██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝
      ██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░
      ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
      ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
      ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░
    -----------------------------------------------
    1- Froggy
    2- Twenty one
    3- snake
    4- Exit

    Choose number:  """).strip()
      if intro=="1":
        clear_screan()
        pass
      elif intro=="2":
        clear_screan()
        
        Twenty_one()
      elif intro =="3":
        clear_screan()
        pass
      elif intro=="4":
        clear_screan()
        print("Exiting...")
        break
      else:
        clear_screan()
        print("\t\tInvaled input!!!")
def Twenty_one():
  print("\tLOADING...")
  time.sleep(2)
  print("\tPLEASE WAIT...")
  time.sleep(2)
  update_list(u_list)
  update_list(c_list)
  for _ in range(2):
    u_list.append(choose_number(n_list))
    c_list.append(choose_number(n_list))
  print("""
        .------..------..------..------..------.
        |A_  _ ||J_ ww ||K_  _ ||Q_ ww ||10_  _|
        |( \/ )||( \/ )||( \/ )||( \/ )||( \/ )|
        | \  / || \  / || \  / || \  / || \  / |
        |  \/ A||  \/ J||  \/ K||  \/ Q||  \/10|
        `------'`------'`------'`------'`------'
    ____  _            _     _            _    _             
   |  _ \| |          | |   | |          | |  (_)            
   | |_) | |_   _  ___| |__ | | ___ _ __ | | ___ _ __   __ _ 
   |  _ <| | | | |/ __| '_ \| |/ _ \ '_ \| |/ / | '_ \ / _` |
   | |_) | | |_| | (__| | | | |  __/ | | |   <| | | | | (_| |
   |____/|_|\__,_|\___|_| |_|_|\___|_| |_|_|\_\_|_| |_|\__, |
                                                        __/ |
                                                       |___/ 

  """)
  
  while True:
    
    show_cards()
    if check_end_game(u_list)or check_end_game(c_list):
      result(c_list,u_list)
      break
    else:
      if pull_card():
        u_list.append(choose_number(n_list))
      else:
        while sum(c_list)<17:
          c_list.append(choose_number(n_list))
        result(c_list,u_list)
        break
    
def clear_screan():
      os.system("cls"if os.name=="nt"else "clear")

def choose_number(list):
      return random.choice(list)
def check_end_game(list):
      if 11 not in list and sum(list)>=21 or 11 in list and sum(list)==21:
        return True
      elif 11 in list and sum(list)>21:
        list[list.index(11)]=1
        return False
      return False
def show_cards():
  print(f"""
  Your cards are {u_list}, curent score is {sum(u_list)}
  Computer's first card {c_list[0]}""")  
def pull_card():
  qustion=input("\tGet another card (y,n): ").strip().lower()
  if qustion=="y":
    return True
  return False
def update_list(list):
  del list[:]
def result(c_list,u_list):
  print(f"""
  Your final hand: {u_list} with score {sum(u_list)}
  Computer's final hand: {c_list} with score {sum(c_list)}
  """)
  if (sum(c_list)>sum(u_list)and 0<=sum(c_list)<=21)or(sum(u_list)>21):
    print("\tYou lost 😢")
  elif sum(c_list)==sum(u_list):
    print("\tDraw 💩")
  elif sum(c_list)<sum(u_list)and 0<=sum(u_list)<=21 or sum(c_list)>21:
    print("\tYou win 🥳")
  
display_games()

