from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from .db import UserDB, SmartphoneDB

userdb = UserDB('users.json')
smartphonedb = SmartphoneDB('smartphones.json')


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboards = [
        [KeyboardButton('🛍 Shop'), KeyboardButton('🛒 Cart')],
        [KeyboardButton('📞 Contact'), KeyboardButton('📝 About')]
    ]

    if userdb.is_user(user.id):
        update.message.reply_html(
            text="""Assalomu alaykum yana bir bor! qaytganingizdan xursandmiz.""",
            reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
        )
        return 

    userdb.add_user(chat_id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)

    update.message.reply_html(
        text=f"""Assalomu alaykum <b>{user.full_name}</b>! smartphone botga xush kelibsiz.""",
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    )
    

def shop(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="shop"
    )
    

def cart(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="cart"
    )
    

def contact(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="contact"
    )
    

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="about"
    )

