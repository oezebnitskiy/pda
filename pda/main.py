# tts_bot 

# What?: bot -> get text -> return .mp3

import telebot
from telebot import types
import json
import token


bot_token = token.token
VOICE_LEN = 5000
CHANNEL_ID = -1001698183512
bot = telebot.TeleBot(bot_token)


callback_button_1 = types.InlineKeyboardButton(text="🧑🏻‍💻", callback_data="work")
callback_button_2 = types.InlineKeyboardButton(text="🎮", callback_data="ongoing")
callback_button_3 = types.InlineKeyboardButton(text="👨🏼‍🎓", callback_data="school")
callback_button_4 = types.InlineKeyboardButton(text="🚀", callback_data="thenext")
callback_button_5 = types.InlineKeyboardButton(text="😌", callback_data="affirmations")
callback_button_6 = types.InlineKeyboardButton(text="🎒", callback_data="holes")
callback_button_7 = types.InlineKeyboardButton(text="👟", callback_data="stones")
callback_button_8 = types.InlineKeyboardButton(text="✨", callback_data="stars")
#

# keyboard = types.InlineKeyboardMarkup(row_width=3).add(callback_button_1,callback_button_2,callback_button_3,callback_button_4,callback_button_5)
keyboard = types.InlineKeyboardMarkup([[callback_button_1,callback_button_2,callback_button_3],[callback_button_4,callback_button_5],
[callback_button_6,callback_button_7,callback_button_8]])

def safe_open(filename):
    try:
        return open(f"./docs/{filename}").read()
    except FileNotFoundError:
        return filename

pages = {}
for page in  ['work', 'ongoing', 'school','thenext','affirmations']:
    for modus in ['holes', 'stones', 'stars']:
        filename = f"{page}_{modus}"
        pages[filename] = safe_open(filename)

current_page = "welcome"
current_state = "holes"

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global current_page
    global current_state
    last_page = f"{current_page}_{current_state}"
    # save the edited message
    mes_text = bot.get_chat(CHANNEL_ID).pinned_message.json['text']
    with open(f"./docs/{last_page}.txt",'w') as file:
        file.write(mes_text)
    pages[last_page] = mes_text
    # change the page and change page status
    if call.data in ['work','ongoing','school','thenext','affirmations']:
        # change page
        new_page = f"{call.data}_{current_state}"
        current_page = call.data
    else:
        new_page = f"{current_page}_{call.data}"
        current_state = call.data
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=pages[new_page], reply_markup=keyboard)


callback_button_1 = types.InlineKeyboardButton(text="🧑🏻‍💻", callback_data="")
callback_button_2 = types.InlineKeyboardButton(text="🎮", callback_data="ongoing")
callback_button_3 = types.InlineKeyboardButton(text="👨🏼‍🎓", callback_data="school")
callback_button_4 = types.InlineKeyboardButton(text="🚀", callback_data="thenext")
callback_button_5 = types.InlineKeyboardButton(text="😌", callback_data="affirmations")
callback_button_6 = types.InlineKeyboardButton(text="🎒", callback_data="holes")
callback_button_7 = types.InlineKeyboardButton(text="👟", callback_data="stones")
callback_button_8 = types.InlineKeyboardButton(text="✨", callback_data="stars")

def send_start_message():
    # Send message and pin it 
    result = bot.send_message(CHANNEL_ID, "Привет!", reply_markup=keyboard)
    bot.pin_chat_message(CHANNEL_ID, result.message_id)


if __name__ == '__main__':
    send_start_message()
    #bot.edit_message_text(chat_id=CHANNEL_ID, message_id=2, text="тру-ту-ту")
    bot.infinity_polling()