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

    inline_btn = InlineKeyboardButton(text='Close', callback_data='close')
    if row:
        row.append(inline_btn)
        inline_keyboards.append(row)
    else:
        inline_keyboards.append([inline_btn])

    update.message.reply_html(
        text="Choose a phone",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )
    

def cart(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    items = userdb.get_items(chat_id=user.id)
    text = ""

    total = 0
    if items:
        for item in items:
            phone = smartphonedb.phone(brend=item['brend'], id=item['phone_id'])
            total += phone['price']
            text += f"<b>model:</b> {phone['name']}\n<b>brend:</b> {phone['company']}\n<b>color:</b> {phone['color']}\n<b>ram:</b> {phone['RAM']}\n<b>memory:</b> {phone['memory']}\n<b>price:</b> ${phone['price']}\n\n"
    else:
        update.message.reply_html(
            text=f"<b>your cart is empty</b>"
        )
        return

    inline_keyboards = [
        [
            InlineKeyboardButton(text='Buy', callback_data='buy'),
            InlineKeyboardButton(text='Clear', callback_data='clear'),
        ]
    ]
    update.message.reply_html(
        text=f"{text}\n\n<b>detail</b>: \n   <i>items</i>: {len(items)}\n   <i>total</i>: {total}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
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


def brend(update: Update, context: CallbackContext) -> None:
    callback_data = update.callback_query.data
    brend = callback_data.split(':')[1]

    phones = smartphonedb.phones(brend)

    inline_keyboards = []
    for phone in phones:
        inline_btn = InlineKeyboardButton(text=f"{phone.doc_id}. {phone['name']}", callback_data=f"phone:{phone['company']}:{phone.doc_id}") # 'phone:iphone:3'
        inline_keyboards.append([inline_btn])

    inline_btn = InlineKeyboardButton(text='Close', callback_data='close')
    inline_keyboards.append([inline_btn])

    update.callback_query.message.reply_html(
        text='Choose a phone',
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    )


def phone(update: Update, context: CallbackContext) -> None:
    callback_data = update.callback_query.data
    _, brend, phone_id = callback_data.split(':')

    phone = smartphonedb.phone(brend=brend, id=phone_id)

    inline_keyboards = [
        [InlineKeyboardButton(text='📦 Add to cart', callback_data=f"cart:{phone['company']}:{phone.doc_id}")]
    ]

    update.callback_query.message.reply_photo(
        photo=phone['img_url'],
        caption=f"<b>model:</b> {phone['name']}\n<b>brend:</b> {phone['company']}\n<b>color:</b> {phone['color']}\n<b>ram:</b> {phone['RAM']}\n<b>memory:</b> {phone['memory']}\n<b>price:</b> ${phone['price']}\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboards),
        parse_mode='HTML'
    )


def add_cart(update: Update, context: CallbackContext) -> None:
    callback_data = update.callback_query.data
    _, brend, phone_id = callback_data.split(':')

    user = update.effective_user

    userdb.add_item(
        chat_id=user.id,
        brend=brend,
        phone_id=phone_id
    )

    update.callback_query.delete_message()

    update.callback_query.message.reply_text(
        text='added item'
    )


def close(update: Update, context: CallbackContext) -> None:
    update.callback_query.delete_message()
    update.callback_query.message.reply_html(
        text="<b>closed</b>"
    )


def clear(update: Update, context: CallbackContext) -> None:
    update.callback_query.delete_message()
    user = update.effective_user
    userdb.clear_items(chat_id=user.id)
    update.callback_query.message.reply_html(
        text="<b>cleared cart</b>"
    )
