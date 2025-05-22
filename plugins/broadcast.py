#broadcast Code All Repo Support

from pyrogram import Client, filters
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def speed_verupikkals(bot, message):
    if len(message.command) == 1:
        matrix = 0  # No matrix value provided, skip no users
    else:
        try:
            matrix = int(message.text.split(None, 1)[1])  # Extract matrix value
        except ValueError:
            await message.reply("Invalid matrix value. Please enter a number.")
            return  # Exit function if matrix value is invalid
    start_time = time.time()
    b_msg = message.reply_to_message
    sts = await message.reply("processing...")
    users = await db.get_all_users()
    users_list = await users.to_list(None)  
    total_users = len(users_list)    
    users = await db.get_all_users() 
    # Skip specified number of users
    skipped_count = 0
    success = 0
    failed = 0
    async for user in users:  # Iterate directly over cursor
        if skipped_count < matrix:
            skipped_count += 1             
        else:# Skip users until reaching the desired matrix value
            try:
                await b_msg.copy(chat_id=int(user['id']))
                success += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await b_msg.copy(chat_id=int(user['id']))
            except InputUserDeactivated:
                await db.delete_user(int(user['id']))
                failed += 1
            except UserIsBlocked:
                await db.delete_user(int(user['id']))
                failed += 1
            except Exception as e:                
                failed += 1

        process = success + failed

        if process % 500 == 1:
            elapsed_time = datetime.timedelta(seconds=int(time.time() - start_time))
            await sts.edit(f"Progress: {process+matrix}/{total_users}\nSuccess: {success}\nFailed: {failed}\nElapsed Time: {elapsed_time}")

    # No need for separate start_time variable as loop starts here
    time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts.edit(f"Completed\nTotal : {total_users}\nSuccess : {success}\nSkipped : {skipped_count}\nFailed : {failed}\nTime Taken : {time_taken}")
