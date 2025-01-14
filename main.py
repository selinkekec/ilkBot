import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    
@cool.command(name='bot')
async def _bot(ctx):
    """bot çalışıyor mu?"""
    await ctx.send('Evet bot çalışıyor.')
@bot.event
aasync def _bot

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("token girin")


