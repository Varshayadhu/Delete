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
    GTRANS_TXT = """<b>𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝗈𝗋</b>
- 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /tr [language code][reply] - 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾.
"""
    PASTE_TXT = """<b>𝖯𝖺𝗌𝗍𝖾</b>
- 𝖯𝖺𝗌𝗍𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍𝗌 𝗈𝗋 𝖽𝗈𝖼𝗎𝗆𝖾𝗇𝗍𝗌 𝗈𝗇 𝖺 𝗐𝖾𝖻𝗌𝗂𝗍𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /paste [text] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗀𝗂𝗏𝖾𝗇 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
- /paste [reply] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
"""
    STICK_TXT = """<b>𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖣</b>
- 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗂𝗌 𝗎𝗌𝖾𝖽 𝗍𝗈 𝗀𝖾𝗍 𝖺 𝖨𝖣 𝗈𝖿 𝖺𝗇 𝗌𝗍𝗂𝖼𝗄𝖾𝗋
<b>Command</b>
- /stickerid - 𝖦𝖾𝗍 𝖨𝖣
"""
    TTS_TXT = """<b>TEXT TO SPEACH</b>
Simple Telegram Text-To-Speech Module.
It can use the following as speech synthesis engines:

Amazon's Polly engine
Google's TTS engine by way of the gTTS library
"""
    JSON_TXT = """<b>𝖩𝗌𝗈𝗇:</b>
𝖡𝗈𝗍 𝗋𝖾𝗍𝗎𝗋𝗇𝗌 𝗃𝗌𝗈𝗇 𝖿𝗈𝗋 𝖺𝗅𝗅 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝗐𝗂𝗍𝗁 /json. 
<b>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:</b>
𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗍𝗂𝗇𝗀 JSON
𝖯𝗆 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 
𝖦𝗋𝗈𝗎𝗉 𝖲𝗎𝗉𝗉𝗈𝗋𝗍
"""
    FUN_TXT ="""<b>𝖥𝗎𝗇 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b> 
    
<b>🎲 𝖭𝗈𝗍𝗁𝗂𝗇𝗀 𝗆𝗎𝖼𝗁 𝗃𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝖿𝗎𝗇 𝗌𝗍𝗎𝖿𝖿𝗌</b>
𝗍𝗋𝗒 𝗍𝗁𝖾𝗌𝖾 𝗈𝗎𝗍: 
𝟣. /dice - 𝖱𝗈𝗅𝗅 𝗍𝗁𝖾 𝖽𝗂𝖼𝖾
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝗍𝗁𝗋𝗈𝗐 𝖺 𝖽𝖺𝗋𝗍
3. /Runs - 𝖩𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝗋𝖺𝗇𝖽𝗈𝗆 𝖽𝖺𝗂𝗅𝗈𝗎𝗀𝖾𝗌
4. /Goal or /Shoot - 𝖳𝗈 𝗀𝗈𝖺𝗅 𝗈𝗋 𝗌𝗁𝗈𝗈𝗍 𝖺 𝖻𝖺𝗅𝗅
"""
    PURGE_TXT ="""<b>𝖯𝗎𝗋𝗀𝖾</b>
- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺 𝗅𝗈𝗍𝗌 𝗈𝖿 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝖺 𝗀𝗋𝗈𝗎𝗉!
    
 <b>𝖠𝖽𝗆𝗂𝗇</b> 
◉ /purge :- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈, 𝖳𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
    """
    MANUELFILTER_TXT = """<b>𝖥𝗂𝗅𝗍𝖾𝗋𝗌</b>
𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 
<b>𝖭𝖮𝖳𝖤:</b>
𝟣. 𝖻𝗈𝗍 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾 𝗂𝗇 𝗈𝗋𝖽𝖾𝗋 𝗍𝗈 𝗋𝖾𝗉𝗅𝗒 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟤. 𝗈𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍. 
𝟥. 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖽𝗈𝖾𝗌 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇𝗌, 𝗆𝖾𝖽𝗂𝖺𝗌 𝖺𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌. 
𝟦. 𝖺𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝖺𝗋𝖾 𝖺𝗅𝗌𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝗐𝗂𝗍𝗁 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 𝟨𝟦 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌. 
𝟧. 𝗍𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝗌𝗈𝗆𝖾 𝖾𝖺𝗌𝗍𝖾𝗋 𝖾𝗀𝗀𝗌, 𝗍𝗋𝗒 𝗍𝗈 𝖿𝗂𝗇𝖽 𝗂𝗍 𝗈𝗎𝗍. 
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
/filter  𝗈𝗋 /add - 𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋
/filters 𝗈𝗋 /viewfilters - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍 
/stop 𝗈𝗋 /del - 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 (𝗌𝖾𝗉𝖺𝗋𝖺𝗍𝖾 𝗄𝖾𝗒𝗐𝗈𝗋𝖽𝗌 𝗐𝗂𝗍𝗁 𝗌𝗉𝖺𝖼𝖾𝗌 𝖿𝗈𝗋 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝖺𝗍 𝖺 𝗍𝗂𝗆𝖾) 
/stopall 𝗈𝗋 /delall - 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)
"""
    SONG_TXT = """<b>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗈𝖽𝗎𝗅𝖾</b>
- 𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺 𝗌𝗈𝗇𝗀, 𝖽𝗈𝗇'𝗍 𝗌𝖾𝖺𝗋𝖼𝗁 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝖻𝗈𝗍 𝗁𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖺𝗅𝗅 𝗂𝗇 𝗈𝗇𝖾 𝖻𝗈𝗍
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽</b>
- /song [Song Name] - 𝖳𝗈 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗌𝗈𝗇𝗀
<b>Usage</b>
- 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒 𝗈𝗇𝖾
- 𝖶𝗈𝗋𝗄𝗌 𝗈𝗇𝗅𝗒 𝗂𝗇 𝖻𝗈𝗍𝗌 𝗉𝗆
<b>𝖡𝗎𝗀</b>
𝖲𝗈𝗆𝖾𝗍𝗂𝗆𝖾𝗌 𝗂𝗍 𝗐𝗂𝗅𝗅 𝗌𝗁𝗈𝗐 𝖺𝗇 𝖾𝗋𝗋𝗈𝗋!
"""
    MUTE_TXT = """<b>𝖬𝗎𝗍𝖾:</b>

𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 Muted; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   

<b> 𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /mute - 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 
- /tmute - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unmute - 𝖴𝗇mute 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
- 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tmute @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁
"""
    CNTRY_TXT = """Use /Country (Country name)
- Get info about Country 
"""
    TRNT_TXT = """This feature will be added soon"""
    SHORT_TXT = """To Short your big urls
- Command /Short Link 
"""
    BUTTON_TXT = """Help: <b>𝖡𝗎𝗍𝗍𝗈𝗇𝗌</b>
𝖳𝗈𝗏𝗂𝗇𝗈 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌, 𝗇𝗈𝗐 𝗅𝖾𝗍𝗌 𝗌𝖾𝖾 𝗁𝗈𝗐 𝗍𝗈 𝗂𝗆𝗉𝗅𝖾𝗆𝖾𝗇𝗍 𝗂𝗍. 
<b>𝖭𝖡:</b>
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒. 
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾. 
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖿𝗈𝗋𝗆𝖺𝗍𝗍𝖾𝖽 𝖺𝗌 𝖻𝖾𝗅𝗈𝗐 𝗈𝗋 𝖾𝗅𝗌𝖾 𝗋𝖾𝗌𝗎𝗅𝗍 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗆𝖺𝗅𝖿𝗈𝗋𝗆𝖾𝖽. 
<b>𝖴𝖱𝖫 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
- 𝗌𝗂𝗇𝗀𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅:https://𝗍.𝗆𝖾/DK_BOTx)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅:https://𝗍.𝗆𝖾/DKBOTXCHATS)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅:https://𝗍.𝗆𝖾/TovinoBotV3)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗂𝗇 𝖲𝖺𝗆𝖾 𝖱𝖺𝗐 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅:https://𝗍.𝗆𝖾/aboutme_DK)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅:https://𝗍.𝗆𝖾/vloggerdeven_TG:𝗌𝖺𝗆𝖾)</code>
<b>𝖠𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝖺𝗅𝖾𝗋𝗍:𝗍𝗁𝗂𝗌 𝗂𝗌 𝖺𝗇 𝖺𝗅𝖾𝗋𝗍!)</code>
"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>
<b>𝖭𝗈𝗍𝖾:</b>
𝟣. 𝖬𝖺𝗄𝖾 𝗆𝖾 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗂𝖿 𝗂𝗍'𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾. 
𝟤. 𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖽𝗈𝖾𝗌 𝗇𝗈𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖼𝖺𝗆 𝗋𝗂𝗉, 𝗉𝗈𝗋𝗇 𝖺𝗇𝖽 𝖿𝖺𝗄𝖾 𝖿𝗂𝗅𝖾𝗌. 
𝟥. 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝗍𝗁𝖾 𝗅𝖺𝗌𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗆𝖾 𝗐𝗂𝗍𝗁 𝗊𝗎𝗈𝗍𝖾𝗌.  𝖨'𝗅𝗅 𝖺𝖽𝖽 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗆𝗒 𝖽𝖻.
"""
    CONNECTION_TXT = """<b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>
𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝗐𝗁𝗂𝖼𝗁 𝗅𝖾𝗍 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗍𝗈 𝖾𝗑𝖾𝖼𝗎𝗍𝖾 𝖻𝗈𝗍𝗁 𝗇𝗈𝗋𝗆𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗌𝗈𝗆𝖾 𝗈𝗍𝗁𝖾𝗋 𝗌𝖾𝗇𝗌𝗂𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗋𝗂𝗀𝗁𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖯𝖬 𝗍𝗁𝖺𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝖿𝗅𝖾𝖼𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉 𝗐𝗁𝗂𝖼𝗁 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋 𝖺𝖽𝖽𝗂𝗍𝗂𝗈𝗇𝗌 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗌𝗍𝗎𝖿𝖿𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝗉𝗋𝖾𝗏𝖾𝗇𝗍 𝖿𝗅𝗈𝗈𝖽𝗂𝗇𝗀. 
𝖭𝖮𝖳𝖤:
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇. 
𝟤. 𝖨𝗇 𝖺 𝖼𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗂𝗆𝗉𝗅𝗒 𝗎𝗌𝖾 𝗍𝗁𝖾 /connect 𝖿𝗈𝗋 𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇  
𝟥. 𝖨𝗇 𝖯𝖬 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝖼𝗁𝖺𝗍 𝗂𝖽 𝗋𝗂𝗀𝗁𝗍 𝖺𝖿𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽. 
𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾: 
/connect - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬 
/disconnect  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍 
/connections - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌

"""
    FILTER_TXT ="""𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗍𝗒𝗉𝖾 𝖻𝖾𝗅𝗈𝗐:"""
    PIN_TXT = """<b>𝖯𝖨𝖭:</b>
𝖠𝗅𝗅 𝗍𝗁𝖾 𝗉𝗂𝗇 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝖿𝗈𝗎𝗇𝖽 𝗁𝖾𝗋𝖾; 𝗄𝖾𝖾𝗉 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝗎𝗉 𝗍𝗈 𝖽𝖺𝗍𝖾 𝗈𝗇 𝗍𝗁𝖾 𝗅𝖺𝗍𝖾𝗌𝗍 𝗇𝖾𝗐𝗌 𝗐𝗂𝗍𝗁 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾!  

<b>𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b> 
- /pin: 𝖯𝗂𝗇 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗒𝗈𝗎 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖺 𝗇𝗈𝗍𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝗍𝗈 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋𝗌. 
- /unpin: 𝖴𝗇𝗉𝗂𝗇 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾. 𝖨𝖿 𝗎𝗌𝖾𝖽 𝖺𝗌 𝖺 𝗋𝖾𝗉𝗅𝗒, 𝗎𝗇𝗉𝗂𝗇𝗌 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.
"""
    TGRAPH_TXT ="""<b>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁</b>
𝖣𝗈 𝖺𝗌 𝗒𝗈𝗎 𝗐𝗂𝗌𝗁 𝗐𝗂𝗍𝗁 telegra.ph 𝗆𝗈𝖽𝗎𝗅𝖾!
<b>𝖴𝗌𝖺𝗀𝖾:</b>

- /telegraph - 𝖲𝖾𝗇𝖽 𝗆𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)

<b>𝖭𝖮𝖳𝖤:</b>
• 𝖳𝗈𝗏𝗂𝗇𝗈 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗂𝗇 𝗀𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝗉𝗆𝗌
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾
"""
    IMBD_TXT ="""<b>Search</b>
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖿𝗂𝗅𝗆 𝖽𝖾𝗍𝖺𝗂𝗅𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
<b>U𝗌𝖺𝗀𝖾:</b>
- /imdb - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾
- /search - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌
"""
    COVID_TXT = """<b><u>𝖢𝗈𝗏𝗂𝖽 19 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇</u><b/>
𝖢𝗈𝗋𝗈𝗇𝖺 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 / 𝖳𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾 𝖼𝗈𝗏𝗂𝖽 𝗂𝗇𝖿𝗈 𝗈𝖿 𝖺𝗇𝗒 𝖼𝗈𝗎𝗇𝗍𝗋𝗒            
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽:</b>
/covid [country name] - 𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒
<b>𝖴𝗌𝖺𝗀𝖾</b>
- 𝖢𝗈𝗎𝗅𝖽 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌
"""
    INFO_TXT ="""<b>𝖨𝗇𝖿𝗈</b>
𝖦𝖾𝗍 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀!
<b>𝖴𝗌𝖺𝗀𝖾:</b>
➥ /id - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋
➥ /info - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋
➥ /short - 𝗌𝗁𝗈𝗋𝗍 𝗅𝗂𝗇𝗄𝗌 
➥ /tts - 𝗍𝖾𝗑𝗍 𝗍𝗈 𝗌𝗉𝖾𝖾𝖼𝗁
➥ /lyrics - 𝗅𝗒𝗋𝗂𝖼𝗌 𝗈𝖿 𝗌𝗈𝗇𝗀
"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of 𝖳𝗈𝗏𝗂𝗇𝗈

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
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
    REPORT_TXT = """➤ 𝐇𝐞𝐥𝐩: Rᴇᴘᴏʀᴛ ⚠️

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚛𝚎𝚙𝚘𝚛𝚝 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚛 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎 𝚐𝚛𝚘𝚞𝚙. 𝙳𝚘𝚗'𝚝 𝚖𝚒𝚜𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛ 𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/kB9TkCs8cX0</code>"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

◉ 𝐔𝐒𝐄𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐀𝐍𝐘 𝐕𝐈𝐃𝐄𝐎 𝐅𝐑𝐎𝐌 𝐘𝐎𝐔𝐓𝐔𝐁𝐄

📺 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄

• 𝐓𝐘𝐏𝐄 /video or /mp4 𝐀𝐍𝐃 (https://youtu.be/kB9TkCs8cX0)

• 𝐄𝐗𝐀𝐌𝐏𝐋𝐄:

<code>/mp4 https://youtu.be/kB9TkCs8cX0</code>
<code>/video https://youtu.be/kB9TkCs8cX0</code>"""

    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨
"""

    STICKER_TXT = """𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
 ⭕ 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕ 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄
𝐓𝐘𝐏𝐄 /ytthumb 𝐀𝐍𝐃 𝐒𝐄𝐍𝐓 𝐘𝐎𝐔𝐑 𝐋𝐈𝐍𝐊

◉ 𝐄𝐗𝐀𝐌𝐏𝐋𝐄

<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
