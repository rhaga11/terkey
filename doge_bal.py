# Louis Philippe B. Facun
# DogeClick Bot Channel from dogeclick.com
# Auto joiner (/join)

import asyncio
import logging
import re
import time
import os
import sys

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else '\clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_click_bot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
dogeclick_channel = 'Dogecoin_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.GREEN + '                                                                      \n' + Fore.RESET)
	print(Fore.GREEN + '    -   BY ANAK MAGANG SETEMPAT   -   \n' + Fore.RESET)
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print_msg_time(f'Current account: {me.first_name}({me.username})')
	print_msg_time(Fore.YELLOW + 'withdraw at least 4.00 DOGE' + Fore.RESET)
	
	# Start command /bots
	await client.send_message(dogeclick_channel, '/balance')
	
	# Print balance
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def balance(event):
		message = event.raw_text
		if 'Available balance' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			exit(1)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
