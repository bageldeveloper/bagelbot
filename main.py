import os
import random
import asyncio
from keepalive import keep_alive
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot, CheckFailure, has_permissions
import numpy as np

import itertools
from listsforstuff import ball, jokes
import datetime

spam = True

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot()

status = itertools.cycle(['/help', 'with deez nuts'])


@bot.event
async def on_ready():

  print("Your bot is ready")
  change_status.start()


@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.slash_command(name="help",
                   description="shows a list of commands that you can do")
async def help(ctx):
  await ctx.respond(
    f'```\n()help: types a list of commands, the thing you just did``````\n()eightball: put a question after the command and the truth will be revealed``````\n()bagel: find it out for yourself``````\n()spam: enter in the message you want to send, the number of times to send it, and it will spam you``````\n()spamstop: stop the bot from spamming you``````\n()spamchat: spams the chat you enter this command into, enter in the message you want to spam and it will spam forever until stopped, only admins can use it``````\n()spamchatstop: stop the bot from spamming the chat, anyone can use this command``````\n()bagel: find it out for yourself``````\n()joke: tells you a super funny joke, like actually hilarious, definitley not a list I got from a website``````\nalso {ctx.author} is pretty cringe ngl```'
  )


@bot.slash_command(name="poll",
                   description="starts a poll that users can vote on")
async def poll(ctx, topic, choice1, choice2, seconds):
  if not seconds.isdigit():
    msg = await ctx.send("the 'seconds' value has got to be a number my dude")
    return
  msg = await ctx.send(
    f"{topic} Option 1: {choice1} Option 2: {choice2} Time remaining: {seconds}"
  )
  await msg.add_reaction("1️⃣")
  await msg.add_reaction("2️⃣")

  for x in reversed(range(int(seconds))):
    await asyncio.sleep(1)

    await msg.edit(
      content=
      f"Topic: ```{topic}``` Option 1: ```{choice1}``` Option 2: ```{choice2}``` Time remaining: {str(datetime.timedelta(seconds = x))}"
    )

  newmsg = await ctx.channel.fetch_message(msg.id)
  thing1 = discord.utils.get(newmsg.reactions, emoji="1️⃣").count
  thing2 = discord.utils.get(newmsg.reactions, emoji="2️⃣").count
  await ctx.send(ctx.author.mention)
  await ctx.send("```results:```")

  if thing1 > thing2:
    await ctx.send(
      f"*{choice1}* got *{thing1}* votes, *{choice2}* got *{thing2}* votes. *{choice1}* won!"
    )
  elif thing2 > thing1:
    await ctx.send(
      f"*{choice1}* got *{thing1}* votes, *{choice2}* got *{thing2}* votes. *{choice2}* won!"
    )
  elif thing2 == thing1:
    await ctx.send(
      f"*{choice1}* got *{thing1}* votes, *{choice2}* got *{thing2}* votes. It was a tie!"
    )


@bot.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="general")
  await channel.send(
    f"Yo wassup, @{member}! Check out #rules, enjoy your time here!")


@bot.event
async def on_member_remove(member):
  channel = discord.utils.get(member.guild.channels, name="general")
  await channel.send("Dang, @{member} left us.")


@bot.slash_command(name="bagel", description="why don't you find out!")
async def bagel(ctx):
  await ctx.respond('bagels are tasty ngl')


# @bot.slash_command(name="makeroles",description="creates a message that assigns users roles affter reacting to it. Seperate roles and emojis by /")
# async def makeroles(ctx, roles, reactions):

#   rolethings = roles.split("/")
#   emojithings = reactions.split("/")
#   message = await ctx.send(f"respond with the corresponding emoji for each role: {roles}, {reactions}")
#   for x in rolethings:
#     guild = ctx.guild
#     await guild.create_role(name=str(rolethings[x]))
#   for x in rolethings:
#     await message.add_reaction(emojithings[x])

#   while True:
#     for x in rolethings:
#       reaction = await bot.wait_for_reaction(emojithings[x], message=message)

#       await bot.add_roles(reaction.author, rolethings[x])

# @bot.slash_command(
#   name="saything",
#   description="balls")
# @has_permissions(administrator=True)
# async def saything(ctx, message):
#   # EDIT: Set spam to True again so you can restart the loop


#   await ctx.send(message)
@bot.slash_command(name="joke", description="tells you a SUPER funny joke")
async def joke(ctx):

  await ctx.respond(random.choice(jokes))


@bot.slash_command(
  name="eightball",
  description="the almighty 8ball with answer any question you have.")
async def eightball(ctx, question):
  if not question:
    await ctx.respond("you need to put in a question after the command, stupid"
                      )
  else:
    await ctx.respond(
      f"```Question:``` {question}```Answer:```{random.choice(ball)}")


keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)
