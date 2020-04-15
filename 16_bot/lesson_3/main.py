import discord
import random
from discord.ext import commands

TOKEN = "Njk5NjUyNzcyODk4Nzk5Nzc2.XpXi7w.ysa68ThkipSULRZ0kMB8PSkanbo"


bot = commands.Bot(command_prefix='')
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']



@bot.command(name='randint')
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


bot.run(TOKEN)
