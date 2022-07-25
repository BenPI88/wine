import os
os.system("clear")
print("Wine Installer")
print("A tool for installing Wine on any Debian system from Buster to Bookworm (Works for Bullseye and PIOS too!)")
print("Press Enter To Install")
input("")
os.system("clear")
os.system("cat LICENSE")
print("10 second timeout to agree")
import time
time.sleep(10)
os.system("clear")
os.system("cat LICENSE")
print("Click enter to aggree")
input("")
os.system("sudo dpkg --add-architecture i386 && sudo wget -nc -O /usr/share/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key")
osver = ""
while not str(osver) == "1" or str(osver) == "2" or str(osver) == "3":
  os.system("clear")
  print("What version of debian do you have?")
  print("1: Buster")
  print("2: Bullseye")
  print("3: Bookworm")
  osver = input("Item #: ")
if str(osver) == "1:":
  os.system("sudo wget -nc -P /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/buster/winehq-buster.sources && sudo apt update && sudo apt install --install-recommends winehq-stable")
if str(osver) == "2":
  os.system("sudo wget -nc -P /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bullseye/winehq-bullseye.sources && sudo apt update && sudo apt install --install-recommends winehq-stable")
if str(osver) == "3":
  os.system("sudo wget -nc -P /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources && sudo apt update && sudo apt install --install-recommends winehq-stable")
