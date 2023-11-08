# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """ <b>
𝐇𝐞𝐥𝐥𝐨, {}

𝐈𝐭'𝐬 𝐌𝐞 𝐅𝐢𝐥𝐞 𝟐 𝐒𝐡𝐨𝐫𝐭 𝐁𝐨𝐭

𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐥𝐢𝐤𝐞 𝐭𝐡𝐢𝐬 𝐁𝐨𝐓 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐄! 
</b> """

        HELP_TEXT = """ <b>
🎆 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐅𝐈𝐋𝐄𝐒 𝟐 𝐋𝐈𝐍𝐊 𝐁𝐎𝐓
🔘 Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ (Oʀ) Mᴇᴅɪᴀ Fʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ....
🔘 Tʜɪs Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ
🔘 Tʜɪs Lɪɴᴋ Cᴀɴ Bᴇ Usᴇᴅ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Oʀ Sᴛʀᴇᴀᴍ Fɪʟᴇs[Usɪɴɢ Exᴛᴇʀɴᴀʟ Vɪᴅᴇᴏ Pʟᴀʏᴇʀ] Tʜʀᴏᴜɢʜ Mʏ Sᴇʀᴠᴇʀ
🔘 Fᴏʀ Sᴛʀᴇᴀᴍɪɴɢ Jᴜsᴛ Cᴏᴘʏ Tʜᴇ Mᴏɴᴏ Lɪɴᴋ Aɴᴅ Pᴀsᴛᴇ Iᴛ Iɴ Yᴏᴜʀ Vɪᴅᴇᴏ Pʟᴀʏᴇʀ Tᴏ Sᴛᴀʀᴛ Sᴛʀᴇᴀᴍɪɴɢ
🔘 Tʜɪs Bᴏᴛ Sʜᴀʀᴇs Tʜᴇ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ Tᴏ Yᴏᴜ.
🔘 Tʜɪs Bᴏᴛ Is Aʟsᴏ Sᴜᴘᴘᴏʀᴛᴇᴅ Iɴ Cʜᴀɴɴᴇʟs. Aᴅᴅ Mᴇ Tᴏ Cʜᴀɴɴᴇʟ As Aᴅᴍɪɴ Tᴏ Mᴀᴋᴇ Mᴇ Wᴏʀᴋᴀʙʟᴇ...!
🔘 Fᴏʀ Mᴏʀᴇ IɴFᴏʀᴍᴀᴛɪᴏɴ : @KR_Join

🔹𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸
🔞 𝐏𝐨𝐫𝐧 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐘𝐨𝐮 𝐓𝐨 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐁𝐚𝐧 𝐅𝐫𝐨𝐦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬

Iғ Bᴏᴛ Nᴏᴛ Wᴏʀᴋɪɴɢ Aɴᴅ Issᴜᴇs Cᴏɴᴛᴀᴄᴛ 
🧛‍♂️ Aᴅᴍɪɴ : @Mr_Santhosh_28
📢 Uᴘᴅᴀᴛᴇ : @KR_Botz
🗣️ Sᴜᴘᴘᴏʀᴛ : @KR_Join </b>
"""

        DON_TXT = """
<b>💗 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐝𝐨𝐧𝐚𝐭𝐢𝐨𝐧
Dᴏɴᴀᴛᴇ Us Tᴏ Kᴇᴇᴘ Oᴜʀ Sᴇʀᴠɪᴄᴇs Cᴏɴᴛɪɴᴏᴜsʟʏ Aʟɪᴠᴇ 😢
Yᴏᴜ Cᴀɴ Sᴇɴᴅ Aɴʏ Aᴍᴏᴜɴᴛ 
Of 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ 😊
📨 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs:
 
GᴏᴏɢʟᴇPᴀʏ / Pᴀʏᴛᴏɴ / PʜᴏɴPᴀʏ / PᴀʏPᴀʟ
 
 Oʀ Dᴏɴᴀᴛᴇ: Mᴇssᴀɢᴇ Mᴇ @Tamil_KiD </b>
"""

        ABOUT_TEXT = """
**╭────[ 𝗔𝗕𝗢𝗨𝗧 𝗠𝗘 ]────⍟
├🤖 𝐌ʏ 𝐍ᴀᴍᴇ : [Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ](https://t.me/KR_Botz)
├👑 𝐎ᴡɴᴇʀ : [♡︎⏤͟͟͞͞♔︎𝆺𝅥⃝🇸ᴀɴᴛʜᴏs𝐇♔︎ ͟͟͞͞➳࿐](https://telegram.dog/kr_botz)
├😎 𝐃ᴇᴠs : [Lᴀsᴛ 🐲 Dʀᴏɢᴢ](https://telegram.dog/LastDrogz) 
├📕 𝐋ɪʙʀᴀʀʏ : 𝐘ʀᴏɢʀᴀᴍ
├✏️ 𝐋ᴀɴɢᴜᴀɢᴇ : 𝐏ʏᴛʜᴏɴ 𝟹
├💾 𝐃ᴀᴛᴀ 𝐁ᴀsᴇ : 𝐌ᴏɴɢᴏ ᴅʙ
├🌀 𝐌ʏ 𝐒ᴇʀᴠᴇʀ : 𝐇ᴇʀᴏᴋᴜ
├📊 𝐁ᴜɪʟᴅ 𝐒ᴛᴀᴜs : 𝟷.𝟸.𝟶 [ 𝐁ᴇᴛᴀ ]              
╰───────────────⍟ **"""

        stream_msg_text ="""
<b><i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

📂 Fɪʟᴇ ɴᴀᴍᴇ : <code>{}</code>

📦 Fɪʟᴇ ꜱɪᴢᴇ : <code>{}</code>

📥 Dᴏᴡɴʟᴏᴀᴅ : {}

🚸 Nᴏᴛᴇ : Tʜɪs Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ , Nᴏᴛ Exᴘɪʀᴇᴅ

© @{} </b>
"""

    class Test(object):
        START_TEXT = """
<i>👋 Hᴇʏ in Russian,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
         [
             [
                 InlineKeyboardButton("🌿 𝐏𝐞𝐚𝐜𝐞 𝐨𝐟 𝐐𝐭𝐦𝐯 🥀", url='https://t.me/Owner_of_qtmve')
             ]
         ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
         [
             [
                 InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="don")
             ],
             [
                 InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                 InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
             ]
         ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="don")
            ],
            [
                InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
            ]
        ]
    )

    DONATE_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ", url="https://telegram.dog/Lastdrogz")
            ],
            [
                InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
            ]
        ]
    ) 
