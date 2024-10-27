from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio
from pyrogram.errors import ChannelInvalid

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://graph.org/file/48cfa4bd374e9f430d653.mp4',
    'https://graph.org/file/118d2ac028f18ac0eafda.mp4',
    'https://graph.org/file/64c15dc5ff0fe8ebc0b73.mp4',
    'https://graph.org/file/f2717422ec9b948127367.mp4',
    'https://graph.org/file/4903445a86cabae4fa02d.mp4',
    'https://graph.org/file/0658f7b252276acfd8fbb.mp4',
    'https://graph.org/file/5edb18364bf8069ea29eb.mp4',
    'https://graph.org/file/0370cca740a4b3ad2ff95.mp4',
    'https://graph.org/file/ed7ef42f3c74b471f16d8.mp4',
    'https://graph.org/file/134cf0af801fa32c2d429.mp4',
    'https://graph.org/file/846c1a28449d8788a5e85.mp4',
    'https://graph.org/file/ebeba3c329a120b8a2e06.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**Hello {}!! Request Approved 🎉 \n\n Middle Class Persons Must Useful Our 👉 @PIFDeals Channel !! Buy It Products On Low Price.. \n\n{}\n\nPowerd By : @PanindiaFilmZ**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ pyrogram ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Define the command handler
@app.on_message(filters.command("send_post"))
def send_post_command(client, message):
    post_text = "This is a sample post."

    try:
        # Get a list of all channels and groups where the bot is an admin
        admin_chats = [
            chat.id
            for chat in client.get_chat_members(message.from_user.id)
            if chat.status == "administrator" and chat.can_post_messages
        ]

        # Send the post to each admin chat
        for chat_id in admin_chats:
            client.send_message(chat_id, post_text)

    except Exception as e:
        print(f"Error: {e}")
    
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍁 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/PanindiaFilmZ"),
                        InlineKeyboardButton("🛒 ᴘɪғ ᴅᴇᴀʟs", url="https://t.me/PIFDeals")
                    ],[
                        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url="https://t.me/AutoAcceptRequest32_bot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/19cd8a38aa67805bd5805.jpg", caption="**🌿 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\nPowerd By : @PanindiaFilmZ**".format(m.from_user.mention, "https://t.me/AutoAcceptRequest32_bot?startgroup"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("sᴛᴀʀᴛ ᴍᴇ ᴘʀɪᴠᴀᴛᴇ..🍁", url="https://t.me/AutoAcceptRequest32_bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🍁 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🍁 Join Channel", url="t.me/PanindiaFilmZ")],
        [InlineKeyboardButton("Try Again", callback_data="chk")]
    ]
        )
        await m.reply_photo("https://telegra.ph/file/d68abc6e85041ab3052e7.jpg", caption="<b>Please join @{} to Use Me.if You Alredy Joined Click Try again Button to Confirm.</b>".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍁 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/PanindiaFilmZ"),
                        InlineKeyboardButton("🛒 ᴘɪғ ᴅᴇᴀʟs", url="https://t.me/PIFDeals")
                    ],[
                        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url="https://t.me/AutoAcceptRequest32_bot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🌿 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\nPowerd By : @PanindiaFilmZ**".format(cb.from_user.mention, "https://t.me/PIFAdminBot"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You Are Not Joined On Channel Join and Try Again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ New Commands ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fl"))
def fl(_, m : Message):
    try:
        text = message.text.splitlines()

        language_map = {
            "Tel": "Telugu",
            "Tam": "Tamil",
            "Eng": "English",
            "Hin": "Hindi",
            "Mal": "Malayalam",
            "Kan": "Kannada",
            "Chi": "Chinese",
            "Spa": "Spanish",
            "Ger": "German",
            "Fre": "French",
            "Rus": "Russian",
            "Jpn": "Japanese",
            "Kor": "Korean",
            # Add more languages as needed
        }

        output = []

        for line in text:
            if "PanindiaFilmZ DB:" in line or line.startswith("@"):
                continue  # Skip headers and unnecessary prefixes

            movie_details = line.split('[')[0].strip()
            languages = ", ".join(full for abbr, full in language_map.items() if abbr in line)

            season = ""
            episode = ""

            if "S" in line and "E" in line:
                season = "Season: " + line.split("S")[1].split("E")[0].strip()
                episode = "Episode: " + line.split("E")[1].split(" ")[0].strip()

            output.append(f"<b>{movie_details}</b>")
            output.append("<blockquote>")
            if languages:
                output.append(f"<b>Languages: {languages}</b>")
            if season:
                output.append(f"<b>{season}</b>")
            if episode:
                output.append(f"<b>{episode}</b>")
            output.append("</blockquote>")

        # Send the filtered output, ensuring to handle large messages
        if output:
            message.reply("\n".join(output))
        else:
            message.reply("No relevant data found.")

    except Exception as e:
        print(f"Error occurred: {e}")  # Print error message for debugging
        message.reply("An error occurred while processing your request. Please try again.")

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
