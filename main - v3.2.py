from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
from config import *
import sys
import re
import os

import os

# # Proxy information
# proxy_host = '172.232.157.160'
# proxy_port = '8085'
# proxy_secret = 'FgMBAgABAAH8AwOG4kw63Q=='

# # Construct proxy URL
# proxy_url = f'socks5://{proxy_host}:{proxy_port}?secret={proxy_secret}'

# # Proxy information
# proxy_host = '159.89.163.128'
# proxy_port = '7497'


# # Construct proxy URL
# proxy_url = f'socks5://{proxy_host}:{proxy_port}'


# # Proxy information
proxy_host = '139.59.1.14'
proxy_port = '1080'

# # Construct proxy URL for HTTP proxy
proxy_url = f'http://{proxy_host}:{proxy_port}'



bot = Client("bot",

             bot_token= "7186933202:AAH7yxM3KP14n6jnIJcd_MWMh9LSVVTEJYI",
             api_id= 22753807,
             api_hash= "5c0a9c3c5f7185a882e2ac7f6002b754")
auth_users = [1923922961,2002609045]
#romeo & dev acc


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/ITS_NOT_ROMEO",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://github.com/Devansh20055",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/TEAM_SILENT_KING_OG",
            ),
            
        ],
    ]
)



@bot.on_message(filters.command(["start"]) )
async def account_login(bot: Client, m: Message):
    #editable = await m.reply_text(f" 𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 [{m.from_user.first_name}](tg://user?id={m.from_user.id}) 👋!\n\n➠𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n\n➠𝐔𝐬𝐞 /txt 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞.\n\n➠𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲: @ITS_NOT_ROMEO \n")
   # if m.from_user.id in auth_users:
        editable = await m.reply_text(f"** 𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 [{m.from_user.first_name}](tg://user?id={m.from_user.id}) 👋!\n\n➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ♥️\n\n➠ Use /help  Know about me .\n➠ 𝐔𝐬𝐞 /txt 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 \n\n➠𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲: @ITS_NOT_ROMEO \n**" ,reply_markup=keyboard)
    # else:
    #     editable = await m.reply_text("You are not authorized to use this command.")
    # else: m.from_user.id not in  auth_users
    # else:
    #      editable =  await m.reply("**Bhag ♥️Day**", quote=True)
    

@bot.on_message(filters.command(["help"]) )
async def account_login(bot: Client, m: Message):
    
        editable = await m.reply_text(f"**🔰 Method to Use me \n\n1. Send Txt In Fomat like :- `File name : Url` \n2. Send me message with :- `File name : Url `\n\n⚠️ Note : Plz mension batch name & Credits else Bot will Stuck for Method 2   \n\n\n🔰 CURRENTLY I SUPPORT THIS PLFORMS  \n\n1. Physics Wallah : /pw_help For more. \n2. Unacademy : /uc_help  For more. \n3. Classplus : /cp_help For more. \n4. Vision Ias : /vis_help For more.  **" ,reply_markup=keyboard)



@bot.on_message(filters.command(["pw_help"]) )
async def account_login(bot: Client, m: Message):
    
        editable = await m.reply_text(f"**  🔰 Physics Wallah 🔰 \n\n📦 TXT file Format : LINK : URL \n\n📍 Supported Quality : \n👉🏼 720 ,480 ,360 ,240 **" ,reply_markup=keyboard)

@bot.on_message(filters.command(["uc_help"]) )
async def account_login(bot: Client, m: Message):
    
        editable = await m.reply_text(f"** 🔰 Unacademy 🔰 \n\n📦 TXT file Format : LINK : URL \n\n📍 Supported Quality : \n👉🏼 1080 ,720 ,480**" ,reply_markup=keyboard)

@bot.on_message(filters.command(["cp_help"]) )
async def account_login(bot: Client, m: Message):
    
        editable = await m.reply_text(f"** 🔰 ClassPlus 🔰   \n\n📦 TXT file Format : LINK : URL \n\n📍 Supported Quality : \n👉🏼 720 ,480 ,360 **" ,reply_markup=keyboard)

@bot.on_message(filters.command(["vis_help"]) )
async def account_login(bot: Client, m: Message):
    
        editable = await m.reply_text(f"** 🔰 Vision Ias 🔰  \n\n📦 TXT file Format : LINK : URL \n\n📍 Supported Quality : \n👉🏼 Send txt to Developer to Know **" ,reply_markup=keyboard)


@bot.on_message(filters.command("stop") )
async def restart_handler(_, m):
    if m.from_user.id in auth_users:
     await m.reply_text("**STOPPED**🛑🛑", True)
     os.execl(sys.executable, sys.executable, *sys.argv)
    else:
         editable =  await m.reply("**Bhag Bhosadi Ke 😘 \n Ban kr duga / Ban kr ke **", quote=True)



# import subprocess

# @bot.on_message(filters.command(["restart"]))
# async def restart_handler(_, m):
#     if m.from_user.id in auth_users:
#         await m.reply_text("**Restarting...**", True)
#         subprocess.Popen(["python", "main-v3.2.py"])
#         await bot.stop()
#     else:
#         await m.reply_text("**Unauthorized!**", True)


# @bot.on_message(filters.command(["cancel"]))
# async def cancel(_, m):
#     editable = await m.reply_text("Canceling All process Plz wait\n🚦🚦 Last Process Stopped 🚦🚦")
#     global cancel
#     cancel = True
#     await editable.edit("cancled")
#     return


# @bot.on_message(filters.command("restart"))
# async def restart_handler(_, m):
#     await m.reply_text("Restarted!", True)
#     os.execl(sys.executable, sys.executable, *sys.argv)





processing_request = False  # Variable to track if a request is being processed



@bot.on_message(filters.command(["TXT"]))
async def account_login(bot: Client, m: Message):
    global processing_request

    if processing_request:
        if m.from_user.id not in auth_users:
            editable = await m.reply("**Nikal ♥️Day**", quote=True)
        else:
            await m.reply_text("**🫨 I'm currently processing another request.\n Please try again later.**",reply_markup=keyboard)
            return
    else:
        processing_request = True
        editable = await m.reply_text(f"**➠ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐀 𝐏𝐫𝐨𝐩𝐞𝐫 𝐖𝐚𝐲 \n\n➠ TXT FORMAT : LINK : URL \n➠ 𝐌𝐨𝐝𝐢𝐟𝐢𝐞𝐝 𝐁𝐲: @ITS_NOT_ROMO **")
        input: Message = await bot.listen(editable.chat.id)

    if input.document:
        x = await input.download()
        caption = f"**😼 User ID: {m.from_user.id}\n ✨ User Link : [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        caption2 = f"**📌 New txt Download Started\n 👤 Started By: [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        await bot.send_document(-1001605524352, x, caption=caption)
        await input.delete(True)
        await bot.send_message(-1002097681261, caption2)
        file_name, ext = os.path.splitext(os.path.basename(x))
        credit = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
        path = f"./downloads/{m.chat.id}"

        try:
             links = []
             with open(x, "r", encoding="utf-8") as f:
              for line_num, line in enumerate(f, start=1):
                try:
                    links.append(line.strip().split("://", 1))
                except Exception as e:
                    print(f"Error processing line {line_num}: {e}")
                    print(len(links))
                    os.remove(x)
        except Exception as e:
            await m.reply_text("Error occurred while processing the file.🥲")
            print("Error:", e)
            os.remove(x)
            processing_request = False  # Reset the processing flag
            return


    else:
        content = input.text
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send d for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
        res = "UN"
    
    await editable.edit("**Enter Your Name or send `de` for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3

    await editable.edit("Now send the **Thumb URL**\nEg : ```https://telegra.ph/file/0633f8b6a6f110d34f044.jpg```\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    thumb2 = input6.text 
    if thumb.startswith("http://") or thumb.startswith("https://"):
        # getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        getstatusoutput(f"wget {thumb} -O thumb1.jpg")
        thumb = "thumb1.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)
  
    try:
        for i in range(count - 1, len(links)):
            
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V


            # if "appx" in V:
            #     download_cmd = f'{cmd} -R 25 --fragment-retries 25 --proxy "{proxy_url}"'
            # else:
            #     download_cmd = f'{cmd} -R 25 --fragment-retries 25'

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://psitoffers.store/testkey.php?vid=" + id + "&quality="+raw_text2   # link downlod command

             name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
             name = f'{str(count).zfill(3)}) {name1[:60]}'

            # elif '.m3u8' in url:
            #  id =  url.replace("/hls/360/main.m3u8", "")
            #  id2 = id.replace("https://d2bps9p1kiy4ka.cloudfront.net/", "")
            #  url =  "https://psitoffers.store/testkey.php?vid=" + id2 + "&quality="+raw_text2   # link downlod command

            

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            if "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            else: 
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            
            # else
            #     cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:   
                cc = f' **➭ Inedx » {str(count).zfill(3)} **\n**➭ Title »  {name1}.mkv**\n**➭ Batch Name » {b_name} **\n**➭ Qualtiy » {raw_text2}**\n\n✨ **Downloaded by : {CR}**\n**━━━━━━━✦✗✦━━━━━━━**'
                cc1 = f'**➭ Index » {str(count).zfill(3)} **\n**➭ Title » {name1}.pdf** \n**➭ Batch Name » {b_name}**\n\n✨ **Downloaded by : {CR}**\n**━━━━━━━✦✗✦━━━━━━━**'                            
                # cc = f' **➭ Title » {str(count).zfill(3)}.** {name1} ({res}) .mkv\n**➭ Batch Name » {b_name} **\n**➭ Qualtiy »{raw_text2}**\n\n✨ **Downloaded by : [𝒯𝐸𝒜𝑀 𝒮𝐼𝐿𝐸𝒩𝒯 𝒦𝐼𝒩𝒢](https://t.me/TEAM_SILENT_KING_OG)**\n**━━━━━━━✦✗✦━━━━━━━**'
                # cc1 = f'**➭ Title » {str(count).zfill(3)}.** {name1}.pdf \n**➭ Batch Name » {b_name}**\n\n✨ **Downloaded by : [𝒯𝐸𝒜𝑀 𝒮𝐼𝐿𝐸𝒩𝒯 𝒦𝐼𝒩𝒢](https://t.me/TEAM_SILENT_KING_OG)**\n**━━━━━━━✦✗✦━━━━━━━**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        await copy.copy(chat_id = -1002097681261)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e: 
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    if "appx" in url:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f'{cmd} -R 25 --fragment-retries 25 --proxy "{proxy_url}"'
                    else:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f'{cmd} -R 25 --fragment-retries 25'
                    try:
                        prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Index » {str(count).zfill(3)} **\n**➭ File » ** `{name}`\n**➭ Link »** `{url}`\n\n✨ **Bot Made by Devansh**\n**━━━━━━━✦✗✦━━━━━━━**")
                        os.system(download_cmd)
                        time.sleep(1)
                        await prog.delete(True)
                        start_time = time.time()
                        reply = await m.reply_text(f"**⚡️ Starting Uploading...** - `{name}`")
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1, progress=progress_bar, progress_args=(reply, start_time))
                        await reply.delete(True)
                        os.remove(f'{name}.pdf')
                        count += 1
                        time.sleep(2)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    prog = await m.reply_text(f"📥 **Downloading **\n\n**➭ Count » {str(count).zfill(3)} **\n**➭ Video Name » ** `{name}`\n**➭ Quality** » `{raw_text2}`\n**➭ Video Url »** `{url}`\n**➭ Thumbnail »** `{input6.text}` \n\n✨ **Bot Made by Devansh**\n**━━━━━━━✦✗✦━━━━━━━**")
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, thumb2)
                    count += 1

            except Exception as e:
                await m.reply_text(f"**This #Failed File is not Counted**\n**Name** =>> `{name}`\n**Link** =>> `{url}`\n\n ** Fail reason »** {e}")
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    time.sleep(2)
    await m.reply_text("🔰Done🔰")
    await m.reply_text("**✨Thanks for Choosing**")
    processing_request = False  # Reset the processing flag
bot.run()
