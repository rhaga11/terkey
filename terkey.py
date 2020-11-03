import os
from time import sleep

biru = "\033[1;36m"
maroon = "\033[1;35m"
hijau = "\033[1;32m"
kuning = "\033[1;33m"

os.system('clear')
print(f"""{maroon}\n\nTERMUX SHORTCUT PROPERTIES\npython 3.9 ~ rayez\n""")

sleep(1)
print(f"\n{maroon}[{biru}+{maroon}] {kuning}Making termux directory..! ")
sleep(1)
print(f"\n{maroon}[{hijau}+{maroon}] {hijau}Success..*\n")

try:
  os.mkdir('/data/data/com.termux/files/home/.termux')
except:
  pass

sleep(1)
print(f"\n{maroon}[{biru}+{maroon}] {kuning}Setting Shortcut..! ")
sleep(1)
print(f"\n{maroon}[{hijau}+{maroon}] {hijau}Success..*\n")

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
f = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
f.write(key)
f.close()

sleep(1)
print(f"\n{maroon}[{biru}+{maroon}] {kuning}Reload Termux Settings..! ")
sleep(1)
print(f"\n{maroon}[{hijau}+{maroon}] {hijau}Success..*\n")
os.system('termux-reload-settings')

sleep(2)
print(f"\n{maroon}[{hijau}+{maroon}] {hijau}Done, Restart your Termux ^^ \n")

