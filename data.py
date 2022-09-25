from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🌚 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🌚", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❤️‍🔥 sᴜᴩᴩᴏʀᴛ ❤️‍🔥", url="https://t.me/crazy_chat_world"),
         InlineKeyboardButton("🕶 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🕶 ", url="https://t.me/wtf_its_Keshav"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ : [ɢɪᴛʜᴜʙ](https://github.com/isu-op-op/stringsessiongenerator)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [ѕυмιт](https://t.me/Kya_rakhu_smjh_nhi_aa_rha) !
    """
