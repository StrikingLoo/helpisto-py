"""Readme :  pip install python-telegram-bot --upgrade"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from config import BOT_TOKEN

def validate_user(update):
    id = int(update.message.from_user.id)
    if id != 426071307:
        print(id)
        update.message.reply_text("Sorry, I don't know you")
        return False
    return True

def log_handler(update, context):
    """ Get the userId + firstname + get/store results"""
    chat_id = update.message.chat_id
    with open('notes.txt', 'a') as f:
        f.write('\n'+update.message.text)

    context.bot.send_message(chat_id=chat_id, text=f"{update.message.text} \n---\nLOGGED -- OK")

def weight_handler(update, context):
    """ Get the userId + firstname + get/store results"""
    chat_id = update.message.chat_id
    with open('weights.txt', 'a') as f:
        f.write('\n'+update.message.text)
    context.bot.send_message(chat_id=chat_id, text=f"{update.message.text} \n---\nLOGGED WEIGHT -- OK")

def fallback_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command. Please try with: ")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/log <note>")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/weight <weight>")


def main():
    print("====== starting bot program ======")

    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # example dog_picture_handler to be demonstrated by teacher
    #dispatcher.add_handler(CommandHandler("dog", dog_picture_handler))

    # movie_handler to be filled in by student
    dispatcher.add_handler(CommandHandler("log", log_handler))
    dispatcher.add_handler(CommandHandler("weight", weight_handler))

    # Optional content - fallback handler
    dispatcher.add_handler(MessageHandler(Filters.all, fallback_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()