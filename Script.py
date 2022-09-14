class script(object):
    START_TXT = """<u><i>Hello 👋 {}. 𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎 🙌</i></u>
<u><i>I'm <p>𝗣𝗿𝗮𝗯𝗵𝗮𝘀</p> or You Can Call me as  <a href="https://t.me/Prabhas_autofilterBOT"> 𝗣𝗿𝗮𝗯𝗵𝗮𝘀 𝗔𝘂𝘁𝗼𝗳𝗶𝗹𝘁𝗲𝗿 𝗯𝗼𝘁</a> 😍.</i></u>

<u><i>I Can Provide Movies In Your Group, It Very Easy Way Just Add Me To Your Group And Make Me Admin In Your Group, Thars all I'll Provide Movies From Your Group.</i></u>

<u><i>To Use Me In PM Use The /connect Command In Your Group And You Can Modify AutoFilter Settings & Other Feature Settings</i></u>,
    m = datetime.datetime.now()

    time = m.hour

    if time < 12:
        get="Good Morning"
    elip time < 15:
          get="Good Afternoon"
    elip time < 20:
          get="Good Evening"
    else:
        get="Good Night"

text = f " " "
{message.from_user.mention}
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>,  𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 𝙰𝙽𝙳 𝚂𝙴𝚁𝙸𝙴𝚂🤩, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍

⚠️ 𝙼𝚘𝚛𝚎 𝙷𝚎𝚕𝚙 𝙲𝚑𝚎𝚌𝚔 𝙷𝚎𝚕𝚙 𝙱𝚞𝚝𝚝𝚘𝚗 𝙱𝚎𝚕𝚘𝚠

©️Creator <a href=https://t.me/Sachin_official_admin>Sachin S </a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    OWNER_TXT2 = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : 𝐒𝐚𝐜𝐡𝐢𝐧 𝐒
• ᴜꜱᴇʀɴᴀᴍᴇ : ᚜ a href=https://t.me/Sachin_official_admin><b>𝚂𝚊𝚌𝚑𝚒𝚗 𝚂</b></a> ᚛

⍟───[ 💕 sᴘᴇᴄɪᴀʟ ᴛʜᴀɴᴋs 💕 ]───⍟

• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴅᴇᴠ ᴋʀɪsʜɴᴀ ᴀᴊɪᴛʜ
• ᴜꜱᴇʀɴᴀᴍᴇ : <a href=https://t.me/Sachin_official_admin>ꜱᴀᴄʜɪɴ ꜱ</a></b>"""
    OWNER_TXT = """<b>🇮🇳 ʜᴇʀᴇ ᴛᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ 🇮🇳</b>"""
    ENGLISHSPELL_TXT = "<i><b>𝐇𝐞𝐥𝐥𝐨 𝐈 𝐜𝐨𝐮𝐥𝐝 𝐧𝐨𝐭 𝐟𝐢𝐧𝐝 𝐭𝐡𝐞 𝐦𝐨𝐯𝐢𝐞 𝐲𝐨𝐮 𝐚𝐬𝐤𝐞𝐝 𝐟𝐨𝐫 🥴</b>\n\n<b>𝐆𝐨𝐨𝐠𝐥𝐞, 𝐘𝐚𝐧𝐝𝐞𝐱 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 𝐚𝐧𝐲 𝐛𝐮𝐭𝐭𝐨𝐧 𝐚𝐧𝐝 𝐟𝐢𝐧𝐝 𝐭𝐡𝐞 <u>𝐂𝐎𝐑𝐑𝐄𝐂𝐓 𝐌𝐎𝐕𝐈𝐄 𝐍𝐀𝐌𝐄</u> 𝐚𝐧𝐝 𝐞𝐧𝐭𝐞𝐫 𝐢𝐭 𝐡𝐞𝐫𝐞 𝐛𝐮𝐭 𝐭𝐡𝐞 𝐦𝐨𝐯𝐢𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 🙃\n\n𝐈𝐟 𝐲𝐨𝐮 𝐝𝐨 𝐧𝐨𝐭 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐦𝐨𝐯𝐢𝐞 𝐞𝐯𝐞𝐧 𝐚𝐟𝐭𝐞𝐫 𝐞𝐧𝐭𝐞𝐫𝐢𝐧𝐠 𝐭𝐡𝐞 𝐜𝐨𝐫𝐫𝐞𝐜𝐭 𝐧𝐚𝐦𝐞 ...</b> <𝐜𝐨𝐝𝐞>@admin 𝐭𝐲𝐩𝐞 𝐦𝐨𝐯𝐢𝐞 𝐧𝐚𝐦𝐞 <b>𝐈𝐧𝐟𝐨𝐫𝐦 𝐭𝐡𝐞 𝐚𝐝𝐦𝐢𝐧 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐟𝐨𝐫𝐦𝐚𝐭 .. 𝐖𝐞 𝐰𝐢𝐥𝐥 𝐮𝐩𝐥𝐨𝐚𝐝 𝐰𝐢𝐭𝐡𝐢𝐧 𝟐𝟒 𝐡𝐨𝐮𝐫𝐬 😇</b></i>"
    MALAYALMSPELL_TXT = "<i><b>ഹലോ നിങ്ങൾ ആവശ്യപ്പെട്ട ഈ സിനിമ എനിക്ക് കണ്ടെത്താൻ കഴിഞ്ഞില്ല 🥴 ...\n\nGoogle, Yandex ഏതെങ്കിലും ഒരു ബട്ടണിൽ ക്ലിക്ക് ചെയ്ത് ശരിയായ സിനിമയുടെ പേര് കണ്ടെത്തി ഇവിടെ നൽകുക എന്നാലേ സിനിമ / സീരിയസ് കിട്ടുകയുള്ളു 🙂...\n\nശരിയായ പേര് നൽകിയിട്ടും നിങ്ങൾക്ക് സിനിമ ലഭിക്കുന്നില്ലെങ്കിൽ ...</b> <code>@admin query</code>  <b>ഈ ഫോർമാറ്റിൽ അഡ്മിനെ അറിയിക്കുക .. ഞങ്ങൾ 24 മണിക്കൂറിനുള്ളിൽ അപ്‌ലോഡ്  ചെയ്യും 😇</b></i>"

    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 

›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ a href=https://t.me/Sachin_official_admin><b>𝚂𝚊𝚌𝚑𝚒𝚗 𝚂</b></a> ᚛━━━━━━━━━━━━

›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ a href=https://t.me/Sachin_official_admin><b>𝚂𝚊𝚌𝚑𝚒𝚗 𝚂</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ a href=https://t.me/Sachin_official_admin><b>𝚂𝚊𝚌𝚑𝚒𝚗 𝚂</b></a> ᚛━━━━━━━━━━━━""" 
    ABOUT_TXT = """
○ 𝖬𝗒 𝖭𝖺𝗆e : ᴘʀᴀʙʜᴀꜱ
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/Sachin_official_admin'>ꜱᴀᴄʜɪɴ ꜱ</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : ᴘʏᴛʜᴏɴ 𝟥 
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : ᴘʏʀᴏɢʀᴀᴍ ᴀꜱʏɴᴄɪᴏ 𝟢.𝟣𝟩.𝟣 
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com'>ᴍᴏɴɢᴏᴅʙ</a>
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : 𝖵9.8 [BeTa]
"""
    ADMINS_TXT = """ʜᴇʏ ʙʀᴏ,
My name is 𝙿𝚛𝚊𝚋𝚑𝚊𝚜
- My Admins are:
- @sachin_official_admin

<b>♻️GROUP♻️:</b>
- <a href=https://t.me/KicchaRequest>Support Group</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and LUCIFER will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Prabhas should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Nᴀʀᴜᴛᴏ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/KicchaRequest)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /donate - <code>to donate any gifts for my owner</code>"""
    STATUS_TXT = """<b>⍟───[ 📈 ʙᴏᴛ sᴛᴀᴛᴜs 📉]───⍟\n
📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code> MB</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
