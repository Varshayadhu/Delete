import imp
import os
import logging
import pyrogram
import random
import asyncio
import pytz
import datetime
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp
from database.connections_mdb import active_connection
import re
import json
import base64

logger = logging.getLogger(__name__)

BATCH_FILES = {}

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Client.on_message(filters.command("start"))
async def start(client, message):


    if message.chat.type in ['group', 'supergroup']:
        buttons = [[
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ]]
        await message.reply_photo(photo=random.choice(PICS), caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup = InlineKeyboardMarkup(buttons), parse_mode='html')
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.mention, total, "Unknown"))       
            await db.add_chat(message.chat.title, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        T = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))

        Time = T.hour
        
        if Time < 12:
            greet="ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ" 
        elif Time < 15:
            greet="ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ" 
        elif Time < 20:
            greet="ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ"
        else:
            greet="ɢᴏᴏᴅ ɴɪɢʜᴛ"
        
        START_TXT = f"""
<b>{greet} {message.from_user.mention}  ʙᴜᴅᴅʏ
ᴍʏ ɴᴀᴍᴇ ɪꜱ  {temp.B_NAME}  ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴍᴏᴠɪᴇꜱ ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ 😈</b>
"""
        buttons = [[
            InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('ʜᴇʟᴘ 💭', callback_data='help'),
            InlineKeyboardButton("🧣ᴀʙᴏᴜᴛ", callback_data="about")
            ],[
            InlineKeyboardButton('🔍sᴇᴀʀᴄʜ', switch_inline_query_current_chat='')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)  
        await message.reply_chat_action("typing")
        time.sleep(0.4)
        lol.edit_text("🎊")
        time.sleep(0.5)
        lol.edit_text("⚡")
        time.sleep(0.3)
        lol.edit_text("ꜱᴛᴀʀᴛɪɴɢ... ")
        time.sleep(0.4)
        lol.delete()
        update.effective_message.reply_sticker("CAACAgUAAx0CUgguZAABARdrYwt_f9vFYZop5n-EGGa80vLar9AAAjsIAAKagolX-O0V64tvzK8pBA")
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=START_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "💢 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 💢", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton("🔃 ᴛʀʏ ᴀɢᴀɪɴ 🔃", callback_data=f"checksub#{message.command[1]}")])
        await client.send_photo(
            photo="https://telegra.ph/file/f5d411fba25ecfa5197fe.jpg",
            chat_id=message.from_user.id,
            caption="☆ ʜᴇʟʟᴏ ᴍʏ ғʀɪᴇɴᴅ ☆\n\n☆ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇsᴜʟᴛ ☆",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        T = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))

        Time = T.hour
        
        if Time < 12:
            greet="ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ" 
        elif Time < 15:
            greet="ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ" 
        elif Time < 20:
            greet="ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ"
        else:
            greet="ɢᴏᴏᴅ ɴɪɢʜᴛ"
        
        START_TXT = f"""
<b>{greet} {message.from_user.mention}  ʙᴜᴅᴅʏ
ᴍʏ ɴᴀᴍᴇ ɪꜱ {temp.B_NAME} ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴍᴏᴠɪᴇꜱ ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ 😈</b>
"""
        buttons = [[
            InlineKeyboardButton('➕ 𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ➕', url='http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('ʜᴇʟᴘ 💭', callback_data='help'),
            InlineKeyboardButton("🧣ᴀʙᴏᴜᴛ", callback_data="about")
            ],[
            InlineKeyboardButton('🔍sᴇᴀʀᴄʜ', switch_inline_query_current_chat='')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_chat_action("typing")
        m=await message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await message.reply_chat_action("typing")
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    file_id = message.command[1]
    files_ = await get_file_details(file_id)
    if not files_:
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
        except Exception as e:
            print(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="CANCEL", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Succesfully Deleted All The Indexed Files.')

