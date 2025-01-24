from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Your bot token from BotFather
API_TOKEN = '7628069072:AAF1Gz_WOOWz6vEcnwkt4__j3lUzrKfltkk'


# Load the model and tokenizer
print("Loading TinyLlama-1.1B-Chat-v1.0 model...")
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Ask me anything about your favorite animal!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"User: {user_message}")

    # Structured prompt for clarity
    prompt = f"{user_message.lower()} in one sentence."

    # Generate response
    response = generator(
        prompt,
        max_length=200,
        temperature=0.7,
        repetition_penalty=2.0,
        do_sample=True,
        top_k=40,
        top_p=0.9,
    )

    # Post-process response
    bot_reply = response[0]["generated_text"].strip()
    if bot_reply.startswith(prompt):
        bot_reply = bot_reply[len(prompt):].strip()

    if not bot_reply:
        bot_reply = "Sorry, I couldn't find a fact about that. Try another animal!"

    print(f"Bot: {bot_reply}")
    await update.message.reply_text(bot_reply)

def main():
    application = Application.builder().token(API_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()