import sys, subprocess, random, json, asyncio, os, time
try:
    import colorama, pyfade, discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from colorama import Fore
from datetime import datetime
from discord.ext import commands
def error_msg():
    print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """Bruhhhh
Seems like you\'re new to Python and/or JSON..
Join the Support-Server and lemme help you :)
https://dsc.gg/hoemotion"""))
    time.sleep(10)
    input(f"{Fore.YELLOW}Press Enter to exit the script")
    raise SystemExit
sys.tracebacklimit = 0
bot = discord.Client()
with open('config.json') as f:
    yamete_kudasai = json.load(f)
token = yamete_kudasai['token']
cooldown = yamete_kudasai['min_cooldown']
cooldown_max = yamete_kudasai['max_cooldown']
display_sleep = yamete_kudasai['display_sleep']
message = yamete_kudasai['message']
duplicate = yamete_kudasai['dm_already_dmed_users']
fetch_users = yamete_kudasai['always_fetch_users']
send_embed = yamete_kudasai['send_embed']
embed_title = yamete_kudasai['embed_title']
embed_description = yamete_kudasai['embed_description']
embed_author = yamete_kudasai['embed_author']
embed_author_icon_url = yamete_kudasai['embed_author_icon_url']
embed_footer = yamete_kudasai['embed_footer']
embed_footer_icon_url = yamete_kudasai['embed_footer_icon_url']
embed_thumbnail_url = yamete_kudasai['embed_thumbnail_url']
embed_image_url = yamete_kudasai['embed_image_url']
embed_color = yamete_kudasai['embed_color']
if duplicate == "True":
    munanyo = "True"
elif duplicate == "False":
    munanyo = "False"
else:
    print(f"{Fore.RED}[DUPLICATE ERROR]")
    error_msg()

async def mass_dm():
    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("blacklistedids.json", "r") as file:
        blcklstdata = json.load(file)
    with open("alreadyusedids.json", "r") as file:
        penis = json.load(file)


    indx = 0
    for i in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        indx += 1
        if i in blcklstdata:
            if fetch_users == "False":
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
            elif fetch_users == "True":
                chupapi = await bot.fetch_user(i)
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                print(f"{Fore.YELLOW}Sleeping 2 seconds")
                await asyncio.sleep(2)
            else:
                print(f"{Fore.RED}[FETCH USERS ERROR]")
                error_msg()
        elif munanyo == "False":
            if i in penis:
                if fetch_users == "False":
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                elif fetch_users == "True":
                    chupapi = await bot.fetch_user(i)
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                    print(f"{Fore.YELLOW}Sleeping 2 seconds")
                    await asyncio.sleep(2)
                else:
                    print(f"{Fore.RED}[FETCH USERS ERROR]")
                    error_msg()
            else:
                chupapi = await bot.fetch_user(i)
                try:
                    await chupapi.send(message)
                    print(
                        f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if display_sleep == "True":
                          print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
                except discord.Forbidden as e:
                    if e.code == 40003:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                        await asyncio.sleep(45)
                        os.execv(sys.executable, ['python'] + sys.argv)
                        continue
                    else:
                        print(
                            f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                        pablo = random.randint(cooldown, cooldown_max)
                        if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                        else:
                            pass
                        await asyncio.sleep(pablo)
                if chupapi.id not in penis:
                    await asyncio.sleep(0.01)
                    penis.append(chupapi.id)

                    with open("alreadyusedids.json", "w") as file:
                        await asyncio.sleep(0.01)
                        json.dump(penis, file)
        else:
            try:
                chupapi = await bot.fetch_user(i)
                await chupapi.send(message)
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                pablo = random.randint(cooldown, cooldown_max)
                if display_sleep == "True":
                    print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                else:
                    pass
                await asyncio.sleep(pablo)
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                    await asyncio.sleep(45)
                    os.execv(sys.executable, ['python'] + sys.argv)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if display_sleep == "True":
                        print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
            if chupapi.id not in penis:
                await asyncio.sleep(0.01)
                penis.append(chupapi.id)

                with open("alreadyusedids.json", "w") as file:
                    await asyncio.sleep(0.01)
                    json.dump(penis, file)

    input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]

async def mass_dm_embed():
    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("blacklistedids.json", "r") as file:
        blcklstdata = json.load(file)
    with open("alreadyusedids.json", "r") as file:
        penis = json.load(file)
    embed = discord.Embed(
        title=embed_title,
        descrtiption=embed_description,
        color=embed_color, )
    if embed_thumbnail_url != "":
        embed.set_thumbnail(url=f"{embed_thumbnail_url}"),
    if embed_image_url != "":
        embed.set_image(url=f"{embed_image_url}"),
    if embed_author_icon_url != "":
        embed.set_author(name=f"{embed_author}")
    else:
        embed.set_author(name=f"{embed_author}", icon_url=f"{embed_author_icon_url}")
    if embed_footer_icon_url != "":
        embed.set_footer(text=f"{embed_footer}")
    else:
        embed.set_author(text=f"{embed_author}", icon_url=f"{embed_footer_icon_url}")

    indx = 0
    for i in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        indx += 1
        if i in blcklstdata:
            if fetch_users == "False":
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
            elif fetch_users == "True":
                chupapi = await bot.fetch_user(i)
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                print(f"{Fore.YELLOW}Sleeping 2 seconds")
                await asyncio.sleep(2)
            else:
                print(f"{Fore.RED}[FETCH USERS ERROR]")
                error_msg()
        elif munanyo == "False":
            if i in penis:
                if fetch_users == "False":
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                elif fetch_users == "True":
                    chupapi = await bot.fetch_user(i)
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                    print(f"{Fore.YELLOW}Sleeping 2 seconds")
                    await asyncio.sleep(2)
                else:
                    print(f"{Fore.RED}[FETCH USERS ERROR]")
                    error_msg()
            else:
                chupapi = await bot.fetch_user(i)
                try:
                    await chupapi.send(embed)
                    print(
                        f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if display_sleep == "True":
                          print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
                except discord.Forbidden as e:
                    if e.code == 40003:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                        await asyncio.sleep(45)
                        os.execv(sys.executable, ['python'] + sys.argv)
                        continue
                    else:
                        print(
                            f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                        pablo = random.randint(cooldown, cooldown_max)
                        if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                        else:
                            pass
                        await asyncio.sleep(pablo)
                if chupapi.id not in penis:
                    await asyncio.sleep(0.01)
                    penis.append(chupapi.id)

                    with open("alreadyusedids.json", "w") as file:
                        await asyncio.sleep(0.01)
                        json.dump(penis, file)
        else:
            try:
                chupapi = await bot.fetch_user(i)
                await chupapi.send(embed)
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                pablo = random.randint(cooldown, cooldown_max)
                if display_sleep == "True":
                    print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                else:
                    pass
                await asyncio.sleep(pablo)
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                    await asyncio.sleep(45)
                    os.execv(sys.executable, ['python'] + sys.argv)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if display_sleep == "True":
                        print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
            if chupapi.id not in penis:
                await asyncio.sleep(0.01)
                penis.append(chupapi.id)

                with open("alreadyusedids.json", "w") as file:
                    await asyncio.sleep(0.01)
                    json.dump(penis, file)

    input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]

print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''
███╗   ███╗ █████╗  ██████╗ ██████╗        ██████╗ ███╗   ███╗
████╗ ████║██╔══██╗██╔════╝██╔════╝        ██╔══██╗████╗ ████║
██╔████╔██║███████║╚█████╗ ╚█████╗         ██║  ██║██╔████╔██║
██║╚██╔╝██║██╔══██║ ╚═══██╗ ╚═══██╗        ██║  ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██████╔╝██████╔╝        ██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝         ╚═════╝ ╚═╝     ╚═╝'''))
print(f'''{Fore.LIGHTWHITE_EX}                                             Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/mass-dm-discord/  
''')

@bot.event
async def on_ready():
    if send_embed == "False":
        await bot.change_presence(status=discord.Status.idle)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
        print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')
        await mass_dm()
    elif send_embed == "True":
        await bot.change_presence(status=discord.Status.idle)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
        print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending Embed Messages to the IDs\n')
        await mass_dm_embed()
    else:
        error_msg()

try:
    bot.run(token, bot=False)
except:
    print(f"{Fore.RED}TOKEN ERROR")
    error_msg()