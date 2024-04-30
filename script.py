class Txt(object):

    PRIVATE_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴅᴏ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ɪɴ ɴᴇɢʟɪɢɪʙʟᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏss ᴏғ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ
"""
    GROUP_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ɴᴇɢʟɪɢɪʙʟᴇ sɪᴢᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏᴏsɪɴɢ ᴛʜᴇ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ

❗**Yᴏᴜ ʜᴀsɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴍᴇ ʏᴇᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ғɪʀsᴛ sᴛᴀʀᴛ ᴍᴇ sᴏ ɪ ᴄᴀɴ ᴡᴏʀᴋ ғʟᴀᴡʟᴇssʟʏ**
"""
    PROGRESS_BAR = """<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

    SEND_FFMPEG_CODE = """
❪ SET CUSTOM FFMPEG CODE ❫

Send me the correct ffmpeg code for more info.


☛ <a href=https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg#:~:text=ffmpeg%20%2Di%20input.mp4%20%2Dvcodec%20libx265%20%2Dcrf%2028%20output.mp4> FOR HELP </a>

⦿ Fᴏʀᴍᴀᴛ Oɴ Hᴏᴡ Tᴏ Sᴇᴛ

☞ ffmpeg -i input.mp4 <code> -c:v libx264 -crf 23 </code> output.mp4

<code> -c:v libx264 -crf 23 </code> Tʜɪs ɪs ʏᴏᴜʀ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ ✅

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Want_To_Know_Mee
"""

    SEND_METADATA ="""
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="My Video" -metadata author="John Doe" -metadata:s:s title="Subtitle Title" -metadata:s:a title="Audio Title" -metadata:s:v title="Video Title" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Want_To_Know_Mee
"""

    
    HELP_MSG = """
Available commands:-

➜ /set_ffmpeg - To set custom ffmpeg code
➜ /set_metadata - To set custom metadata code
➜ /set_caption - To set custom caption
➜ /del_ffmpeg - Delete the custom ffmpeg code
➜ /del_caption - Delete caption
➜ /see_ffmpeg - View custom ffmpeg code
➜ /see_metadata - View custom metadata code
➜ /see_caption - View caption 
➜ To Set Thumbnail just send photo


<b>⦿ Developer:</b> <a href=https://t.me/Want_To_Know_Mee>ᶦτͫ𝒛⃪ͤ ꯭𝐒ʜɪᴠ𝆺꯭𝅥.ۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗ ༎𓆪─̶̶⃛͢🐼⛧‌ٖٖٖٖٖٖٜٖٖٖٖ ❄️</a>
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : @{}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
├👑 Instagram : <a href=https://www.instagram.com/sanjuu____03>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a> 
├☃️ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
├📕 Lɪʙʀᴀʀy : <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
├🌀 ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://t.me/Want_To_Know_Mee>˹AD_Cᴏᴍᴘʀᴇssᴏʀ_Bᴏᴛ˼</a>
╰───────────────⍟ """
