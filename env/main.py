import discord
from discord.ext import commands
import asyncio

valid_keys = ["ANTI-D424FFAD3", "ANTI-3FF48384D", "ANTI-F433FDSDA"]  # Replace with your own list of valid keys
registered_users = {}
MOD_ROLE_ID = 1098926785774760007 # Replace with the ID of your mod role

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def download(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name="**Download**", value="https://www.mediafire.com/file/de0eh7fq6ohhlrl/AntiCheat.rar/file")

    await ctx.author.send(embed=embed)
    await ctx.send("**Sent!**")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def register(ctx, key):
    if key in valid_keys:
        if key in registered_users.values():
            await ctx.send(f"{ctx.author.mention}, this key has already been registered by another user.")
        else:
            registered_users[ctx.author.id] = key
            await ctx.send(f"{ctx.author.mention}, you have been registered with key `{key}`!")
    else:
        await ctx.send(f"{ctx.author.mention}, invalid key!")

@bot.command()
async def clear(ctx, amount=5):
    if amount <= 0 or amount > 100:
        await ctx.send("You can only clear between 1 and 100 messages at once.")
    else:
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"Cleared {amount} messages.", delete_after=2.0)

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    roles = [role for role in server.roles if role != ctx.guild.default_role]

    embed = discord.Embed(title=f"{server.name} Server Information", color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon.url)
    embed.add_field(name="Server Name:", value=server.name, inline=False)
    embed.add_field(name="Server ID:", value=server.id, inline=False)
    embed.add_field(name="Owner:", value=server.owner.mention, inline=False)
    embed.add_field(name="Region:", value=str(server.region).capitalize(), inline=False)
    embed.add_field(name="Members:", value=server.member_count, inline=False)
    embed.add_field(name="Channels:", value=len(server.channels), inline=False)
    embed.add_field(name="Roles:", value=len(roles), inline=False)

@bot.command(name='avatar')
async def avatar(ctx, *, member: discord.Member = None):
    member = member or ctx.author
    try:
        embed = discord.Embed(title=f"{member.name}'s Avatar")
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    except AttributeError:
        await ctx.send("This user does not have an avatar.")




bot.run('MTA5ODg5Nzk0OTQ0ODIxNjYxNg.Gi6A-k.ejiDBK-31cmx3IgVXh3SIXlos9AxDGx7Dks3OQ')
