from dhooks import Webhook, File, Embed
import requests
import pyautogui, time
import sys
import os
import pyfiglet
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from os import system

system("title " + "WEBHOOK SPAMMER")

os.system("cls")

text="Webhook spammer By NeyRox"
cprint(figlet_format(text, font="Basic"), "green") 

embed = Embed(
    description='STOP SENDING LOGGERS SKID :sunglasses:',
    color=0x5CDBF0,
    foistamp='now'
)


web = input("\u001b[31mEntre l'URL du webhook: ")

os.system("cls")

hook = Webhook(web)

image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZkfQK3F_ge3ZbcZPe6B-3aO6hocaQEdilcQ&usqp=CAU'
image2 = 'https://i.imgur.com/xpqgA9z.jpg'
image3 = 'https://pbs.twimg.com/media/Bpvdm-QIgAAsoX5.jpg'

embed.set_author(name='CLOWN', icon_url=image2)
embed.add_field(name='YOURE A FUCKING CLOWN', value='HAHAHAHA')
embed.set_footer(text='FUCK YOU', icon_url=image3)

embed.set_thumbnail(image2)
embed.set_image(image1)


text="SPAM STARTED"
cprint(figlet_format(text, font="Basic"), "red") 
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[32mSpammer 5 fois!")
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[31mSpammer 10 fois!")
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[32mSpammer 15 fois!")
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[31mSpammer 20 fois!")
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[32mSpammer 25 fois!")
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
hook.send(embed=embed)
print("\u001b[31mSpammer 30 fois, relance le logiciel pour spam!")
time.sleep(10)