from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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
    brends = smartphonedb.brends()

    # input: [1, 2, 3, 4, 5, 6, 7] -> ['iphone', 'samsung']
    # output: [[1, 2, 3], [4, 5, 6], [7]]

    inline_keyboards = []
    row = []

    for brend in brends:
        row.append(InlineKeyboardButton(text=brend, callback_data=f'brend:{brend}'))
        
        if len(row) == 3:
            inline_keyboards.append(row)
            row = []

    if row:
        inline_keyboards.append(row)

    update.message.reply_html(
        text="Choose a phone",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )
    

def cart(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="cart"
    )
    

def contact(update: Update, context: CallbackContext) -> None:
    inline_keyboards = [
        [
            InlineKeyboardButton(text='📞 Phone number', callback_data='contact:number'),
            InlineKeyboardButton(text='📧 Email', callback_data='contact:email')
        ],
        [
            InlineKeyboardButton(text='📍 Location', callback_data='contact:location'),
            InlineKeyboardButton(text='📌 Address', callback_data='contact:address')
        ],
    ]
    update.message.reply_html(
        text="Biz bilan bog'lanish",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )
    

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="about"
    )
    

def phone_number(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_html(
        text="Bizning telefon raqamlarimiz:\n\n📞 +998(88)123-12-12\n📞 +998(91)123-12-12"
    )
    

def email(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_html(
        text="Bizning elektron pochtamiz:\n\n📧 smartphonebot@gmail.com"
    )

