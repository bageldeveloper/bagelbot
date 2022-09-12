import discord
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.ext import commands

spam = True

bot = commands.Bot(command_prefix='()', help_command=None)
client = Bot("()")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="()help"))

@bot.command()
async def help(ctx):
    await ctx.reply(f'```\n()help: types a list of commands, the thing you just did``````\n()bagel: find it out for yourself``````\n()spam: enter in the message you want to send, the number of times to send it, and it will spam you``````\n()spamstop: stop the bot from spamming you``````\n()spamchat: spams the chat you enter this command into, enter in the message you want to spam and it will spam forever until stopped, only admins can use it``````\n()spamchatstop: stop the bot from spamming the chat, anyone can use this command``````\n()bagel: find it out for yourself``````\nalso {ctx.author} is pretty cringe ngl```')

@bot.command()
async def bagel(ctx):
    await ctx.reply('bagels are tasty ngl')

@bot.command()
async def spam(ctx, message, num):
        for x in range(int(num)):
            await ctx.author.send(message)

@bot.command()
async def spamstop(ctx):
        await ctx.reply("there is no stopping the spam :)")


@bot.command()

@has_permissions(administrator=True)

async def spamchat(ctx, message):
    # EDIT: Set spam to True again so you can restart the loop
    global spam
    spam = True

    while True:
        # If "spam" is set to False, stop looping
        if not spam:
            break

        await ctx.send(message)

@bot.command()
async def spamchatstop(ctx):
    global spam
    spam = False
    await ctx.reply('man why did you stop the spam?')

bot.run('MTAwNDEyOTg1MTc1OTkyNzMyNg.GPgdG_.z5Sx2ju2iAW3PfKcuBQ2vCDumSkr8GCt0DonbI')
