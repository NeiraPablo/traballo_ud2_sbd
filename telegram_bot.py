import logging
import os
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# from dotenv import load_dotenv
# from pathlib import Path
# import requests 

from python_scripts.jokes import *
from python_scripts.nasa_apod import *
from python_scripts.meteo_pred import *
from python_scripts.pokeapi import *
from python_scripts.cine import *
from python_scripts.titular import *
from python_scripts.bbdd import *
from python_scripts.csv_json import *

# Authentication to manage the bot
# load_dotenv()
TOKEN = os.getenv('TOKEN')
if TOKEN==None:
    print('Lembra indicar a variable de entorno TOKEN')
    print('p.ex: dokcer run --rm -e TOKEN=o_teu_token nomebot')
    exit(1)

# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

###############################################################################

# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hola jefe")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def tempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_pred()) 

async def nasa_pic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto, imagen = nasa()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=imagen)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto) 

async def chiste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=joke()) 

async def poke_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto, imagen = pokemon()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=imagen, caption=texto) 

async def titular_dia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=titular(), parse_mode='HTML')

async def pelis_cine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=cartelera(), parse_mode='HTML')

async def inferno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=destino('Pablo'))

async def csv_to_json(update, context):
    try:
        file = await context.bot.get_file(update.message.document.file_id)
        filename = update.message.document.file_name
        downloaded_file_path = os.path.join(os.getcwd(), filename)
        await file.download_to_drive(custom_path=downloaded_file_path)
        tipo, response = csv_file(downloaded_file_path)

        if tipo == 'csv_to_json':
            document_path = f'{os.path.splitext(os.path.basename(filename))[0]}.json'
        elif tipo == 'json_to_csv':  
            document_path = f'{os.path.splitext(os.path.basename(filename))[0]}.csv'
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Ha habido algún problema, formato no válido?')
            return

        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

        if os.path.isfile(document_path):
            if tipo == 'csv_to_json':
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Aquí está el archivo JSON convertido:', reply_to_message_id=update.message.message_id)
                await context.bot.send_document(chat_id=update.effective_chat.id, document=open(document_path, 'rb'))
            elif tipo == 'json_to_csv':
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Aquí está el archivo CSV convertido:', reply_to_message_id=update.message.message_id)
                await context.bot.send_document(chat_id=update.effective_chat.id, document=open(document_path, 'rb'))
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id, text='Ha habido algún error')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Ha habido algún error')
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Error: {str(e)}')


# function
# async def afirmador(update, context):
#     file = await context.bot.get_file(update.message.document)
#     filename = update.message.document.file_name
#     await file.download_to_drive(filename)
  
#     # envía ficheiro de resposta
#     answer = open('resposta.txt', "rb")
#     await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)

###############################################################################

if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    tempo_handler = CommandHandler('tempo', tempo)
    application.add_handler(tempo_handler)

    nasa_handler = CommandHandler('nasa', nasa_pic)
    application.add_handler(nasa_handler)

    joke_handler = CommandHandler('chiste', chiste)
    application.add_handler(joke_handler)

    poke_handler = CommandHandler('poke', poke_info)
    application.add_handler(poke_handler)

    titular_handler = CommandHandler('titular', titular_dia)
    application.add_handler(titular_handler)

    cine_handler = CommandHandler('cartelera', pelis_cine)
    application.add_handler(cine_handler)

    inferno_handler = CommandHandler('inferno', inferno)
    application.add_handler(inferno_handler)

    application.add_handler(MessageHandler(filters.Document.ALL, csv_to_json))

    # Handler to manage text messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # application.add_handler(MessageHandler(filters.Document.ALL, afirmador))

    # Keeps the application running
    application.run_polling()