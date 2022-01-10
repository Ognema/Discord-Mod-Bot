import online
online.keep_on()
import os, nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType
from datetime import datetime

TESTING_GUILD_ID = 919969623946969119

client = commands.Bot(command_prefix="m.c ")


@client.command()
async def mute(message, user: nextcord.Member, *, reason = None):
  guild = message.guild
  role = guild.get_role(919969623959539724)
  if role in user.roles:
    await user.remove_roles(role, reason=reason)
    await message.send(f"Unmuted {user}")
  else:
    await user.add_roles(role, reason=reason)
    await message.send(f"Muted {user}")
#Delete mute
@client.command()
async def investing(message):
  await message.send("""If you are new to investing in bitcoin,stocks etc. instead of asking in general ask in these channels:
⬛︱nfts - For help with NFT
🎲︱crypto - For help with Crypto
💼︱career-discussion - For help with Future careers and current
📊︱stocks - For help with Stocks""")
#Rules:

@client.command()
async def rule(message, num: int):
  num = num - 1
  data = ["1. Follow Discord's TOS","2. Be respectful with all members","3. No Advertising","4. No NSFW content","5. No spamming in text or VC","6. Do not discuss about sensitive topics","7. No malicious content","8. No Self Bots","9. Do not DM the staff team","10. Profile Picture / Banner Rules","11. Emoji Rules","12. Use English only"]
  await message.send(data[num])

@client.command()
async def rule1(message):
  await message.send("1. Follow Discord's TOS")
  
@client.command()
async def rule2(message):
  await message.send("2. Be respectful with all members")

@client.command()
async def rule3(message):
  await message.send("3. No Advertising")

@client.command()
async def rule4(message):
  await message.send("4. No NSFW content")

@client.command()
async def rule5(message):
  await message.send("5. No spamming in text or VC")

@client.command()
async def rule6(message):
  await message.send("6. Do not discuss about sensitive topics")

@client.command()
async def rule7(message):
  await message.send("7. No malicious content")

@client.command()
async def rule8(message):
  await message.send("8. No Self Bots")

@client.command()
async def rule9(message):
  await message.send("9. Do not DM the staff team ")

@client.command()
async def rule10(message):
  await message.send("10. Profile Picture / Banner Rules")

@client.command()
async def rule11(message):
  await message.send("11. Emoji Rules")

@client.command()
async def rule12(message):
  await message.send("12. Use English only")
  
@client.command()
async def party(message):
  await message.send("https://cdn.discordapp.com/emojis/854728647616757780.gif?size=48&size=40")

@client.command()
async def vibe(message):
  await message.send("https://cdn.discordapp.com/emojis/896774356825411644.gif?v=1&size=64")

#Tags 
@client.command()
async def rotateMHM(message):
  await message.send('https://cdn.discordapp.com/emojis/851682650966982698.gif?size=56')

@client.command()
async def rotate(message, rotate: str):
  if rotate.upper() == "MHM":
    await message.send("https://cdn.discordapp.com/emojis/851682650966982698.gif?size=56")

@client.command()
async def whoASKED(message):
  await message.send('https://tenor.com/view/me-looking-for-who-asked-looking-for-who-asked-who-asked-me-looking-gif-20318322')

@client.command()
async def who(message, rotate: str):
  if rotate.upper() == "ASKED":
    await message.send("https://tenor.com/view/me-looking-for-who-asked-looking-for-who-asked-who-asked-me-looking-gif-20318322")  


@client.command()
async def me(message):
  await message.send('https://tenor.com/view/i-asked-goku-mui-goku-mui-meme-gif-22463661')


@client.command()
async def uno(message):
  await message.send('https://cdn.discordapp.com/emojis/900643070155034645.gif?v=1&size=64')


@client.command()
async def superIDOL(message):
  await message.send('https://tenor.com/view/superidol-gif-23969581')

@client.command()
async def super(message, rotate: str):
  if rotate.upper() == "IDOL":
    await message.send("https://tenor.com/view/superidol-gif-23969581")


@client.command()
async def coding(message):
  await message.send(""" 
   🐍︱python - For Python development
  🕸︱web-dev - For Front-End and Back-End(Database) development
  🔮︱ai-ml - For Artificial Intelligence and Machine Learning
  🤖︱discord-dev  - For discord development
  🎮︱game-dev - For Game development
  👉🏽︱not-python - For other than python like Java,C,C#.""")

@client.command()
async def investment_channels(message):
  await message.send("""
 ︱nfts - For help with NFT
 ︱crypto - For help with Crypto
 ︱career-discussion - For help with Future careers and current
 ︱stocks - For help with Stocks""")
#
@client.event
async def on_ready():
  print("Online")

s_m_a = {}
s_m_b = {}
s_m_aft = {}
s_m_time = {}
s_m_pfp = {}
s_m_id = {}
@client.event 
async def on_message_edit(b, a):
    global s_m_a
    global s_m_b
    global s_m_aft
    global s_m_time
    global s_m_pfp
    global s_m_id
    s_m_a[b.channel.id] = b.author
    s_m_b[b.channel.id] = b.content
    s_m_aft[b.channel.id] = a.content
    s_m_time[b.channel.id] = datetime.now()
    s_m_pfp[b.channel.id] = b.author.avatar.url
    s_m_id[b.channel.id] = b.author.id

@client.command(aliases=['esnipe', 'editsnipe', 'snipeedit'])
@commands.has_any_role(919433872368869436, 905219932776710144,
                       822985879243980870, 896436751273439244,
                       822620759255154749)
async def es(before):
    channel = before.channel
    try:
        sE = nextcord.Embed(
            title=f"Last edited message in #{channel.name}",
            description=str("-Before: ") +
            str(s_m_b[before.channel.id]) +
            str("\n+Now: ") +
            str(s_m_aft[before.channel.id]),
            color=0x0000FF)
        sE.set_footer(
            text=
            f"Sent by {s_m_a[before.channel.id]} |  on {s_m_time[before.channel.id]} | user id = {s_m_id[before.channel.id]}"
        )
        sE.set_thumbnail(url=str(s_m_pfp[before.channel.id]))
        await channel.send(embed=sE)
    except:
        await channel.send(f"There are no edited messages in <#{channel.id}>")

client.sniped_messages = {}

@client.event
async def on_message_delete(ctx):
    channel = client.get_channel(927315614547198062)
    embed=nextcord.Embed(title=f"Deleted message in {ctx.channel}",description=f"`{ctx.content}`", timestamp=ctx.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    await channel.send(embed=embed)
    client.sniped_messages[ctx.channel.id] = (
        ctx.content, ctx.author, ctx.channel.name, ctx.created_at)

@client.command(aliases=['snp', 's'])
async def snipe(ctx):
    try:
        contents, author, channel_name, t1me = client.sniped_messages[ctx.channel.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = nextcord.Embed(description=contents,
                          color=0x0000FF, timestamp=t1me)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)
#
@client.command()
async def kick(ctx ,member : nextcord.Member,*, reason=None):
  await member.kick(reason=reason)
  await ctx.member.send(f"You where kicked because: {+reason}")

@client.command()
async def ban(ctx ,member : nextcord.Member,*, reason=None):
  await member.ban(reason=reason)
  await ctx.member.send(f"You where banned because: {+reason}")
#

@client.slash_command(
    name="announce",
    description="Announce/echo anything to a specified channel.",
    guild_ids=[TESTING_GUILD_ID],
)
async def annoucement_command(
    interaction: Interaction,
    arg1=SlashOption(name="title", description="The Embed's Title.",required=True),
    arg2=SlashOption(name="description", description="The Embed's Description.",required=True),
    arg3: nextcord.abc.GuildChannel=SlashOption(name="channel", description="Where you want to send the message.", channel_types=[ChannelType.text, ChannelType.public_thread], required=True),
):
    await arg3.send(embed=nextcord.Embed(title=arg1, description=arg2))
    await interaction.response.send_message(f"Successfully sent message to {arg3}",ephemeral=True)
  


@client.event
async def on_command_error(message, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await message.send(embed=nextcord.Embed(title=f"Missing Required Argument, **{error.param}**", description=error))
    elif isinstance(error, commands.MemberNotFound):
        await message.send(embed=nextcord.Embed(title=f"Member Not Found, **{error.argument}**", description=error))


client.run(os.environ["TOKEN"])
