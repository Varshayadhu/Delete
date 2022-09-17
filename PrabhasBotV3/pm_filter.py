# Kanged From @sachin9742s
import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, DELETE_TIME, P_TTI_SHOW_OFF, IMDB, REDIRECT_TO, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE, START_IMAGE_URL, UNAUTHORIZED_CALLBACK_TEXT, CHANNEL_ID, CHANNEL_LINK, redirected_env
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

from image.edit_1 import (  # pylint:disable=import-error
    bright,
    mix,
    black_white,
    g_blur,
    normal_blur,
    box_blur,
)
from image.edit_2 import (  # pylint:disable=import-error
    circle_with_bg,
    circle_without_bg,
    sticker,
    edge_curved,
    contrast,
    sepia_mode,
    pencil,
    cartoon,
)
from image.edit_3 import (  # pylint:disable=import-error
    green_border,
    blue_border,
    black_border,
    red_border,
)
from image.edit_4 import (  # pylint:disable=import-error
    rotate_90,
    rotate_180,
    rotate_270,
    inverted,
    round_sticker,
    removebg_white,
    removebg_plain,
    removebg_sticker,
)
from image.edit_5 import (  # pylint:disable=import-error
    normalglitch_1,
    normalglitch_2,
    normalglitch_3,
    normalglitch_4,
    normalglitch_5,
    scanlineglitch_1,
    scanlineglitch_2,
    scanlineglitch_3,
    scanlineglitch_4,
    scanlineglitch_5,
)

BUTTONS = {}
SPELL_CHECK = {}
FILTER_MODE = {}

import datetime
now = datetime.datetime.now()
hour = now.hour

if 0 <= hour <12:
    greeting = "Gᴏᴏᴅ ᴍᴏʀɴɪɴɢ"
elif 12 <= hour <15:
    greeting = 'Gᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ'
elif 15 <= hour <20:
    greeting = 'Gᴏᴏᴅ ᴇᴠᴇɴɪɴɢ'
else:
    greeting = 'Gᴏᴏᴅ ɴɪɢʜᴛ'


@Client.on_message((filters.group | filters.private) & filters.text & ~filters.edited & filters.incoming)
async def give_filter(client, message):
    k = await manual_filters(client, message)
    if k == False:
        await auto_filter(client, message)

# Sticker ID
@Client.on_message(
    filters.private
    & ~filters.forwarded
    & ~filters.command(["start", "about", "help", "id"])
)
async def stickers(bot, msg):
    if msg.sticker:
        await msg.reply(f"This Sticker's ID is⚠️ `{msg.sticker.file_id}`", quote=True)
    

@Client.on_message(filters.command('autofilter'))
async def fil_mod(client, message):
      mode_on = ["yes", "on", "true"]
      mode_of = ["no", "off", "false"]

      try: 
         args = message.text.split(None, 1)[1].lower() 
      except: 
         return await message.reply("**𝙸𝙽𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳...**")
      
      m = await message.reply("**𝚂𝙴𝚃𝚃𝙸𝙽𝙶.../**")

      if args in mode_on:
          FILTER_MODE[str(message.chat.id)] = "True" 
          await m.edit("**𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙴𝙽𝙰𝙱𝙻𝙴𝙳**")
      
      elif args in mode_of:
          FILTER_MODE[str(message.chat.id)] = "False"
          await m.edit("**𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳**")
      else:
          await m.edit("𝚄𝚂𝙴 :- /autofilter on 𝙾𝚁 /autofilter off")

@Client.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client,message):
    group_id = message.chat.id
    name = message.text

    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await message.reply_text(reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await message.reply_text(
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button)
                            )
                    elif btn == "[]":
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or ""
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button)
                        )
                except Exception as e:
                    print(e)
                break 

    else:
        if FILTER_MODE.get(str(message.chat.id)) == "False":
            return
        else:
            await auto_filter(client, message)   

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(UNAUTHORIZED_CALLBACK_TEXT, show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.", show_alert=True)
        return

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    settings = await get_settings(query.message.chat.id)
    pre = 'Chat' if settings['redirect_to'] == 'Chat' else 'files'

    if settings['button']:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}#{query.from_user.id}'
                )
            ] 
            for file in files
        ]
    else:
        btn = [        
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'{pre}#{file.file_id}#{query.from_user.id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'{pre}_#{file.file_id}#{query.from_user.id}',
                )
            ] 
            for file in files
        ]

    btn.insert(0, 
        [
            InlineKeyboardButton(f'♨️ {search} ♨️ ', 'dupe')
        ]
    )
    btn.insert(1,
        [ 
            InlineKeyboardButton(f'ғɪʟᴇs: {len(files)}', 'reqst1'),
            InlineKeyboardButton(f'ᴍᴏᴠɪᴇs', 'dupe'),
            InlineKeyboardButton(f'sᴇʀɪᴇs', 'dupe')
        ]
    )

    if 0 < offset <= 7:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 7
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("ᴘᴀɢᴇs", callback_data="pages"),
             InlineKeyboardButton(f"{round(int(offset) / 10) + 1} / {round(total / 10)}",
                                  callback_data="pages"),
             InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}")]
        )
    elif off_set is None:
        btn.append(
            [
                InlineKeyboardButton("ᴘᴀɢᴇs", callback_data="pages"),
                InlineKeyboardButton(f"{round(int(offset) / 10) + 1} / {round(total / 10)}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data=f"next_{req}_{key}_{n_offset}")]
        )
    else:
        btn.append(
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"{round(int(offset) / 10) + 1} / {round(total / 10)}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    try:
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()


@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("⚠️ Bʀᴏ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ᴏᴡɴ ғɪʟᴇ . Dᴏɴ'ᴛ ʀᴇǫᴜᴇꜱᴛ ᴏᴛʜᴇʀꜱ ғɪʟᴇ 😩", show_alert=True)
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.message_id)
    if not movies:
        return await query.answer("Aʜʜ... Bᴜᴛᴛᴏɴ Exᴘɪʀᴇᴅ Pʟᴇᴀsᴇ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ 🙂", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝙵𝙸𝙻𝙴 𝙾𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴...')
    k = await manual_filters(bot, query.message, text=movie)
    if k == False:
        files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
        if files:
            k = (movie, files, offset, total_results)
            await auto_filter(bot, query, k)
        else:
            k = await query.message.edit('𝚃𝙷𝙸𝚂 𝙼𝙾𝚅𝙸𝙴 I𝚂 𝙽𝙾𝚃 𝚈𝙴𝚃 𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳 𝙾𝚁 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝙳𝙰𝚃𝚂𝙱𝙰𝚂𝙴 💌')
            await asyncio.sleep(10)
            await k.delete()


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return await query.answer('𝗌𝖺𝗇𝗍𝗁𝗈𝗌𝗁𝖺𝗆 𝖺𝗅𝗅𝖾')

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!", show_alert=True)
    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("ʙᴜᴅᴅʏ ᴅᴏɴ'ᴛ ᴛᴏᴜᴄʜ ᴏᴛʜᴇʀs ᴘʀᴏᴘᴇʀᴛʏ 😁", show_alert=True)
    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        act = query.data.split(":")[2]
        hr = await client.get_chat(int(group_id))
        title = hr.title
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}"),
             InlineKeyboardButton("𝙳𝙴𝙻𝙴𝚃𝙴", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')
    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title

        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occurred!!', parse_mode="md")
        return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')
    elif "disconnect" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]

        hr = await client.get_chat(int(group_id))

        title = hr.title
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text(
                f"Some error occurred!!",
                parse_mode="md"
            )
        return await query.answer('Piracy Is Crime')
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text(
                f"Some error occurred!!",
                parse_mode="md"
            )
        return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return await query.answer('𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃')
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert, show_alert=True)
    if query.data.startswith("file"):
        FILE_CHANNEL_ID = int(-1001688529387)
        ident, file_id, rid = query.data.split("#")

        if int(rid) not in [query.from_user.id, 0]:
            return await query.answer(UNAUTHORIZED_CALLBACK_TEXT, show_alert=True)

        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        mention = query.from_user.mention
        f_caption = files.caption
        settings = await get_settings(query.message.chat.id)
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
                                                       
            except Exception as e:
                logger.exception(e)
            f_caption = f_caption
            size = size
            mention = mention
        if f_caption is None:
            f_caption = f"{files.file_name}"
            size = f"{files.file_size}"
            mention = f"{query.from_user.mention}"
        buttons = [
            [
                InlineKeyboardButton('『🎪 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ 🎪』', url='https://t.me/KicchaRequest')
            ]
            ]

        try:
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
                return
            elif settings['botpm']:
                await query.answer(url=f"https://t.me/{temp.U_NAME}?start={ident}_{file_id}")
                return
            else:
               msg = await client.send_cached_media(
                    chat_id=CHANNEL_ID,
                    file_id=file_id,
                    caption=f'<b>{title}</b>\n\n<code>{size}</code>\n\n<code>=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=</code>\n\n<b>{greeting} <spoiler>{query.from_user.mention}</spoiler>✨</b>\n\n<i>Because of copyright this file will be deleted from here within 10 minutesso forward it to anywhere before downloading!</i>\n\n<b><b>🔰 Powered By:<spoiler></b>{query.message.chat.title}</b></spoiler>',
                    protect_content=True if ident == "filep" else False
                    )
            msg1 = await query.message.reply(
                f'<spoiler><b>{query.from_user.mention}</b></spoiler>\n\n'           
                f'<b>Fɪʟᴇ Nᴀᴍᴇ</b>\n<code>[KR.OTT] {title}</code>\n\n'              
                f'<b>Sɪᴢᴇ</b> : <b>{size}</b>\n\n'
                f'<b>Error?<a href={CHANNEL_LINK}>CLICK HERE TO JOIN & TRY AGAIN!</a></b>',
                True,
                'html',
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                     [
                        [
                            InlineKeyboardButton("🔥 GET FILE 🔥", url=f'{msg.link}')
                        ],                       
                        [
                            InlineKeyboardButton("✘ Close ✘", callback_data='close_data')
                        ]
                    ]
                )
            )
            await query.answer('Check Out The Chat',)
            await asyncio.sleep(600)
            await msg1.delete()
            await msg.delete()
            del msg1, msg
        except Exception as e:
            logger.exception(e, exc_info=True)
            await query.answer(f"Encountering Issues", True)

    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("☆ 𝐇𝐄𝐘 𝐈 𝐋𝐈𝐊𝐄 𝐘𝐎𝐔𝐑 𝐒𝐌𝐀𝐑𝐓𝐍𝐄𝐒 ! 𝐁𝐔𝐓 𝐃𝐎𝐍𝐓 𝐁𝐄 𝐎𝐕𝐄𝐑𝐒𝐌𝐀𝐑𝐓 😏", show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            await query.answer(f"🦋 ʜᴇʟʟᴏ ᴍʏ ғʀɪᴇɴᴅ ᴘʟᴇᴀsᴇ sᴇɴᴛ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ 🦋",show_alert=True)
        files = files_[0]
        title = files.file_name
        size = get_size(files.file_size)
        mention = query.from_user.mention
        f_caption = files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption = CUSTOM_FILE_CAPTION.format(file_name='' if title is None else title,
                                                       file_size='' if size is None else size,
                                                       file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption = f_caption
        if f_caption is None:
            f_caption = f"{title}"
        buttons = [
            [
                InlineKeyboardButton('『🎪 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ 🎪』', url='https://t.me/KicchaRequest')
            ]
            ]
      
        await query.answer()
        ms = await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption,
            reply_markup = InlineKeyboardMarkup(buttons),
            protect_content=True if ident == 'checksubp' else False
        )
    elif query.data == "removebg":
        await query.message.edit_text(
            "**Select required mode**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁 𝖶𝗁𝗂𝗍𝖾 𝖡𝖦", callback_data="rmbgwhite"),
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁𝗈𝗎𝗍 𝖡𝖦", callback_data="rmbgplain"),
                ],[
                InlineKeyboardButton(text="𝖲𝗍𝗂𝖼𝗄𝖾𝗋", callback_data="rmbgsticker"),
                ],[
                InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
             ]]
        ),)
    elif query.data == "stick":
        await query.message.edit(
            "**Select a Type**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="stkr"),
                        InlineKeyboardButton(
                            text="𝖤𝖽𝗀𝖾 𝖢𝗎𝗋𝗏𝖾𝖽", callback_data="cur_ved"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="𝖢𝗂𝗋𝖼𝗅𝖾", callback_data="circle_sticker"
                        )
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
                    ],
                ]
            ),
        )
    elif query.data == "rotate":
        await query.message.edit_text(
            "**Select the Degree**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="180", callback_data="180"),
                        InlineKeyboardButton(text="90", callback_data="90"),
                    ],
                    [InlineKeyboardButton(text="270", callback_data="270")],
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
                ]
            ),
        )
    elif query.data == "glitch":
        await query.message.edit_text(
            "**Select required mode**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="normalglitch"
                        ),
                        InlineKeyboardButton(
                            text="𝖲𝖼𝖺𝗇 𝖫𝖺𝗂𝗇𝗌", callback_data="scanlineglitch"
                        ),
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
                    ]
                ]
            ),
        )
    elif query.data == "normalglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="normalglitch1"),
                        InlineKeyboardButton(text="2", callback_data="normalglitch2"),
                        InlineKeyboardButton(text="3", callback_data="normalglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="normalglitch4"),
                        InlineKeyboardButton(text="5", callback_data="normalglitch5"),
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='glitch')
                    ],
                ]
            ),
        )
    elif query.data == "scanlineglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
                        InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
                        InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
                        InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='glitch')
                    ],
                ]
            ),
        )
    elif query.data == "blur":
        await query.message.edit(
            "**Select a Type**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖡𝗈𝗑", callback_data="box"),
                        InlineKeyboardButton(text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="normal"),
                    ],
                    [InlineKeyboardButton(text="𝖦𝖺𝗎𝗌𝗌𝗂𝖺𝗇", callback_data="gas")],
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
                ]
            ),
        )
    elif query.data == "circle":
        await query.message.edit_text(
            "**Select required mode**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖶𝗂𝗍𝗁 𝖡𝖦", callback_data="circlewithbg"),
                        InlineKeyboardButton(text="𝖶𝗂𝗍𝗁𝗈𝗎𝗍 𝖡𝖦", callback_data="circlewithoutbg"),
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')
                    ]
                ]
            ),
        )
    elif query.data == "border":
        await query.message.edit(
            "**Select Border**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖱𝖾𝖽", callback_data="red"),
                        InlineKeyboardButton(text="𝖦𝗋𝖾𝖾𝗇", callback_data="green"),
                    ],
                    [
                        InlineKeyboardButton(text="𝖡𝗅𝖺𝖼𝗄", callback_data="black"),
                        InlineKeyboardButton(text="𝖡𝗅𝗎𝖾", callback_data="blue"),
                    ],
                    [
                        InlineKeyboardButton('⪻ ʙᴀᴄᴋ', callback_data='photo')   
                    ],
                ]
            ),
        )
    elif query.data == "bright":
        await bright(client, query.message)
    elif query.data == "mix":
        await mix(client, query.message)
    elif query.data == "b|w":
        await black_white(client, query.message)
    elif query.data == "circlewithbg":
        await circle_with_bg(client, query.message)
    elif query.data == "circlewithoutbg":
        await circle_without_bg(client, query.message)
    elif query.data == "green":
        await green_border(client, query.message)
    elif query.data == "blue":
        await blue_border(client, query.message)
    elif query.data == "red":
        await red_border(client, query.message)
    elif query.data == "black":
        await black_border(client, query.message)
    elif query.data == "circle_sticker":
        await round_sticker(client, query.message)
    elif query.data == "inverted":
        await inverted(client, query.message)
    elif query.data == "stkr":
        await sticker(client, query.message)
    elif query.data == "cur_ved":
        await edge_curved(client, query.message)
    elif query.data == "90":
        await rotate_90(client, query.message)
    elif query.data == "180":
        await rotate_180(client, query.message)
    elif query.data == "270":
        await rotate_270(client, query.message)
    elif query.data == "contrast":
        await contrast(client, query.message)
    elif query.data == "box":
        await box_blur(client, query.message)
    elif query.data == "gas":
        await g_blur(client, query.message)
    elif query.data == "normal":
        await normal_blur(client, query.message)
    elif query.data == "sepia":
        await sepia_mode(client, query.message)
    elif query.data == "pencil":
        await pencil(client, query.message)
    elif query.data == "cartoon":
        await cartoon(client, query.message)
    elif query.data == "normalglitch1":
        await normalglitch_1(client, query.message)
    elif query.data == "normalglitch2":
        await normalglitch_2(client, query.message)
    elif query.data == "normalglitch3":
        await normalglitch_3(client, query.message)
    elif query.data == "normalglitch4":
        await normalglitch_4(client, query.message)
    elif query.data == "normalglitch5":
        await normalglitch_5(client, query.message)
    elif query.data == "scanlineglitch1":
        await scanlineglitch_1(client, query.message)
    elif query.data == "scanlineglitch2":
        await scanlineglitch_2(client, query.message)
    elif query.data == "scanlineglitch3":
        await scanlineglitch_3(client, query.message)
    elif query.data == "scanlineglitch4":
        await scanlineglitch_4(client, query.message)
    elif query.data == "scanlineglitch5":
        await scanlineglitch_5(client, query.message)
    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)
    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)
    elif query.data == "rmbgsticker":
        await removebg_sticker(client, query.message)
    elif query.data == "pages":
        await query.answer()
    elif query.data == "nihu":
        buttons = [[
        InlineKeyboardButton('✨ ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ᴍᴏʀᴇ ʙᴜᴛᴛᴏɴs ✨', callback_data='start')
   ],[
        InlineKeyboardButton('ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
   ],[
        InlineKeyboardButton('🍁 ᴏᴡɴᴇʀ', callback_data='me'),      
        InlineKeyboardButton('⚙️ ʜᴇʟᴘ', callback_data='help')
   ],[
        InlineKeyboardButton('🔰 ɢᴏ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ 🔰', callback_data='nihu')   
    ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html',
        )
    elif query.data == "start":
        buttons = [[
        InlineKeyboardButton('ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
   ],[
        InlineKeyboardButton('🍁 ᴏᴡɴᴇʀ', callback_data='me'),      
        InlineKeyboardButton('⚙️ ʜᴇʟᴘ', callback_data='help')
   ],[
        InlineKeyboardButton('🔰 ɢᴏ ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ 🔰', callback_data='nihu')   
    ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )

    elif query.data == "photo":
        buttons = [[
            InlineKeyboardButton(text="𝖡𝗋𝗂𝗀𝗍𝗁", callback_data="bright"),
            InlineKeyboardButton(text="𝖬𝗂𝗑𝖾𝖽", callback_data="mix"),
            InlineKeyboardButton(text="𝖡 & 𝖶", callback_data="b|w"),
            ],[
            InlineKeyboardButton(text="𝖢𝗂𝗋𝖼𝗅𝖾", callback_data="circle"),
            InlineKeyboardButton(text="𝖡𝗅𝗎𝗋", callback_data="blur"),
            InlineKeyboardButton(text="𝖡𝗈𝗋𝖽𝖾𝗋", callback_data="border"),
            ],[
            InlineKeyboardButton(text="𝖲𝗍𝗂𝖼𝗄𝖾𝗋", callback_data="stick"),
            InlineKeyboardButton(text="𝖱𝗈𝗍𝖺𝗍𝖾", callback_data="rotate"),
            InlineKeyboardButton(text="𝖢𝗈𝗇𝗍𝗋𝖺𝗌𝗍", callback_data="contrast"),
            ],[
            InlineKeyboardButton(text="𝖲𝖾𝗉𝗂𝖺", callback_data="sepia"),
            InlineKeyboardButton(text="𝖯𝖾𝗇𝖼𝗂𝗅", callback_data="pencil"),
            InlineKeyboardButton(text="𝖢𝖺𝗋𝗍𝗈𝗈𝗇", callback_data="cartoon"),
            ],[
            InlineKeyboardButton(text="𝖨𝗇𝗏𝖾𝗋𝗍", callback_data="inverted"),
            InlineKeyboardButton(text="𝖦𝗅𝗂𝗍𝖼𝗁", callback_data="glitch"),
            InlineKeyboardButton(text="𝖱𝖾𝗆𝗈𝗏𝖾 𝖡𝖦", callback_data="removebg")
            ],[
            InlineKeyboardButton(text="𝙲𝙻𝙾𝚂𝙴 ✘", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)        
        await query.message.edit_text(        
            text="Select your required mode from below!",
            reply_markup=reply_markup,
            parse_mode='html'
        )
        await query.answer('Lᴏᴀᴅɪɴɢ..........')
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('ᴍᴀ-ғɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('ᴀᴜ-ғɪʟᴛᴇʀ', callback_data='autofilter'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct')
            ],[
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tele'),
            InlineKeyboardButton('sᴛɪᴄᴋᴇʀ-ɪᴅ', callback_data='sticker'),
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb')
            ],[
            InlineKeyboardButton('ғɪʟᴇ-sᴛᴏʀᴇ', callback_data='newdata'),
            InlineKeyboardButton('ᴀᴜᴅɪᴏ-ʙᴏᴏᴋ', callback_data='abook'),
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report')
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='eth')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "eth":
        buttons = [[ 
            InlineKeyboardButton('ɢ-ᴛʀᴀɴs', callback_data='gtrans'),
            InlineKeyboardButton('ᴜʀʟ-sʜᴏʀᴛɴᴇʀ', callback_data='urlshort'),
            InlineKeyboardButton('ᴇxᴛʀᴀ', callback_data='extra')
            ],[
            InlineKeyboardButton('sᴏɴɢ', callback_data='songs'),
            InlineKeyboardButton('ᴛᴛs', callback_data='ttss'),
            InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data='video')            
            ],[
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data='image'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purges'),
            InlineKeyboardButton('ᴡʜᴏ-ɪs', callback_data='whois')           
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='prop')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )  
    elif query.data == "prop":
        buttons = [[ 
            InlineKeyboardButton('ᴊsᴏɴᴇ', callback_data='son'),
            InlineKeyboardButton('ᴘᴀsᴛᴇ', callback_data='pastes'),
            InlineKeyboardButton('ᴄᴏᴠɪᴅ', callback_data='corona')
            ],[
            InlineKeyboardButton('ᴋɪᴄᴋ', callback_data='zombies'),
            InlineKeyboardButton('ᴘɪɴɢ', callback_data='pings'),
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='restric')            
            ],[
            InlineKeyboardButton('ғᴜɴ', callback_data='fun'), 
            InlineKeyboardButton('ғᴏɴᴛ', callback_data='fond'),
            InlineKeyboardButton('ᴘɪɴ', callback_data='pin')           
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='eth'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ ✘", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "hellp":
        buttons = [[
            InlineKeyboardButton('ᴍᴀ-ғɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('ᴀᴜ-ғɪʟᴛᴇʀ', callback_data='autofilter'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct')
            ],[
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tele'),
            InlineKeyboardButton('sᴛɪᴄᴋᴇʀ-ɪᴅ', callback_data='sticker'),
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb')
            ],[
            InlineKeyboardButton('ғɪʟᴇ-sᴛᴏʀᴇ', callback_data='newdata'),
            InlineKeyboardButton('ᴀᴜᴅɪᴏ-ʙᴏᴏᴋ', callback_data='abook'),
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report')
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='eth')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "eth":
        buttons = [[ 
            InlineKeyboardButton('ɢ-ᴛʀᴀɴs', callback_data='gtrans'),
            InlineKeyboardButton('ᴜʀʟ-sʜᴏʀᴛɴᴇʀ', callback_data='urlshort'),
            InlineKeyboardButton('ᴇxᴛʀᴀ', callback_data='extra')
            ],[
            InlineKeyboardButton('sᴏɴɢ', callback_data='songs'),
            InlineKeyboardButton('ᴛᴛs', callback_data='ttss'),
            InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data='video')            
            ],[
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data='image'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purges'),
            InlineKeyboardButton('ᴡʜᴏ-ɪs', callback_data='whois')           
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='prop')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )  
    elif query.data == "prop":
        buttons = [[ 
            InlineKeyboardButton('ᴊsᴏɴᴇ', callback_data='son'),
            InlineKeyboardButton('ᴘᴀsᴛᴇ', callback_data='pastes'),
            InlineKeyboardButton('ᴄᴏᴠɪᴅ', callback_data='corona')
            ],[
            InlineKeyboardButton('ᴋɪᴄᴋ', callback_data='zombies'),
            InlineKeyboardButton('ᴘɪɴɢ', callback_data='pings'),
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='restric')            
            ],[
            InlineKeyboardButton('ғᴜɴ', callback_data='fun'), 
            InlineKeyboardButton('ғᴏɴᴛ', callback_data='fond'),
            InlineKeyboardButton('ᴘɪɴ', callback_data='pin')           
            ],[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='eth'),
            InlineKeyboardButton('sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ ✘", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)       
        await query.message.edit_text(                     
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "about":
        await query.message.delete()
        await query.message.reply_sticker(
            'CAACAgQAAxkBAAECr4hiKhTf1qJEeLctIJCsrxk2k5BPmQADEgAC4oetNCxmTn2LSYe8HgQ',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about_menu')
                    ],
                    [
                        InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
                    ]
                ]
            )
        )
    elif query.data == "about_menu":
        buttons = [[
        InlineKeyboardButton('ꜱᴀᴄʜɪɴ ꜱ', url='https://t.me/Sachin_official_admin'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/KicchaRequest'),
        InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.reply(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html',
            disable_web_page_preview=True
        )
    elif query.data == "me":
        buttons= [[
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ', callback_data='owner'),
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.OWNER_TXT2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    
    elif query.data == "owner":
        buttons = [[       
            InlineKeyboardButton('🔰 ɪɴsᴛᴀɢʀᴀᴍ 🔰', url='https://instagram.com'),
            InlineKeyboardButton('🔰 ᴛᴇʟᴇɢʀᴀᴍ 🔰', url='https://t.me/NL_MP4')
        ], [
 
            InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="me"),
            InlineKeyboardButton('ᴄʟᴏsᴇ ✘', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.OWNER_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "movss":
        await query.answer("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ⪼ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ⪼ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ⪼ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴋɢꜰ ᴄʜᴀᴘᴛᴇʀ 2  2022\n\n✘ ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)\n\n© Tʜᴏᴍᴀs Sʜᴇʟʙʏ", show_alert=True)

    elif query.data == "moviis":  
        await query.answer("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ⪼ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ⪼ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ⪼ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ʟᴏᴋɪ S01 E01\n\n✘ ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)\n\n© Tʜᴏᴍᴀs Sʜᴇʟʙʏ", show_alert=True)   
    elif query.data == 'reqst1':
        await query.answer("Hey Bro 😍\n\n🎯 Click On The Button below The Files You Want  ⬇️", show_alert=True)
       
       
    elif query.data == "weather":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.WEATHER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "image":
        buttons= [[
            InlineKeyboardButton(' ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.IMAGE_TXT.format(temp.B_NAME),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "try":
        btn = [[
            InlineKeyboardButton('🔍 ɢᴏᴏɢʟᴇ 🔎', url=f'https://google.com/search?q='),
            InlineKeyboardButton(' 🔍 ʏᴀɴᴅᴇx 🔎', url=f'https://yandex.com/search?text=')
        ],[
            InlineKeyboardButton("🇺🇸 ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴏ ᴇɴɢʟɪꜱʜ 🇺🇸", callback_data="mmmm")
        ]] 
        await query.message.edit_text(script.MALAYALMSPELL_TXT, reply_markup=InlineKeyboardMarkup(btn))
    elif query.data == "mmmm":
        btn = [[
            InlineKeyboardButton('🔍 ɢᴏᴏɢʟᴇ 🔎', url=f'https://google.com/search?q='),
            InlineKeyboardButton(' 🔍 ʏᴀɴᴅᴇx 🔎', url=f'https://yandex.com/search?text=')
        ],[
            InlineKeyboardButton("🇮🇳 ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴏ ᴍᴀʟᴀʏᴀʟᴀᴍ 🇮🇳", callback_data="try")
        ]] 
        await query.message.edit_text(script.ENGLISHSPELL_TXT, reply_markup=InlineKeyboardMarkup(btn))
        
    elif query.data == "whois":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.WHOIS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "urlshort":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.URLSHORT_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "zombies":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ZOMBIES_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "fun":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FUN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "video":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='song')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VIDEO_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "pin":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "son":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.JSON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "pastes":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PASTE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "pings":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PINGS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "ttss":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TTS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "purges":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.PURGE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "tele":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.TELE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )         
    elif query.data == "fond":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FOND_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "cntry":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.CNTRY_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "source":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.delete()
        await query.message.reply(
                text=script.SOURCE_TXT,
                reply_markup=reply_markup,
                parse_mode='html'
            )
    elif query.data == "gtrans":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.GTRANS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "urlshrt":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.SHORT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "trnt":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.TRNT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "tts":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.TTS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "mute":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.MUTE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "tts":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.TTS_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "song":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.SONG_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "json":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.JSON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "covid":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.COVID_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )         
    elif query.data == "ping":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.PING_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "fun":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.FUN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "ban":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BAN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "purge":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.PURGE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "tgraph":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.TGRAPH_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )       
    elif query.data == "info":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.INFO_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "imbd":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.IMBD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "hud":
        buttons = [[
            InlineKeyboardButton('𝖠𝗎𝗍𝗈', callback_data='autofilter'),
            InlineKeyboardButton('𝖬𝖺𝗇𝗎𝖺𝗅', callback_data='manual')
            ],[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help'),
            InlineKeyboardButton('𝖢𝗅𝗈𝗌𝖾', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.FILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "manual":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='hud'),
            InlineKeyboardButton('𝖡𝗎𝗍𝗍𝗈𝗇', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='manual')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "paste":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.PASTE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='hud')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "pin":
        buttons = [[
            InlineKeyboardButton('𝖡𝖺𝖼𝗄', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.PIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "restric":
        buttons = [[
            InlineKeyboardButton('🔙 Back', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        await query.message.edit_text(
            text=script.RESTRIC_TXT,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "fil":
        await query.answer("This movie have total : {total_results} ", show_alert=True
        )
    elif query.data == "reason":
        await query.answer("""I couldn't find the file you requested 😕
Try to do the following...

=> Request with correct spelling

=> Don't ask movies that are not released in OTT platforms

=> Try to ask in [MovieName, Language] this format.

=> Search on Google 😌""", show_alert=True
        )
    elif query.data == "tip":
        await query.answer("""=> Ask with Correct Spelling
=> Don't ask movie's those are not released in OTT 🤧
=> For better results :
      - Movie name language
      - Eg: Solo Malayalam""", show_alert=True
        )
    elif query.data == "so":
        await query.answer(f"""🏷 Title: {search} 
🎭 Genres: {genres} 
📆 Year: {year} 
🌟 Rating: {rating} 
☀️ Languages : {languages} 
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date} 
""",show_alert=True
       )
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help'),
            InlineKeyboardButton('Refresh ⧖', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.reply_chat_action("typing")
        m=await query.message.reply_text("◈◇◇")
        await asyncio.sleep(2)
        n=await m.edit("◈◈◇")
        await asyncio.sleep(2)
        o=await n.edit("◈◈◈")
        await asyncio.sleep(2)
        await o.delete()
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "rfrsh":
        await query.answer("Fetching MongoDb DataBase")
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help'),
            InlineKeyboardButton('Refresh ⧖', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data.startswith("setgs"):
        ident, set_type, status, grp_id = query.data.split("#")
        grpid = await active_connection(str(query.from_user.id))

        if str(grp_id) != str(grpid):
            await query.message.edit("Your Active Connection Has Been Changed. Go To /settings.")
            return await query.answer('Piracy Is Crime')

        if status == "True" or status == "Chat":
            await save_group_settings(grpid, set_type, False)
        else:
            await save_group_settings(grpid, set_type, True)

        settings = await get_settings(grpid)

        if settings is not None:
            buttons = [
                [
                    InlineKeyboardButton('Filter Button',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}'),
                    InlineKeyboardButton('Single' if settings["button"] else 'Double',
                                         callback_data=f'setgs#button#{settings["button"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton( 'Redirect To',
                                         callback_data=f'setgs#redirect_to#{settings["redirect_to"]}#{grp_id}',),
                    InlineKeyboardButton('👤 PM' if settings["redirect_to"] == "PM" else '📄 Chat',
                                         callback_data=f'setgs#redirect_to#{settings["redirect_to"]}#{grp_id}',),
                ],
                [
                    InlineKeyboardButton('Bot PM', callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✅ Yes' if settings["botpm"] else '❌ No',
                                         callback_data=f'setgs#botpm#{settings["botpm"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('File Secure',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✅ Yes' if settings["file_secure"] else '❌ No',
                                         callback_data=f'setgs#file_secure#{settings["file_secure"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('IMDB', callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✅ Yes' if settings["imdb"] else '❌ No',
                                         callback_data=f'setgs#imdb#{settings["imdb"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Spell Check',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✅ Yes' if settings["spell_check"] else '❌ No',
                                         callback_data=f'setgs#spell_check#{settings["spell_check"]}#{str(grp_id)}')
                ],
                [
                    InlineKeyboardButton('Welcome', callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}'),
                    InlineKeyboardButton('✅ Yes' if settings["welcome"] else '❌ No',
                                         callback_data=f'setgs#welcome#{settings["welcome"]}#{str(grp_id)}')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_reply_markup(reply_markup)
    elif query.data == "close":
        await query.message.delete()
    elif query.data == 'tips':
        await query.answer("sᴇɴᴅ ᴄᴏʀʀᴇᴄᴛ ᴍᴏᴠɪᴇ/sᴇʀɪᴇs ɴᴀᴍᴇ ғᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛs .\nᴛᴏ ɢᴇᴛ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛ ғᴏʀ sᴇʀɪᴇs sᴇᴀʀᴄʜ ʟɪᴋᴇ ᴇxᴀᴍᴘʟᴇ ɢɪᴠᴇɴ, Eg - Peaky Blinders S01E01\n\n © 𝖥𝖨𝖫𝖤𝖲𝖤𝖠𝖱𝖢𝖧𝗑𝖡𝖮𝖳", True)
    try: await query.answer('Your Results are there in Filter Button') 
    except: pass


async def auto_filter(client, msg: pyrogram.types.Message, spoll=False):
    if not spoll:
        message = msg
        settings = await get_settings(message.chat.id)
        if message.text.startswith("/"): return  # ignore commands
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if 2 < len(message.text) < 100:
            search = message.text
            files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
            if not files:
                if settings["spell_check"]:
                    return await advantage_spell_chok(msg)
                else:
                    return
        else:
            return
    else:
        settings = await get_settings(msg.message.chat.id)
        message = msg.message.reply_to_message  # msg will be callback query
        search, files, offset, total_results = spoll
    
    pre = 'filep' if settings['file_secure'] else 'file'
    pre = 'Chat' if settings['redirect_to'] == 'Chat' else pre

    if settings["button"]:
        btn = [
            [
                InlineKeyboardButton(
                        text=f"[{get_size(file.file_size)}] {file.file_name}", 
                        callback_data=f'{pre}#{file.file_id}#{msg.from_user.id if msg.from_user is not None else 0}'
                )
            ] 
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'{pre}#{file.file_id}#{msg.from_user.id if msg.from_user is not None else 0}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'{pre}_#{file.file_id}#{msg.from_user.id if msg.from_user is not None else 0}',
                )
            ]
            for file in files
        ]

    btn.insert(0, 
        [
            InlineKeyboardButton(f'♨️ {search} ♨️ ', 'dupe')
        ]
    )
    btn.insert(1,
        [
            InlineKeyboardButton(f'ᴍᴏᴠɪᴇs', 'dupe'),
            InlineKeyboardButton(f'sᴇʀɪᴇs', 'dupe'),
            InlineKeyboardButton(f'ᴛɪᴘs', 'tips')
        ]
    )

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [InlineKeyboardButton(text=f" 1/{round(int(total_results) / 10)}", callback_data="pages"),
             InlineKeyboardButton(text="ɴᴇxᴛ", callback_data=f"next_{req}_{key}_{offset}")]
        )
    else:
        btn.append(
            [InlineKeyboardButton(text=" 1/1", callback_data="pages")]
        )
    imdb = await get_poster(search, file=(files[0]).file_name) if settings["imdb"] else None
    TEMPLATE = settings['template']
    if imdb:
        cap = TEMPLATE.format(
            query=search,
            requested = message.from_user.mention,
            mention_bot=temp.MENTION,
            mention_user=message.from_user.mention if message.from_user else message.sender_chat.title,
            title=imdb['title'],
            votes=imdb['votes'],
            aka=imdb["aka"],
            seasons=imdb["seasons"],
            box_office=imdb['box_office'],
            localized_title=imdb['localized_title'],
            kind=imdb['kind'],
            imdb_id=imdb["imdb_id"],
            cast=imdb["cast"],
            runtime=imdb["runtime"],
            countries=imdb["countries"],
            certificates=imdb["certificates"],
            languages=imdb["languages"],
            director=imdb["director"],
            writer=imdb["writer"],
            producer=imdb["producer"],
            composer=imdb["composer"],
            cinematographer=imdb["cinematographer"],
            music_team=imdb["music_team"],
            distributors=imdb["distributors"],
            release_date=imdb['release_date'],
            year=imdb['year'],
            genres=imdb['genres'],
            poster=imdb['poster'],
            plot=imdb['plot'],
            rating=imdb['rating'],
            url=imdb['url'],
            **locals()
        )
    else:
        cap = f"<b><i>📀 ᴛɪᴛʟᴇ :  : {search}\n🗣️ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}\n🦋 ɢʀᴏᴜᴘ 🦋: {message.chat.title}</i></b>"
    if imdb and imdb.get('poster'):
        try:
            await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024],
                                      reply_markup=InlineKeyboardMarkup(btn))
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=poster, caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            logger.exception(e)
            await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    if spoll:
        await msg.message.delete()
        
async def advantage_spell_chok(msg):
    query = re.sub(
        r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e|a)?(l)*(o)*|mal(ayalam)?|t(h)?amil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(u)?(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle(s)?)",
        "", msg.text, flags=re.IGNORECASE)  # plis contribute some common words
    query = query.strip() + " movie"
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        btn = [[
            InlineKeyboardButton('🔍 ɢᴏᴏɢʟᴇ 🔎', url=f'https://google.com/search?q='),
            InlineKeyboardButton(' 🔍 ʏᴀɴᴅᴇx 🔎', url=f'https://yandex.com/search?text=')
        ],[
            InlineKeyboardButton("🇮🇳 ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴏ ᴍᴀʟᴀʏᴀʟᴀᴍ 🇮🇳", callback_data="try")
        ]]        
        k=await msg.reply_photo(photo="https://telegra.ph/file/4bb1968bd091453b0070c.jpg", caption=script.ENGLISHSPELL_TXT, reply_markup=InlineKeyboardMarkup(btn))    
        await asyncio.sleep(40)
        await k.delete()
        await msg.delete()
        return

    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE)  # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(
        r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)',
        '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*",
                         re.IGNORECASE)  # match something like Watch Niram | Amazon Prime
        for mv in g_s:
            match = reg.match(mv)
            if match:
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed))  # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True)  # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist))  # removing duplicates
    if not movielist:
        btn = [[
            InlineKeyboardButton('🔍 ɢᴏᴏɢʟᴇ 🔎', url=f'https://google.com/search?q='),
            InlineKeyboardButton(' 🔍 ʏᴀɴᴅᴇx 🔎', url=f'https://yandex.com/search?text=')
        ],[
            InlineKeyboardButton("🇮🇳 ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴏ ᴍᴀʟᴀʏᴀʟᴀᴍ 🇮🇳", callback_data="try")
        ]]           
        k=await msg.reply_photo(photo="https://telegra.ph/file/4bb1968bd091453b0070c.jpg", caption=script.ENGLISHSPELL_TXT, reply_markup=InlineKeyboardMarkup(btn))    
        await asyncio.sleep(40)
        await k.delete()
        await msg.delete()
        return

    SPELL_CHECK[msg.message_id] = movielist
    btn = [[
        InlineKeyboardButton('🔍 ɢᴏᴏɢʟᴇ 🔎', url=f'https://google.com/search?q='),
        InlineKeyboardButton(' 🔍 ʏᴀɴᴅᴇx 🔎', url=f'https://yandex.com/search?text=')
    ],[
        InlineKeyboardButton("🇮🇳 ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴏ ᴍᴀʟᴀʏᴀʟᴀᴍ 🇮🇳", callback_data="try")
    ]]
    k=await msg.reply_photo(photo="https://telegra.ph/file/4bb1968bd091453b0070c.jpg", caption=script.ENGLISHSPELL_TXT, reply_markup=InlineKeyboardMarkup(btn))    
    await asyncio.sleep(40)
    await k.delete()
    await msg.delete()
    return

        

async def manual_filters(client, message, text=False):
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await client.send_message(group_id, reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await client.send_message(
                                group_id,
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id=reply_id
                            )
                    elif btn == "[]":
                        await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id=reply_id
                        )
                    else:
                        button = eval(btn)
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id=reply_id
                        )
                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False
