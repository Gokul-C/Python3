#remove ramdom.py from this python files list and run this program.
#because i think it has same names in these two files and it has some conflicts
#its an spambot program that will spam whatsapp,insta,fb etc....

import pyautogui
import time

time.sleep(5)
spamtext = open ("spam.txt","r")
for msg in spamtext:
    pyautogui.typewrite(msg)
    pyautogui.press("enter")