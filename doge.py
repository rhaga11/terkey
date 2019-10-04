# Louis Philippe B. Facun
# DogeClick Bot Channel from dogeclick.com
# Auto joiner (/join)

import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_clickbot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
dogeclick_channel = 'Dogecoin_click_bot'
ltcclick_channel = 'Litecoin_click_bot'
bchclick_channel = 'BCH_clickbot'
zcclick_channel = 'Zcash_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')
	
def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=250)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(Fore.MAGENTA + '    _    _   _    ___  _____ _____ ___ ____ ___    _    _     _ ')
	print(Fore.MAGENTA + '   / \  | \ | |  / _ \|  ___|  ___|_ _/ ___|_ _|  / \  | |   | |')
	print(Fore.MAGENTA + '  / _ \ |  \| | | | | | |_  | |_   | | |    | |  / _ \ | |   | | ')
	print(Fore.MAGENTA + ' / ___ \| |\  | | |_| |  _| |  _|  | | |___ | | / ___ \| |___| |___ ')
	print(Fore.MAGENTA + '/_/   \_\_| \_|  \___/|_|   |_|   |___\____|___/_/   \_\_____|_____|\n' + Fore.RESET)
	
	print(Fore.BLUE + ' ========================================  \n' + Fore.RESET)
	print(Fore.GREEN + ' #Created By Ahmad Nadori   -   \n' + Fore.RESET)
	print(Fore.GREEN + ' #Whatsapp : 0895333386043  -   \n' + Fore.RESET)
	print(Fore.GREEN + ' JANGAN LUPA LIKE & SUBSCRIBE NYA GAES!  -   \n' + Fore.RESET)
	print(Fore.BLUE + ' ========================================  \n' + Fore.RESET)
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python join.py phone_number')
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
	
	#DOGE_click_bot_JOIN
	print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Mengirim perintah /join memindai')
	
	# Start command /join
	await client.send_message(dogeclick_channel, '/join')
	
	# Join the channel
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(f'Bergabung ke @{channel_name}...')
			
			# Join the channel
			await client(JoinChannelRequest(channel_name))
			print_msg_time(f'Verifikasi data...')
			
			# Clicks the joined
			await client(GetBotCallbackAnswerRequest(
				peer=dogeclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	
	# Print waiting hours
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.GREEN + f'Berhasil! Mohon tunggu {waiting_hours} untuk mendapat reward\n' + Fore.RESET)
			
			
			
			#DOGE_click_bot_MSG
	print_msg_time('Tunggu Sebentar /bots sedang memindai')
	
	# Start command /bots
	await client.send_message(dogeclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(dogeclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
			
			#DOGE_click_bot_VISIT
			
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Tunggu sebentar /visit memindai')
	
	# Start command /visit
	await client.send_message(dogeclick_channel, '/visit')
	
	# Start visiting the ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def visit_ads(event):
	
	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				#url = event.message.reply_markup.rows[0].buttons[0].url
			
				if url is not None:
					print_msg_time('Sedang visit ke website...')

					# Parse the html of url
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					
					# Captcha detected
					if captcha is not None:
						print_msg_time(Fore.RED + 'Captcha terdeteksi!'+ Fore.RED +' Mohon untuk skip ads di telegram nya...\n')
									
						# Clicks the skip
						await client(GetBotCallbackAnswerRequest(
							peer=dogeclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))		
		
	# Print earned money
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)
			
			
			
			
			
			
			
			
			
			
			
			
			
			#Ltc_click_bot_JOIN
			
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Mengirim perintah /join memindai')
	
	# Start command /join
	await client.send_message(ltcclick_channel, '/join')
	
	# Join the channel
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(f'Bergabung ke @{channel_name}...')
			
			# Join the channel
			await client(JoinChannelRequest(channel_name))
			print_msg_time(f'Verifikasi data...')
			
			# Clicks the joined
			await client(GetBotCallbackAnswerRequest(
				peer=ltcclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	
	# Print waiting hours
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.GREEN + f'Berhasil! Mohon tunggu {waiting_hours} untuk mendapat reward\n' + Fore.RESET)
			
			
			
			#Ltc_click_bot_MSG
	print_msg_time('Tunggu Sebentar /bots sedang memindai')
	
	# Start command /bots
	await client.send_message(ltcclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(ltcclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
			
			
			#Ltc_click_bot_VISIT
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Tunggu sebentar /visit memindai')
	
	# Start command /visit
	await client.send_message(ltcclick_channel, '/visit')
	
	# Start visiting the ads
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def visit_ads(event):
	
	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				#url = event.message.reply_markup.rows[0].buttons[0].url
			
				if url is not None:
					print_msg_time('Sedang visit ke website...')

					# Parse the html of url
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					
					# Captcha detected
					if captcha is not None:
						print_msg_time(Fore.RED + 'Captcha terdeteksi!'+ Fore.RED +' Mohon untuk skip ads di telegram nya...\n')
									
						# Clicks the skip
						await client(GetBotCallbackAnswerRequest(
							peer=ltcclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))		
		
	# Print earned money
	@client.on(events.NewMessage(chats=ltcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)
			
			
			
			
			
			
			
			
			
			#BCH_click_bot_JOIN
			
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Mengirim perintah /join memindai')
	
	# Start command /join
	await client.send_message(bchclick_channel, '/join')
	
	# Join the channel
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(f'Bergabung ke @{channel_name}...')
			
			# Join the channel
			await client(JoinChannelRequest(channel_name))
			print_msg_time(f'Verifikasi data...')
			
			# Clicks the joined
			await client(GetBotCallbackAnswerRequest(
				peer=bchclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	
	# Print waiting hours
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.GREEN + f'Berhasil! Mohon tunggu {waiting_hours} untuk mendapat reward\n' + Fore.RESET)
			
			
			
			#BCH_click_bot_MSG
	print_msg_time('Tunggu Sebentar /bots sedang memindai')
	
	# Start command /bots
	await client.send_message(bchclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(bchclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
			
			
			#BCH_click_bot_VISIT
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Tunggu sebentar /visit memindai')
	
	# Start command /visit
	await client.send_message(bchclick_channel, '/visit')
	
	# Start visiting the ads
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def visit_ads(event):
	
	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				#url = event.message.reply_markup.rows[0].buttons[0].url
			
				if url is not None:
					print_msg_time('Sedang visit ke website...')

					# Parse the html of url
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					
					# Captcha detected
					if captcha is not None:
						print_msg_time(Fore.RED + 'Captcha terdeteksi!'+ Fore.RED +' Mohon untuk skip ads di telegram nya...\n')
									
						# Clicks the skip
						await client(GetBotCallbackAnswerRequest(
							peer=bchclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))		
		
	# Print earned money
	@client.on(events.NewMessage(chats=bchclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)
			
			
			
			
			#ZCASH_click_bot_JOIN
			
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Mengirim perintah /join memindai')
	
	# Start command /join
	await client.send_message(zcclick_channel, '/join')
	
	# Join the channel
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(f'Bergabung ke @{channel_name}...')
			
			# Join the channel
			await client(JoinChannelRequest(channel_name))
			print_msg_time(f'Verifikasi data...')
			
			# Clicks the joined
			await client(GetBotCallbackAnswerRequest(
				peer=zcclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	
	# Print waiting hours
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.GREEN + f'Berhasil! Mohon tunggu {waiting_hours} untuk mendapat reward\n' + Fore.RESET)
			
			
			
			#ZCASH_click_bot_MSG
	print_msg_time('Tunggu Sebentar /bots sedang memindai')
	
	# Start command /bots
	await client.send_message(zcclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(zcclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
			
			
			#ZCASH_click_bot_VISIT
			print(f'Nama akun anda: {me.first_name}({me.username})\n')
	print_msg_time('Tunggu sebentar /visit memindai')
	
	# Start command /visit
	await client.send_message(zcclick_channel, '/visit')
	
	# Start visiting the ads
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def visit_ads(event):
	
	
		original_update = event.original_update
		if type(original_update)is not UpdateShortMessage:
			if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
				url = event.original_update.message.reply_markup.rows[0].buttons[0].url
				#url = event.message.reply_markup.rows[0].buttons[0].url
			
				if url is not None:
					print_msg_time('Sedang visit ke website...')

					# Parse the html of url
					(status_code, text_response) = get_response(url)
					parse_data = BeautifulSoup(text_response, 'html.parser')
					captcha = parse_data.find('div', {'class':'g-recaptcha'})
					
					# Captcha detected
					if captcha is not None:
						print_msg_time(Fore.RED + 'Captcha terdeteksi!'+ Fore.RED +' Mohon untuk skip ads di telegram nya...\n')
									
						# Clicks the skip
						await client(GetBotCallbackAnswerRequest(
							peer=zcclick_channel,
							msg_id=event.message.id,
							data=event.message.reply_markup.rows[0].buttons[1].data
						))		
		
	# Print earned money
	@client.on(events.NewMessage(chats=zcclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + f'{message}\n' + Fore.RESET)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
