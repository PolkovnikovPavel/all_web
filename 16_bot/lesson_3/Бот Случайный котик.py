import requests, json
from discord.ext import commands

TOKEN = "Njk5NjUyNzcyODk4Nzk5Nzc2.XpXi7w.ysa68ThkipSULRZ0kMB8PSkanbo"
bot = commands.Bot(command_prefix='')


@bot.event
async def on_ready():
    print(f'{bot.user} подключен к Discord!')
    print('И готов показывать случайных котиков или собачек')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'кот' in message.content.lower():
        answer = requests.get('https://api.thecatapi.com/v1/images/search').text
        img = json.loads(answer)
        await message.channel.send(img[0]['url'])
    elif 'соба' in message.content.lower():
        answer = requests.get('https://dog.ceo/api/breeds/image/random').text
        img = json.loads(answer)
        await message.channel.send(img['message'])


bot.run(TOKEN)
