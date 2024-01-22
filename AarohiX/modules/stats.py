from pyrogram import filters, Client
from pyrogram.types import Message

from AarohiX import OWNER, AarohiX
from AarohiX.database.chats import get_served_chats
from AarohiX.database.users import get_served_users


@AarohiX.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )
