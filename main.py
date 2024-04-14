import telegram
from telegram.ext import Updater, CommandHandler
from datetime import datetime

# Replace 'YOUR_TOKEN' with your actual bot token obtained from BotFather
TOKEN = '6853643190:AAEHg8R8-DILYR2JLrnBJsCeVqzblfiUgDA'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your date and time bot. Send /datetime to get the current date and time.")

def datetime_command(update, context):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current date and time: {current_time}")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("datetime", datetime_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
