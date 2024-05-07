from pyrogram import Client, filters
from pyrogram.types import *
from info import LOG_CHANNEL

@Client.on_message(filters.command("feedback"))
async def feedback(client, message):
  await message.reply_text("/fp - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴘᴜʙʟɪᴠᴀʟʟʏ\n /fa - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴀɴᴏɴʏᴍᴏᴜsʟʏ")

@Client.on_message(filters.command("fp"))
async def feedback_p(client, message):
  fp = message.text.split(" ", 1)[1]
  await message.reply_text(f"ʜɪ {message.from_user.mention},\n ᴛʜᴀɴᴋ ᴜ ғᴏʀ ᴛʜᴇ ғᴇᴇᴅʙᴀᴄᴋ")

  await client.send_message(LOG_CHANNEL, text=f"#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴘᴜʙʟɪᴄ\nғᴇᴇᴅʙᴀᴄᴋ ғʀᴏᴍ {message.from_user.mention}\n ᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{fp}</code>")

@Client.on_message(filters.command("fa"))
async def feedback_a(client, message):
  fa = message.text.split(" ", 1)[1]
  await message.reply_text(f"ʜɪ {message.from_user.mention},\n ᴛʜᴀɴᴋ ᴜ ғᴏʀ ᴛʜᴇ ғᴇᴇᴅʙᴀᴄᴋ")

  await client.send_message(LOG_CHANNEL, text=f"#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴀɴᴏɴʏᴍᴏᴜsʟʏ\nғᴇᴇᴅʙᴀᴄᴋ ғʀᴏᴍ {message.from_user.mention}</b>\n ᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{fa}</code>")

# ɪ ᴀᴍ ɴᴏᴛ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʙᴇɪɴɢ ʏᴏᴜʀ sᴇᴄᴏɴᴅ ғᴀᴛʜᴇʀ ... sᴏ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴍʏ ᴄʀᴇᴅɪᴛ...

#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @tgx_bots

#ᴛʜɪs ʟɪɴᴇ ɪs ғᴏʀ ᴄᴏᴘʏ-ᴘᴀsᴛᴇʀs...
#...ᴡʜɪʟᴇ ʏᴏᴜ ᴀʀᴇ ʀᴇᴍᴏᴠɪɴɢ ᴍʏ ᴄʀᴇᴅɪᴛ ᴀɴᴅ ᴄᴀʟʟɪɴɢ ʏᴏᴜʀsᴇʟғ ᴀ ᴅᴇᴠᴇʟᴏᴘᴇʀʀ...
 # _____ ᴊᴜsᴛ ɪᴍᴀɢɪɴᴇ, Aᴛ ᴛʜᴀᴛ ᴛɪᴍᴇ ɪ ᴀᴍ ғᴜᴄᴋɪɴɢ ʏᴏᴜʀ ᴍᴏᴍ ᴀɴᴅ sɪs ᴀᴛ sᴀᴍᴇ ᴛɪᴍᴇ, ʜᴀʀᴅᴇʀ & ᴛᴏᴏ ʜᴀʀᴅᴇʀ...

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ 𝗧𝗚𝗫 𝗕𝗢𝗧𝗦 ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @tgx_bots Community @Otakflix_Network </b>
