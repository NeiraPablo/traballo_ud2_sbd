import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# Authentication to manage the bot
import os
TOKEN = os.getenv('TOKEN')

# TOKEN = '6982824376:AAGIqh5AU7b-wsVm8dWu2qbyMjoz7eEizWE'

if TOKEN==None:
    print('Lembra indicar a variable de entorno TOKEN')
    print('p.ex: dokcer run --rm -e TOKEN=o_teu_token nomebot')
    exit(1)

# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hola jefe")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="funca")

# This function responds to echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def nasa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=nasa()) 

# function
# async def afirmador(update, context):
#     file = await context.bot.get_file(update.message.document)
#     filename = update.message.document.file_name
#     await file.download_to_drive(filename)
  
#     # envía ficheiro de resposta
#     answer = open('resposta.txt', "rb")
#     await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)

if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    test_handler = CommandHandler('test', test)
    application.add_handler(test_handler)

    nasa_handler = CommandHandler('nasa', nasa)
    application.add_handler(nasa_handler)

    # Handler to manage text messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # application.add_handler(MessageHandler(filters.Document.ALL, afirmador))

    # Keeps the application running
    application.run_polling()