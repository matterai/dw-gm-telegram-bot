import openai
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, buddy! I am a chat GPT 3.5 bot. I can help you to play DW game.")

async def gm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    openai.api_key = os.getenv('GPT_TOKEN')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "user", "content": update.message.text }
        ]
    )
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].message.content)

if __name__ == '__main__':
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN');
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    gm_handler = CommandHandler('gm', gm)
    application.add_handler(start_handler)
    application.add_handler(gm_handler)
    
    application.run_polling()