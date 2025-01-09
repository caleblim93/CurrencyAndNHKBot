import discord
import requests
from discord.ext import commands
import Caller
from googletrans import Translator

token = 'TOKEN HERE'
intents = discord.Intents.default()
intents.message_content = True
intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
usd_currencies = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
myr_currencies = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/myr.json"
translator = Translator()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    usd = await get_usd_currencies()
    myr = await get_myr_currencies()
    activity_name = f"1 USD = {usd} yen\n\n1 MYR = {myr} yen"
    activity = discord.Game(name=activity_name)
    await bot.change_presence(activity=activity)

@bot.command()
async def list(ctx):
    await ctx.send("These are the commands:")
    await ctx.send('!list, !main, !featured, !society, !disaster, !politics, !business, !international, !science, !sports, !life')
    await ctx.send('For english translated: put _en behind. Example: !main_en')

@bot.command()
async def main(ctx):
    await ctx.send('Main News JP:')
    titles,links = Caller.call('main')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}: Link: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def main_en(ctx):
    await ctx.send('Main News EN:')
    titles,links = Caller.call('main')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def featured(ctx):
    await ctx.send('Featured News JP :')
    titles,links = Caller.call('featured')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = '\n\n'.join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def featured_en(ctx):
    await ctx.send('Featured News EN:')
    titles,links = Caller.call('featured')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = '\n\n'.join(lines)
    print(f'Message:{message}')
    await command_send_message(ctx,message)

@bot.command()
async def society(ctx):
    await ctx.send('Society News JP :')
    titles,links = Caller.call('society')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def society_en(ctx):
    await ctx.send('Society News EN:')
    titles,links = Caller.call('society')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def disaster(ctx):
    await ctx.send('Disaster News JP :')
    titles,links = Caller.call('disaster')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def disaster_en(ctx):
    await ctx.send('Fetching...')
    await ctx.send('Disaster News EN:')
    titles,links = Caller.call('disaster')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def politics(ctx):
    await ctx.send('Politics News JP :')
    titles,links = Caller.call('politics')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def politics_en(ctx):
    await ctx.send('Politics News EN:')
    titles,links = Caller.call('politics')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def business(ctx):
    await ctx.send('Business News JP :')
    titles,links = Caller.call('business')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def business_en(ctx):
    await ctx.send('Business News EN:')
    titles,links = Caller.call('business')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def international(ctx):
    await ctx.send('International News JP :')
    titles,links = Caller.call('international')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def international_en(ctx):
    await ctx.send('International News EN:')
    titles,links = Caller.call('international')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def science(ctx):
    await ctx.send('Science and Culture News JP :')
    titles,links = Caller.call('science')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def science_en(ctx):
    await ctx.send('Science and Culture News EN:')
    titles,links = Caller.call('science')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def sports(ctx):
    await ctx.send('Sports News JP :')
    titles,links = Caller.call('sports')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def sports_en(ctx):
    await ctx.send('Sports News EN:')
    titles,links = Caller.call('sports')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def life(ctx):
    await ctx.send('Medic and Life News JP :')
    titles,links = Caller.call('life')
    # Combine items and prices into a formatted string
    lines = [f"Title: {title}\nLink: {link}" for title, link in zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)

@bot.command()
async def life_en(ctx):
    await ctx.send('Medic and Life News EN:')
    titles,links = Caller.call('life')
    # Combine items and prices into a formatted string
    lines = [f'Title: {jp_en_translate(title)}\nLink: {link}' for title, link in
             zip(titles, links)]
    message = "\n\n".join(lines)
    await command_send_message(ctx,message)


@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message is "hello"
    if message.content.lower() == "hello":
        print('Message Hello detected!')
        await message.channel.send("Hello! How can I assist you today?")  # Send a response
    elif message.content.lower() == 'usd'  and message.channel.name.lower() == 'usd':
        jpy = await get_usd_currencies()
        await message.channel.send(f"1 USD = {jpy} yen")
    elif message.content.lower() == 'myr' and message.channel.name.lower() == 'myr' :
        myr = await get_myr_currencies()
        await message.channel.send(f"1 MYR = {myr} yen")

    # Process commands
    await bot.process_commands(message)

async def get_usd_currencies():
    response = requests.get(usd_currencies)
    data = response.json()
    currencies_data = data['usd']
    print(f'currencies_data: {currencies_data}')
    print(f'JPY -> USD: {currencies_data["jpy"]}')
    return currencies_data["jpy"]

async def get_myr_currencies():
    response = requests.get(myr_currencies)
    data = response.json()
    currencies_data = data['myr']
    print(f'currencies_data: {currencies_data}')
    print(f'JPY -> USD: {currencies_data["jpy"]}')
    return currencies_data["jpy"]


async def command_send_message(ctx,message):
    # Check Discord's message length limit and send the message
    if len(message) <= 2000:
        await ctx.send(message)  # Send the entire message
    else:
        # Split the message into chunks if it exceeds the limit
        chunks = [message[i:i + 2000] for i in range(0, len(message), 2000)]
        for chunk in chunks:
            await ctx.send(chunk)

async def jp_en_translate(text):
    translated = await translator.translate(text,src="ja", dest="en")
    return translated.text
# Run the bot
bot.run(token)
