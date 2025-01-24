from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#bot token from BotFather
API_TOKEN = '7628069072:AAF1Gz_WOOWz6vEcnwkt4__j3lUzrKfltkk'

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your AI Assistant. How can I help you?')

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"Received message: {user_message}")  # Prints to your PC/console
    await update.message.reply_text(f"You said: {user_message}")

# Main function
def main():
    # Create Application object
    application = Application.builder().token(API_TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
