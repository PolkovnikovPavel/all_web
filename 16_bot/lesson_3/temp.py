import asyncio, pymorphy2
from discord.ext import commands

TOKEN = "Njk5NjUyNzcyODk4Nzk5Nzc2.XpXi7w.ysa68ThkipSULRZ0kMB8PSkanbo"
morph = pymorphy2.MorphAnalyzer()
bot = commands.Bot(command_prefix='!')


async def timer(hours, minutes, channel):
    delta_t = hours * 3600 + minutes * 60
    await asyncio.sleep(delta_t)
    await channel.send("время Х наступило!")


@bot.event
async def on_ready():
    print(f'{bot.user} подключен к Discord!')
    print('И готов переводить')


@bot.command(name='starform')
async def my_randint(ctx, word):
    word = morph.parse(word)[0].normal_form
    await ctx.send(word)


@bot.command(name='inf')
async def my_randint(ctx, word, num):
    parse = morph.parse(word)[0]
    word = parse.make_agree_with_number(int(num))
    await ctx.send(f'{num} {word[0]}')


@bot.command(name='aliv')
async def my_randint(ctx, word):
    i = morph.parse(word)[0]
    if 'NOUN' not in i.tag:
        await ctx.send('Не существительное')
    elif i.tag.animacy == 'inan':
        await ctx.send('Не живое')
    else:
        await ctx.send('Живое')


bot.run(TOKEN)
