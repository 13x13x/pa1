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
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
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
        await app.send_video(kk.id,img, "**Hello {}!\n\nMiddle Class Persons Must Useful Our 👉 @PIFDeals Channel !! Buy It Products On Low Price.. \n\n{}\n\nPowerd By : @PanindiaFilmZ**".format(m.from_user.mention, m.chat.title))
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
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/AutoAcceptRequest32_bot?start=start")
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

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("PIFChannels"))
async def Pifchannels_command(_, m: Message):
    try:
        # Check if the user is a member of a specific channel
        await app.get_chat_member(cfg.CHID, m.from_user.id)
        
        if m.chat.type == enums.ChatType.PRIVATE:
            # Define the keyboard with buttons
            keyboard = [
                [
                    InlineKeyboardButton("🍁 ʜᴅ ᴛᴇʟᴜɢᴜ ᴍᴏᴠɪᴇs 🎖️", url="https://t.me/+wIa9vb3tRho3N2Q1")
                ],
                [
                    InlineKeyboardButton("🧞‍♀️ ʜɪɴᴅɪ - ᴍᴀʟᴀʏᴀʟᴀᴍ 🧐", url="https://t.me/+97U9EyGMz_s2YzQ1"),
                    InlineKeyboardButton("🔔 ᴛᴀᴍɪʟ - ᴋᴀɴɴᴀᴅᴀ 🤖", url="https://t.me/+a3-YTIF0zsFhMDc1")
                ],
                [
                    InlineKeyboardButton("🔥 ʜᴏʟʟʏᴡᴏᴏᴅ - ᴅᴜʙʙᴇᴅ 🎉", url="https://t.me/+9Ks800pBuq9kMmNl"),
                    InlineKeyboardButton("🙂 ᴡᴇʙ - sᴇʀɪᴇs ✨", url="https://t.me/+YcesJaZ8gwUyMTc1")
                ],
                [
                    InlineKeyboardButton("🥵 ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴍᴏᴠɪᴇꜱ ♥️", url="https://t.me/PIFRareHiddenMovies")
                ],
                [
                    InlineKeyboardButton("☀️ ᴅᴠᴅ - ᴅᴀᴛᴀʙᴀsᴇ 🌚", url="https://t.me/PIFOficials"),
                    InlineKeyboardButton("🌿 ʜᴅ - ᴅᴀᴛᴀʙᴀsᴇ 💧", url="https://t.me/PIFOficial")
                ],
                [
                    InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ ⚙", url="https://t.me/BoTzUpdates0"),
                    InlineKeyboardButton("🥵 ᴏɴʟʏ ᴀᴅᴜʟᴛꜱ 🙈", url="https://t.me/Pakkinte_Anty_Bitlu")
                ],
                [
                    InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")
                ]
            ]
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Send the message with the keyboard
            sent_message = await m.reply(
                text="""**__🙂 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴄᴏᴍᴍᴜɴɪᴛʏ!! ᴄʜᴇᴀᴋ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs ʟɪsᴛ ʙᴇʟᴏᴡ!!__**

**__      ʜᴇ'ʟʟᴏ .. ɪ ᴀᴍ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴀᴅᴍɪɴ 🤨__**

**__✨  ᴅᴇᴀʟs 𝟸𝟺/𝟽 :- 
@PIFDeals __** 

**__✨ ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 𝟸.𝟶 
@Telugu_Adults_Rare_Hidden_Movies __**

**__ᴛᴀʀɢᴇᴛ - ʀᴇᴀᴄʜɪɴɢ ᴜʀ sᴇʟғ 🎯__**

**__ғᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs - @PIFAdminBot __**

**__ @PanindiaFilmZ 🔥**__""",
                reply_markup=reply_markup
            )
            
            # Delete the sent message and the command message after 10 seconds
            await asyncio.sleep(60)
            await sent_message.delete()
            await m.delete()

    except Exception as e:
        print(f"An error occurred: {e}")

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
