import os
import discord
import requests
import random
from discord.ext import commands
import asyncio
import json
import time


# Add bot to a server you have permissions in:
# https://discord.com/api/oauth2/authorize?client_id=864943618853961768&permissions=0&scope=bot

TOKEN = "hi"
lvl = 0
exp = 0
random.jokes = [
    "I'm afraid for the calendar. Its days are numbered.",
    "My wife said I should do lunges to stay in shape. That would be a big step forward.",
    "Why do fathers take an extra pair of socks when they go golfing?" " In case they get a hole in one!",
    "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
    "What do a tick and the Eiffel Tower have in common?" " They're both Paris sites.",
    "What do you call a fish wearing a bowtie?" " Sofishticated.",
    "What do you call a factory that makes okay products?" " A satisfactory.",
    "What did the janitor say when he jumped out of the closet?" " Supplies!",
    "Have you heard about the chocolate record player? It sounds pretty sweet.",
    "How does the moon cut his hair?" " Eclipse it.",
    "What did one wall say to the other?" " I'll meet you at the corner.",
    "Where do fruits go on vacation?" " Pear-is!",
    "I asked my dog what's two minus two. He said nothing.",
    "What did Baby Corn say to Mama Corn?" " Where's Pop Corn?",
    "Dad, did you get a haircut?" " No, I got them all cut!",
    "How do you get a squirrel to like you? Act like a nut.",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "I don't trust stairs. They're always up to something.",
    "What do you call someone with no body and no nose? Nobody knows.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What did one hat say to the other?" " Stay here! I'm going on ahead.",
    "Dad, can you put my shoes on?" " No, I don't think they'll fit me.",
    "What does a lemon say when it answers the phone?" "Yellow!",
    "This graveyard looks overcrowded. People must be dying to get in.",
    "What kind of car does an egg drive?" " A yolkswagen.",
    "Dad, can you put the cat out?" " I didn't know it was on fire.",
    "Why didn't the skeleton climb the mountain?" " It didn't have the guts.",
    "How many tickles does it take to make an octopus laugh? Ten tickles.",
    "I have a joke about chemistry, but I don't think it will get a reaction.",
    "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
    "What does a bee use to brush its hair?" " A honeycomb!",
    "How do you make a tissue dance? You put a little boogie in it.",
    "Why did the math book look so sad? Because of all of its problems!",
    "What kind of shoes do ninjas wear? Sneakers!",
    "How does a penguin build its house? Igloos it together.",
    "How did Harry Potter get down the hill?" " Walking. JK! Rowling.",
    "What do you call a fake noodle?" " An impasta.",
    "What do you call a belt made of watches?" " A waist of time.",
    "What happens when a strawberry gets run over crossing the street?" " Traffic jam.",
    "What do you call two monkeys that share an Amazon account?" " Prime mates.",
    "What do you call a pony with a sore throat?" " A little hoarse.",
    "Where do math teachers go on vacation?" " Times Square.",
    "Whenever I try to eat healthy, a chocolate bar looks at me and Snickers.",
    "What's a robot's favorite snack?" " Computer chips.",
    "Mountains aren't just funny. They're hill areas.",
    "How do you get a good price on a sled?" " You have toboggan.",
    "How can you tell if a tree is a dogwood tree?" " By its bark.",
    "When does a joke become a dad joke?" " When it becomes apparent.",
    "Did you hear about the circus fire? It was in tents.",
    "Can February March? No, but April May!",
    "What’s an astronaut’s favorite part of a computer? The space bar.",
    "What did the fish say when he hit the wall? Dam.",
    "If you see a crime happen at the Apple store, what does it make you?" " An iWitness.",
]

responses = ["No",
        "Yes",
        "My sources say no",
        "It seems likely",
        "Nope"
        "Absolutely"
        "100% not"
        "Certainly"]

coin_sides = ["**Heads**", "**Tails**"]



bot = commands.Bot(command_prefix = ".")


#Deletes default 'help' command
bot.remove_command('help')
#Help list with commands descriptions
@bot.command(pass_context=True)
async def help(ctx, aliases=['commands', 'commandinfo']):
    embed = discord.Embed(
        colour = discord.Colour.blue())
    embed.set_author(name='---List of Commands Available---')
    embed.add_field(name='.serverinfo', value='Provides information about the server.', inline=False)
    embed.add_field(name='.clear', value='Clears the specified amount of messages.', inline=False)
    embed.add_field(name='.changenick', value='Changes the specified users nickname.', inline=False)
    embed.add_field(name='.ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='.cat', value='Sends a random cat image', inline=False)
    embed.add_field(name='.say', value='The bot messages what you want it to', inline=False)
    embed.add_field(name='.8ball', value='Responds to your yes or no question', inline=False)
    embed.add_field(name='.joke', value='Tells you a random joke', inline=False)
    embed.add_field(name='.coinflip', value='Flips a coin', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice(coin_sides))


@bot.command(pass_context=True, change_nickname=True)
async def changenick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'{member.mention}, your nickname has successfully been changed to {nick}.')


@bot.command(aliases= ['purge','delete'])
async def clear(ctx, amount = 50): # Change amount
    if ctx.message.author.id == 410559071373230095:
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} messages cleared!')
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)
    else:
        await ctx.channel.send(f"{ctx.author.mention} You don't have permission to use this command.", color=0xff00f6)

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.id == 410559071373230095:
        muted = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role)
        await ctx.send(f"User {member.mention} was muted by {ctx.author.mention}!")
    else:
        await ctx.send(f"{ctx.author.mention} You don't have permission to use this command.", color=0xff00f6)

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.id == 410559071373230095:
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted)
        await ctx.send(f"{member.mention} was unmuted by {ctx.author.mention}!")
    else:
        await ctx.send(f"{ctx.author.mention} You don't have permission to use this command.", color=0xff00f6)

@bot.command()
async def say(ctx, msg=None):
    if msg is not None:
        await ctx.send(msg)
        await ctx.message.delete()


@bot.command()
async def cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()

    cat_embed = discord.Embed()
    cat_embed.set_image(url=f"{r[0]['url']}")
    embed = discord.Embed(title="Cat!", color=discord.Color.purple())
    await ctx.send(embed=cat_embed)


#Joke command
@bot.command()
async def joke(ctx):
    await ctx.send(f'{random.choice(random.jokes)}')


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question):
  eightballresponses = [
discord.Embed(title=f'Question: {question}\nAnswer: "No"'),
discord.Embed(title=f'Question: {question}\nAnswer: "Yes"'),
discord.Embed(title=f'Question: {question}\nAnswer: "My sources say no"'),
discord.Embed(title=f'Question: {question}\nAnswer: "It seems likely"'),
discord.Embed(title=f'Question: {question}\nAnswer: "Nope"'),
discord.Embed(title=f'Question: {question}\nAnswer: "Absolutely"'),
discord.Embed(title=f'Question: {question}\nAnswer: "100% not"'),
discord.Embed(title=f'Question: {question}\nAnswer: "Certainly"'),]
  responses = random.choice(eightballresponses)
  await ctx.send(embed=responses)


@bot.command()
async def serverinfo(ctx):
    discord.Embed(title="Server Info")
    await ctx.send ("Whatever this server is. It's pretty epic. :sunglasses:")


# latency
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms ')


# If there is an error, it will answer with an error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')


@bot.event
async def on_ready():
    print("The Bot is Ready")


# Startup Information
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over Mr Squidward\'s servers'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await ctx.send(f'Welcome to the server {member.mention}')

bot.run(TOKEN)
