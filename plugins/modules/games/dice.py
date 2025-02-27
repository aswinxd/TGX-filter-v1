# codes added by @tgxupdate
# use with proper credits

from pyrogram import Client, filters, enums
from info import COMMAND_HAND_LER
from plugins.helper.cust_p_filters import f_onw_fliter

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["roll", "dice"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
