import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, int(s1), int(s2)):
    await ctx.send("toplam: " {s1+s2})

@bot.command()
async def eksilt(ctx, int(s1), int(s2)):
    await ctx.send(f"fark: " {s1-s2})

@bot.command()
async def bolme(ctx, int(s1), int(s2)):
    await ctx.send(f"carpim: " {s1/s2})

@bot.command()
async def carpma(ctx, int(s1), int(s2)):
    await ctx.send(f"bolum: " {s1*s2})

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run("")
