import os

import discord
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected !')
    await client.change_presence(activity = discord.Game(name="Centralized Logger Bot"))
    log_channel = client.get_channel(int(os.getenv('LOG')))
    print ("Admin Server : " + log_channel.guild.name)


@client.event
async def on_message_delete(message):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    message_embed = discord.Embed(title="MESSAGE DELETED !", description="Server : " + message.author.guild.name, color=0x9A0000)
    message_embed.add_field(name="Content : ", value=message.content, inline=False)
    message_embed.add_field(name="Channel : ", value=message.channel.name, inline=False)
    message_embed.add_field(name="Author name : ", value=message.author.name, inline=False)
    message_embed.add_field(name="Author ID : ", value=message.author.id, inline=False)
    await log_channel.send(embed=message_embed)
    

@client.event
async def on_message(message):
    # Ignore self messages
    if message.author == client.user:
        return


@client.event
async def on_message_edit(before, after):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    message_embed = discord.Embed(title="MESSAGE EDITED !", description="Server : " + before.author.guild.name, color=0x0056FF)
    message_embed.add_field(name="Content before edition : ", value=before.content, inline=False)
    message_embed.add_field(name="Content after edition : ", value=after.content, inline=False)
    message_embed.add_field(name="Channel : ", value=before.channel.name, inline=False)
    message_embed.add_field(name="Author name : ", value=before.author.name, inline=False)
    message_embed.add_field(name="Author ID : ", value=before.author.id, inline=False)
    await log_channel.send(embed=message_embed)


@client.event
async def on_guild_channel_create(channel):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    message_embed = discord.Embed(title="CHANNEL CREATION !", description="Server : " + channel.guild.name, color=0x9DFF00)
    message_embed.add_field(name="Channel name", value=channel.name, inline=False)
    message_embed.add_field(name="Position from top : ", value=str(channel.position), inline=False)
    await log_channel.send(embed=message_embed)

@client.event
async def on_guild_channel_delete(channel):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    message_embed = discord.Embed(title="CHANNEL DELETION !", description="Server : " + channel.guild.name, color=0xF57D00)
    message_embed.add_field(name="Channel name", value=channel.name, inline=False)
    await log_channel.send(embed=message_embed)

@client.event
async def on_webhooks_update(channel):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    admin_server = log_channel.guild
    admin_role = admin_server.get_role(int(os.getenv('ADMIN')))
    message_embed = discord.Embed(title="WEBHOOK MODIFICATION !", description="Server : " + channel.guild.name, color=0xF50000)
    message_embed.add_field(name="ALERT !", value="Modifying webhook could be risky if the member is not allowed to do so !", inline=False)
    await log_channel.send(embed=message_embed)
    await log_channel.send('{}'.format(admin_role.mention) + ", WEBHOOK ALERT !")

@client.event
async def on_member_update(before, after):
    log_channel = client.get_channel(int(os.getenv('LOG')))
    if (before.name != after.name or before.nick != after.nick or before.roles != after.roles):
        before_roles = "<Null>"
        after_roles = "<Null>"
        before_name = "<Null>"
        after_name = "<Null>"
        before_nick = "<Null>"
        after_nick = "<Null>"

        if before.roles != after.roles:
            before_roles = str(before.roles)
            after_roles = str(after.roles)

        message_embed = discord.Embed(title="MEMBER UPDATE !", description="Server : " + before.guild.name, color=0x8C00FF)
        if before.name != None:
            before_name = before.name
        if before.nick != None:
            before_nick = before.nick
        if after.name != None:
            after_name = after.name
        if after.nick != None:
            after_nick = after.nick

        message_embed.add_field(name="Name before and after update : ", value=before_name + " | " + after_name, inline=False)
        message_embed.add_field(name="Nick before and after update : ", value=before_nick + " | " + after_nick, inline=False)
        message_embed.add_field(name="Roles before : ", value=before_roles, inline=False)
        message_embed.add_field(name="Roles after : ", value=after_roles, inline=False)
        await log_channel.send(embed=message_embed)


client.run(TOKEN)
