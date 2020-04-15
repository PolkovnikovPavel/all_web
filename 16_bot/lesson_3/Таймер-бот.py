import asyncio
from discord.ext import commands

TOKEN = "Njk5NjUyNzcyODk4Nzk5Nzc2.XpXi7w.ysa68ThkipSULRZ0kMB8PSkanbo"
bot = commands.Bot(command_prefix='')


async def timer(hours, minutes, channel):
    delta_t = hours * 3600 + minutes * 60
    await asyncio.sleep(delta_t)
    await channel.send("время Х наступило!")


@bot.event
async def on_ready():
    print(f'{bot.user} подключен к Discord!')
    print('И готов вести отсчёт времени')


@bot.command(name='set_timer')
async def my_randint(ctx, *text):
    hours, minutes = text[1], text[3]
    await timer(int(hours), int(minutes), ctx)


bot.run(TOKEN)
