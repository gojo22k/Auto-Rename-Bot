import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","madflixbotz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hᴇʟʟᴏ {} 
    
➻ Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀғᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.
    
➻ Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Aᴜᴛᴏ Rᴇɴᴀᴍᴇ Oғ Yᴏᴜʀ Fɪʟᴇs.
    
➻ Tʜɪs Bᴏᴛ Aʟsᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.
    
➻ Usᴇ /tutorial Cᴏᴍᴍᴀɴᴅ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ.    
<b>Bot Is Made By @aniflixClou</b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Usᴇ Tʜᴇsᴇ Kᴇʏᴡᴏʀᴅs Tᴏ Sᴇᴛᴜᴘ Cᴜsᴛᴏᴍ Fɪʟᴇ Nᴀᴍᴇ

✓ ᴇᴘɪsᴏᴅᴇ :- Tᴏ Rᴇᴘʟᴀᴄᴇ Eᴘɪsᴏᴅᴇ Nᴜᴍʙᴇʀ
✓ ᴏ̨ᴜᴀʟɪᴛʏ :- Tᴏ Rᴇᴘʟᴀᴄᴇ Vɪᴅᴇᴏ Rᴇsᴏʟᴜᴛɪᴏɴ

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - Episode - quality  [Dual Audio] - @aniflixClou </code>
<b>➻ Then Send the file with respective captions</code>
<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b> <a href='https://t.me/AutoRenameXBot'>Auto Rename Bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Koyeb</a>
<b>📢 Channel :</b> <a href='https://t.me/aniflix.clou'>Aniflix</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/aniflix.clou'>Ankit</a>
    
<b>♻️ Bot Made By :</b> @AniflixClou"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Sɪᴢᴇ</b> : {1} | {2}
<b>⏳️ Dᴏɴᴇ</b> : {0}%
<b>🚀 Sᴘᴇᴇᴅ</b> : {3}/s
<b>⏰️ Eᴛᴀ</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>rasanandamohapatra2014@okhdfcbank</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""
