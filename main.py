import colorama
from colorama import Fore
import pyautogui
import time

print('')

print(Fore.RED + 'Welcome to Spammer!')
print("")

print(Fore.GREEN + '░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░')
print(Fore.GREEN + '██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗')
print(Fore.GREEN + '╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝')
print(Fore.GREEN + '░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗')
print(Fore.GREEN + '██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║', Fore.BLUE + '[*]', Fore.YELLOW + "Dark Tool Zone Sri Lanka")
print(Fore.GREEN + '╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝', Fore.BLUE + '[*]', Fore.YELLOW + "Tool By Mr.Devil (Yohan Deshitha)")

print("")

def menu():
    print(Fore.RED + " [1]. Spam01 \n [2]. Spam02 \n [3]. Spam03 \n [4]. Spam04")
    option = input()

    if option == "1":
      print(Fore.BLUE + "[+] Spam is started in 15 second !")
      print("")
      print(Fore.RED + "[+] Open Whatsapp Web and Open Chat you want to spam !")
      print("")
      print(Fore.YELLOW + "[+] Spam Credits -:", Fore.BLUE + "Lasal" )
      print("")
      f=open("script_1", 'r')

      time.sleep(15)

      for word in f:
         pyautogui.typewrite(word)
         pyautogui.press("Enter")

    if option == "2":
      print(Fore.BLUE + "[+] Spam is started in 15 second !")
      print("")
      print(Fore.RED + "[+] Open Whatsapp Web and Open Chat you want to spam !")
      print("")
      print(Fore.YELLOW + "[+] Spam Credits -:", Fore.BLUE + "Lasal" )
      print("")
      f=open("script_2", 'r')

      time.sleep(15)

      for word in f:
         pyautogui.typewrite(word)
         pyautogui.press("Enter")
         

    if option == "3":
      print(Fore.BLUE + "[+] Spam is started in 15 second !")
      print("")
      print(Fore.RED + "[+] Open Whatsapp Web and Open Chat you want to spam !")
      print("")
      print(Fore.YELLOW + "[+] Spam Credits -:", Fore.BLUE + "B.S.Prabasha" )
      print("")
      f=open("script_3", 'r')

      time.sleep(15)

      for word in f:
         pyautogui.typewrite(word)
         pyautogui.press("Enter")
         
    if option == "4":
      print(Fore.BLUE + "[+] Spam is started in 15 second !")
      print("")
      print(Fore.RED + "[+] Open Whatsapp Web and Open Chat you want to spam !")
      print("")
      print(Fore.YELLOW + "[+] Spam Credits -:", Fore.BLUE + "B.S.Prabasha" )
      print("")
      f=open("script_4", 'r')

      time.sleep(15)

      for word in f:
         pyautogui.typewrite(word)
         pyautogui.press("Enter")
         

menu()




