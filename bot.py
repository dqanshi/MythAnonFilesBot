#    Copyright (C) 2021 - DragonPower84 | @DragonPower84


import os
import sys
import time
import logging
import pyrogram
import aiohttp
import asyncio
import requests
import aiofiles
from random import randint
from progress import progress
from config import Config
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

DOWNLOAD = "./"

# vars
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

   
bot = Client(
    "AnonFilesBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


START_TEXT = """
Hᴇʟʟᴏ User I'ᴍ <code>MythAɴᴏɴFɪʟᴇsBᴏᴛ</code> 😀 \n\n<code>I Cᴀɴ Uᴘʟᴏᴀᴅ Fɪʟᴇs Tᴇʟᴇɢʀᴀ Tᴏ AɴᴏɴFɪʟᴇs</code>\n\n__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ : **@Kai84_Space**
"""
HELP_TEXT = """
**MythAɴᴏɴFɪʟᴇsBᴏᴛ Hᴇʟᴘ**\n\n__Sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ғɪʟᴇ, I'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴀɴᴏɴғɪʟᴇs.ᴄᴏᴍ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ__\n\n__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Kai84_Space**
"""
ABOUT_TEXT = """
- **Bot :** `AnonFilesBot`
- **Creator :** [Kai84](https://t.me/Kai84_Space)
- **Source :** [Click here](https://github.com/DragonPower84/MythAnonFilesBot)
- **Language :** [Python3](https://python.org)
- **Server :** [Heroku](https://heroku.com)

__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Kai_8_4
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
        
@bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

      
@bot.on_message(filters.media & filters.private)
async def upload(client, message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await client.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="**MadarChod, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ My Bot! Cᴏɴᴛᴀᴄᴛ** [Dᴇᴠᴇʟᴏᴘᴇʀ](https://telegram.Dog/ConKai84_Bot).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ 🏃\nor Fuck Off!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Kai84 Space", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="**System Got Error 404!\nIf Errors Don't Stop,Then Report to **[Developer](https://t.me/ConKai84_bot)**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    m = await message.reply("**Dᴏᴡɴʟᴏᴀᴅɪɴɢ FIʟᴇs Tᴏ Mʏ Sᴇʀᴠᴇʀ ....** 📥😘")
    now = time.time()
    sed = await bot.download_media(
                message, DOWNLOAD,
          progress=progress,
          progress_args=(
            "**Uᴘʟᴏᴀᴅing Pʀᴏᴄᴇss Sᴛᴀʀᴇᴅ Wᴀɪᴛ A Little**\n\n`Fact: Files Tᴀᴋᴇ ᴛɪᴍᴇ Aᴄᴄᴏʀᴅɪɴɢ Yᴏᴜʀ Fɪʟᴇs Sɪᴢᴇ`", 
            m,
            now
            )
        )
    try:
        files = {'file': open(sed, 'rb')}
        await m.edit("**Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ AɴᴏɴFIʟᴇs Sᴇʀᴠᴇʀ Pʟᴇᴀsᴇ Wᴀɪᴛ**")
        callapi = requests.post("https://api.anonfiles.com/upload", files=files)
        text = callapi.json()
        output = f"""
<u>**Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ Tᴏ AɴᴏɴFɪʟᴇs**</u>

**📂 Fɪʟᴇ Nᴀᴍᴇ:** {text['data']['file']['metadata']['name']}

**📦 Fɪʟᴇ Sɪᴢᴇ:** {text['data']['file']['metadata']['size']['readable']}

**📥Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ:** `{text['data']['file']['url']['full']}`

🔅__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Kai_8_4**"""
        btn = InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇ", url=f"{text['data']['file']['url']['full']}")]])
        await msg.edit(output, reply_markup=btn)
        os.remove(sed)
    except Exception:
        await m.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ, Mᴀʏʙᴇ Tɪᴍᴇ Oᴜᴛ Dᴜᴇ Tᴏ Lᴀʀɢᴇ Fɪʟᴇ Sɪᴢᴇ!__")
        return
      
@bot.on_message(filters.regex(pattern="https://") & filters.private & ~filters.edited)
async def kl(client, message):
    msg = await message.reply("__Cʜᴇᴄᴋɪɴɢ Uʀʟ...__")
    links = message.text
    linkv = links.split(" | ")[1]
    try:
        ext = links.split(" | ")[-1]
        await msg.edit("__𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚑𝚎 𝙵𝚒𝚕𝚎 𝚏𝚘𝚛 𝚄 𝙰𝚗𝚍 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚘 𝙰𝚗𝚘𝚗𝙵𝚒𝚕𝚎__")
        files = os.path.join(DOWNLOAD, ext)
        os.system(f"wget -nv '{links}' -O {files}")
        callapi = requests.post("https://api.anonfiles.com/upload", files=files)
        text = callapi.json()
        sendup = f"""
<u>**Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ Tᴏ AɴᴏɴFɪʟᴇs**</u>

**📂 Fɪʟᴇ Nᴀᴍᴇ:** {text['data']['file']['metadata']['name']}

**📦 Fɪʟᴇ Sɪᴢᴇ:** {text['data']['file']['metadata']['size']['readable']}

**📥Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ:** `{text['data']['file']['url']['full']}`

**🔅__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ : **@Kai_8_4**"""
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇ", url=f"{text['data']['file']['url']['full']}")]])
        await msg.edit(sendup, reply_markup=btn)
        os.remove(filename)
    except Exception:
        await msg.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ__")
        
        
bot.start()
print("AnonFilesBot Is Started!,  if Have Any Problems contact @ConKai84_Bot")
idle()
