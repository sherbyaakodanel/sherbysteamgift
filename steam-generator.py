from pyfiglet import figlet_format
from termcolor import colored
from colorama import init, Fore
import time
import sys
import ctypes
import random
import string
import random
import os

init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Steam Keys Generator|sherbyaakodanel")

ascii_art = figlet_format('sherby')
print(ascii_art)
print('VK - https://vk.com/sherbyaakodanel')

q=int(input("Сколько ключей тебе нужно, друг?\n> "))

for i in range(q):
    for g in range(1):
        x=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        y=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        z=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    print(Fore.LIGHTRED_EX + x + "-" + y + "-" + z)

print(Fore.LIGHTBLUE_EX + "\nТвои ключи были сгенерированы и сохранены в .txt файл. !")
time.sleep(3)

sys.stdout = open("keys.txt", "w")

for i in range(q):
    for g in range(1):
        x=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        y=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        z=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    print(x + "-" + y + "-" + z)

    input()