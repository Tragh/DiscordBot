# bot.py
import os
import io
import discord
import asyncio
from dotenv import load_dotenv
from helper_classes import *

botActionController=BotActionController()


async def reportForDuty(message):
	await message.channel.send("bot reporting for duty!")
		
botActionController.addBotAction(
	channelList=['admin-test', 'admin-chat'],
	onCommand="!bot",
	takeAction=reportForDuty)

async def repostMessage(message):
	await asyncio.sleep(2)
	
	discordFileList=[] #Here we'll store references to the files so that we can upload them
	fileBufferList=[] #Here we'll store the file buffers so that we can close them later
	
	for attachment in message.attachments:
		filebuffer=io.BytesIO() #create a file buffer
		await attachment.save(filebuffer) #save the message's file in the buffer we just made
		discordFileList.append(discord.File(filebuffer,filename=attachment.filename)) #make this filebuffer into a discord file buffer object and add it to the list
		fileBufferList.append(filebuffer) #now append the buffer to the filebufferlist so we can close it later
	
	if len(discordFileList) == 0:
		await message.channel.send(content = message.content[11:])
	else:
		await message.channel.send(content = message.content[11:], files=discordFileList)
	
	for fileBuffer in fileBufferList:
		fileBuffer.close()

botActionController.addBotAction(
	channelList=['admin-chat'],
	onCommand="!botrepost",
	takeAction=repostMessage)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		print(
			f'{client.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.is_system():
		return
	
	for botAction in botActionController.botActionsList:
		if message.channel.name in botAction.channels and (botAction.command == None or message.content.startswith(botAction.command + ' ') or message.content == botAction.command):
			await botAction.action(message)
	
	
	

client.run(TOKEN)
