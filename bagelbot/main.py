import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='()', help_command=None)

@bot.command()
async def help(ctx):
    await ctx.reply('```\n()help: types a list of commands, the thing you just did``````\n()bagel: find it out for yourself``````\n()spam: enter in the message you want to send and the number of times to send it and it will spam you with that```')

@bot.command()
async def bagel(ctx):
    await ctx.reply('bagels are tasty ngl')

@bot.command()
async def spam(ctx, message, num:int):
    for x in range(num):
        await ctx.author.send(message)

bot.run('MTAwNDEyOTg1MTc1OTkyNzMyNg.GPgdG_.z5Sx2ju2iAW3PfKcuBQ2vCDumSkr8GCt0DonbI')