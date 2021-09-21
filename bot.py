from os import times
from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
    MessageHandler, 
    Filters
)

from io import open
import datetime
import threading
import time
import random

#   TOKEN
updater = Updater(token='1909204788:AAE9uQZXBrgeyfv9SUhE_wnMEvY8gLP9mEs')

#   DISTPATCHER
dispatcher = updater.dispatcher

#   LOGGIN
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def EnviarMensaje(update, context, mensaje):
    context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje) 


# Textos
texto_1 = 'Buenas 😌, te imaginas que existiera alguien tan psicopata, capaz de escribir un programa informático que te hablara como si fuera él? Si? Me alegra que conozcas a tu novio... \n\nPulsa /aqui para continuar leyendo'
texto_2 = 'Nada, ya se que estoy dejando una huella en tu vida, pero siempre puede mejorar verdad? Así que en los ratos que tenía libres cuando hablábamos, escribia este bot. Para que tengas otra historia de conquista cool que contarle a tus nietos 😌 \n\nPulsa /siguiente para continuar leyendo'
texto_3 = 'Entonces... a lo que iba. Poco a poco te vas conviertiendo en alguien muy importante para mí. No llevamos un mes y ya eres mi persona favorita :) \n\nMe haces muy feliz chiquita, no te imaginas cuanto. Antes tenía que lidear con muchos problemas solo, pero ahora cuando algo me afecta, me das un besito y me ayudas a resolverlo. No pense que fuera a tener eso nunca, no pense que fuera a tenerte a tí... Tengo mucha suerte de tener el don para hacerte reír 😌 \n\nPresiona /here para continuar leyendo'
texto_4 = 'Por mi parte prometo cuidarte, mimarte mucho y seguir cargándote para que puedas subir a los sitios altos :) Tengo muchas ganas de descubir cada etapa de nuestra relación y ver a donde nos lleva. No me importa mucho el resultado, siempre que sea contigo, valdrá la pena. \n\nPresiona /press  para seguir leyendo'
texto_5 = 'Bueno... creo que ya va siendo hora que termine mi seductora muela 😌. Solo quería darte una probadita de las cosas que puedo llegar a hacer cuando quiero de verdad a alguien... Tal vez se me ocurran nuevas ideas para este bot, quien sabe 😌... De momento me debes unos cuantos besos. \n\nGracias por ser tú, por estar en mi vida y por hacerla más bonita :)'


def Start(update, context):
    EnviarMensaje(update, context, texto_1)


start_handler = CommandHandler('start', Start)
dispatcher.add_handler(start_handler)

def Segundo(update, context):
    EnviarMensaje(update, context, texto_2)

segundo_handler = CommandHandler('aqui', Segundo)
dispatcher.add_handler(segundo_handler)


def Tercero(update, context):
    EnviarMensaje(update, context, texto_3)

tercero_handler = CommandHandler('siguiente', Tercero)
dispatcher.add_handler(tercero_handler)


def Cuarto(update, context):
    EnviarMensaje(update, context, texto_4)

Cuarto_handler = CommandHandler('here', Cuarto)
dispatcher.add_handler(Cuarto_handler)

def Quinto(update, context):
    EnviarMensaje(update, context, texto_5)

    chat = update.effective_chat.id

    context.bot.send_photo(
        chat, photo=open('photo1.jpg', 'rb')

    )

Quinto_handler = CommandHandler('press', Quinto)
dispatcher.add_handler(Quinto_handler)

#   RUN-BOT
if __name__ == '__main__':


    updater.start_polling()        
    updater.idle()
