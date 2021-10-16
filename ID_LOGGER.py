import sys, subprocess, json, time, asyncio
try:
    import discord, colorama, pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
from discord.ext import commands
from colorama import Fore
from datetime import datetime

sys.tracebacklimit = 0
blacklisted_servers = []
with open('config.json') as f:
    yamete_kudasai = json.load(f)
token = yamete_kudasai['token']

print(pyfade.Fade.Horizontal(pyfade.Colors.cyan_to_blue, '''

██╗██████╗         ██╗      █████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗        ██║     ██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██║  ██║        ██║     ██║  ██║██║  ██╗ ██║  ██╗ █████╗  ██████╔╝
██║██║  ██║        ██║     ██║  ██║██║  ╚██╗██║  ╚██╗██╔══╝  ██╔══██╗
██║██████╔╝        ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═════╝         ╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝'''))
print(f'''{Fore.LIGHTWHITE_EX}                                                    Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/mass-dm-discord/  
''')


def log_id(id, name, discriminator, guild):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        with open("blacklistedids.json", "r") as file:
            data = json.load(file)
            if id not in data:
                pass
            elif id in data:
                return

        with open("ids.json", "r") as file:
            data = json.load(file)
            time.sleep(0.01)

        if id not in data:
            time.sleep(0.01)
            data.append(id)

            with open("ids.json", "w") as file:
                time.sleep(0.01)
                json.dump(data, file)

            try:
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[{Fore.YELLOW}{guild}{Fore.LIGHTGREEN_EX}] {Fore.YELLOW}{id} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{name}#{discriminator}{Fore.LIGHTGREEN_EX} Total:{Fore.YELLOW} {len(data)}")
            except AttributeError:
                print(f"{Fore.BLUE}{current_time} {Fore.YELLOW} {id} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{name}#{discriminator} {Fore.LIGHTGREEN_EX}Total: {Fore.YELLOW}{len(data)}")
            except:
                pass

    except:
        pass

bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion️"))
    await bot.change_presence(status=discord.Status.idle)
    print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started logging IDs\n')

@bot.event
async def on_message(message):
    await asyncio.sleep(0.1)
    try:
        if message.guild.id in blacklisted_servers:
            return
        else:
            pass
        try:
            if not message.author.bot:
                try:
                    log_id(message.author.id, message.author.name, message.author.discriminator,
                           message.author.guild.name)
                except AttributeError:
                    pass

            if message.author.bot:
                pass
        except AttributeError:
            pass
    except:
        pass

@bot.event
async def on_delete(message):
    await asyncio.sleep(0.1)
    if message.guild.id in blacklisted_servers:
        return
    else:
        pass
        try:
            if not message.author.bot:
                log_id(message.author.id, message.author.name, message.author.discriminator, message.author.guild.name)
            if message.author.bot:
                pass
        except AttributeError:
            pass

@bot.event
async def on_raw_reaction_add(payload):
    await asyncio.sleep(0.1)
    try:
        if payload.member.guild.id in blacklisted_servers:
            return
        else:
            pass
        try:
            if not payload.member.bot:
                log_id(payload.member.id, payload.member.name, payload.member.discriminator, payload.member.guild.name)
        except:
            pass
    except:
        pass


@bot.event
async def on_edit(message):
    await asyncio.sleep(0.1)
    try:
        if message.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not message.author.bot:
                    log_id(message.author.id, message.author.name, message.author.discriminator,
                           message.author.guild.name)
                if message.author.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass

@bot.event
async def on_member_join(member):
    await asyncio.sleep(0.1)
    try:
        if member.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not member.bot:
                    log_id(member.id, member.name, member.discriminator, member.guild.name)
                if member.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass

@bot.event
async def on_member_remove(user):
    await asyncio.sleep(0.1)
    try:
        if user.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not user.bot:
                    log_id(user.id, user.name, user.discriminator, user.guild.name)
                if user.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass

@bot.event
async def on_member_update(before, after):
    await asyncio.sleep(0.1)
    try:
        if after.member.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not after.member.bot:
                    log_id(after.member.id, after.member.name, after.member.discriminator, after.member.guild.name)
                if after.member.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass

@bot.event
async def on_voice_state_update(user, before, after):
    await asyncio.sleep(0.1)
    try:
        if after.user.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not user.bot:
                    log_id(user.id, user.name, user.discriminator, user.guild.name)
                if user.bot:
                    pass
            except AttributeError:
                pass
    except:
         pass

@bot.event
async def on_reaction_add(reaction, member):
    await asyncio.sleep(0.1)
    try:
        if member.guild.id in blacklisted_servers:
            return
        else:
            pass
            try:
                if not member.bot:
                    log_id(member.id, member.name, member.discriminator, member.guild.name)
                if member.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass

bot.run(token, bot=False)
